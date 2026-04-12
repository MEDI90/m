import sys
import os
import site


def is_in_virtual_env() -> bool:
    # When a virtual environment is active,
    # sys.prefix points to the venv's directory,
    # while sys.base_prefix continues to
    # point to the global Python installation.
    # If they are different, it confirms we
    # are running safely inside the isolated construct.
    return sys.prefix != sys.base_prefix


def print_global_warning() -> None:
    # Outputs a warning when the script is executed
    # using the system's global Python interpreter.
    print()
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print()
    print("Then run this program again.")


def print_venv_success() -> None:
    # Extracts and formats the specific environment name and path for display.
    env_name: str = os.path.basename(sys.prefix)
    env_path: str = sys.prefix

    print()
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")

    # Fetches the specific directory where third-party
    # packages will be stored in this environment.
    site_packages: list[str] = site.getsitepackages()
    if site_packages:
        print(site_packages[0])
    else:
        # Fallback mechanism in case getsitepackages() returns an empty list
        for path in sys.path:
            if "site-packages" in path:
                print(path)
                break


def main() -> None:
    # Main execution flow: routes to the appropriate
    # output based on the environment check.
    if is_in_virtual_env():
        print_venv_success()
    else:
        print_global_warning()


if __name__ == "__main__":
    main()
