from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':

        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            m.rank in [Rank.COMMANDER, Rank.CAPTAIN] for m in self.crew
        )
        if not has_leader:
            raise ValueError(
            )

        if self.duration_days > 365:
            experienced_count = sum(1 for m in self.crew
                                    if m.years_experience >= 5)
            if (experienced_count / len(self.crew)) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation\n========================================")

    cmd = CrewMember(
        member_id="C001", name="Sarah Connor", rank=Rank.COMMANDER,
        age=45, specialization="Mission Command", years_experience=20
    )
    nav = CrewMember(
        member_id="L001", name="John Smith", rank=Rank.LIEUTENANT,
        age=32, specialization="Navigation", years_experience=8
    )
    eng = CrewMember(
        member_id="O001", name="Alice Johnson", rank=Rank.OFFICER,
        age=28, specialization="Engineering", years_experience=4
    )

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[cmd, nav, eng],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for m in valid_mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print("Unexpected validation error:")
        for err in e.errors():
            print(err['msg'])

    print("\n" + "========================================")

    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Outpost Resupply",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=[nav, eng],
            budget_millions=500.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
