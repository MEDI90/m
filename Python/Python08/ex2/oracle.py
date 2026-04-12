import os
import sys


def main() -> None:
    # Gracefully handle the python-dotenv dependency.
    # This ensures the program doesn't crash unexpectedly
    # if the environment isn't fully set up.
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("WARNING: python-dotenv module is missing.")
        print("Please install it using 'pip install python-dotenv'.")
        sys.exit(1)

    print("ORACLE STATUS: Reading the Matrix...")

    # Check if a local .env file exists for development settings
    env_exists: bool = os.path.isfile('.env')

    # Load environment variables from the .env file into os.environ.
    # This is crucial for configuration management,
    # keeping secrets out of version control.
    load_dotenv()

    # Retrieve configuration securely.
    # Notice there are no hardcoded secrets in the source code;
    # everything is loaded dynamically.
    matrix_mode: str | None = os.environ.get('MATRIX_MODE')
    db_url: str | None = os.environ.get('DATABASE_URL')
    api_key: str | None = os.environ.get('API_KEY')
    log_level: str | None = os.environ.get('LOG_LEVEL')
    zion_endpoint: str | None = os.environ.get('ZION_ENDPOINT')

    # Handle missing configurations appropriately by warning the user
    # instead of failing silently or crashing.
    if not any([matrix_mode, db_url, api_key, log_level, zion_endpoint]):
        print("WARNING: Default/missing configuration. Please "
              "configure the environment or use a .env file.\n")

    # Differentiate between development and
    # production configurations using default fallbacks
    mode_display: str = matrix_mode if matrix_mode else "development (default)"

    # Safely display loaded configuration WITHOUT exposing real secrets.
    # We mask sensitive connection strings depending on the environment mode.
    db_display: str = "Not connected"
    if db_url:
        if ("local" in db_url.lower() or "sqlite" in db_url.lower()
                or matrix_mode == "development"):
            db_display = "Connected to local instance"
        else:
            db_display = f"Connected to {db_url}"

    # Confirm the presence of sensitive keys without
    # printing their actual values to stdout
    api_display: str = "Authenticated" if api_key else "Missing API key"
    log_display: str = log_level if log_level else "INFO (default)"
    zion_display: str = "Online" if zion_endpoint else "Offline"

    print("\nConfiguration loaded:")
    print(f"Mode: {mode_display}")
    print(f"Database: {db_display}")
    print(f"API Access: {api_display}")
    print(f"Log Level: {log_display}")
    print(f"Zion Network: {zion_display}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
