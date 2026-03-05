class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def catching_err() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("PlantError: The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught {e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("WaterError: Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught {e}")

    print("\nTesting catching all garden errors...")
    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    catching_err()
