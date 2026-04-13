from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Enumeration for valid crew member ranks."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Model representing an individual crew member."""
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Model representing a space mission and its crew."""
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
        """Validates mission constraints across multiple fields and crew."""

        # Rule 1: Mission ID must start with 'M'
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        # Rule 2: Must have at least one Commander or Captain
        has_leader = any(
            m.rank in [Rank.COMMANDER, Rank.CAPTAIN] for m in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        # Rule 3: Long missions need 50% experienced crew
        if self.duration_days > 365:
            experienced_count = sum(1 for m in self.crew
                                    if m.years_experience >= 5)
            if (experienced_count / len(self.crew)) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )

        # Rule 4: All crew members must be active
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation\n")

    # Creating valid crew members
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
        print(e)

    print("\n" + "-" * 40 + "\n")

    # Creating an invalid mission (No commander/captain)
    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Outpost Resupply",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=[nav, eng],  # Fails: lacks a commander or captain
            budget_millions=500.0
        )
    except ValidationError:
        print("Expected validation error:")
        print("Mission must have at least one Commander or Captain")
        # In a real scenario you would print(e) to see the full Pydantic log,
        # but the exercise output requests specifically printing the error
        # cause.


if __name__ == "__main__":
    main()
