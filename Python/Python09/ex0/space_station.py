from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation\n========================================")

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        if valid_station.is_operational:
            status_msg = 'Operational'
        else:
            status_msg = 'Offline'
        print(f"Status: {status_msg}")

    except ValidationError as e:
        print("Error creating valid station:")
        print(e)

    print("\n" + "========================================")

    try:
        SpaceStation(
            station_id="ID",
            name="Alpha Station",
            crew_size=25,
            power_level=150.0,
            oxygen_level=98.0,
            last_maintenance="2026-04-13"
        )
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'].replace('Value error, ', ''))


if __name__ == "__main__":
    main()
