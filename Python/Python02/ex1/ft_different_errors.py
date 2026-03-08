def garden_operations(action: str) -> None:
    if action == "value":
        int("abs")
    elif action == "zero":
        1 / 0
    elif action == "file":
        open("missing.txt", "r")
    elif action == "key":
        garden = {"tree": 5}
        garden["missing_plant"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
