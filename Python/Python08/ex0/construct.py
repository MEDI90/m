import sys
import os
import site


def is_in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def print_global_warning() -> None:
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

    site_packages: list[str] = site.getsitepackages()
    if site_packages:
        print(site_packages[0])
    else:
        for path in sys.path:
            if "site-packages" in path:
                print(path)
                break


def main() -> None:
    if is_in_virtual_env():
        print_venv_success()
    else:
        print_global_warning()


if __name__ == "__main__":
    main()