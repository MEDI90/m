def garden_operations() -> None:
    print("\nTesting ValueError...")
    try:
        int("abs")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        1/0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        if file:
            file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("\nTesting KeyError...")
    try:
        k = "missing_plant"
        garden = {"tree": 5}
        garden[k]
    except KeyError:
        print(f"Caught KeyError: '{k}'")
    print("\nTesting multiple errors together...")
    try:
        int("abc")
        1 / 0
        garden = {"tree": 5}
        garden["missing_plant"]
        open("missing.txt", "r")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(f"Error: {e}")
