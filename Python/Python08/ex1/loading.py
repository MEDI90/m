import sys
import importlib


def check_dependencies() -> list[str]:
    # Dictionary mapping required packages to their descriptive purpose
    packages: dict[str, str] = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'matplotlib': 'Visualization ready'
    }

    missing_packages: list[str] = []

    # Iterate through required packages and attempt to import them dynamically.
    # This prevents the program from crashing
    # immediately if a dependency is missing,
    # allowing us to handle errors gracefully as required.
    for pkg, desc in packages.items():
        try:
            module = importlib.import_module(pkg)
            # Fetch the package version dynamically
            # to display version information
            version: str = getattr(module, '__version__', 'unknown')
            print(f"[OK] {pkg} ({version})")
            print(desc)
        except ImportError:
            missing_packages.append(pkg)

    return missing_packages


def detect_environment() -> None:
    # Check the executable path to identify
    # if Poetry is managing the environment
    if 'pypoetry' in sys.executable or 'poetry' in sys.executable:
        print("\nEnvironment detected: Poetry")
    # In a standard pip virtual environment,
    # sys.prefix differs from sys.base_prefix
    elif sys.prefix != sys.base_prefix:
        print("\nEnvironment detected: Pip Virtual Environment")
    else:
        print("\nEnvironment detected: Global/System")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    missing: list[str] = check_dependencies()

    # Handle missing dependencies by providing helpful error messages
    # and clear installation instructions for both pip and Poetry.
    if missing:
        print("\nERROR: Missing dependencies detected.")
        print(f"Missing: {', '.join(missing)}")
        print("\nTo install with pip, run:")
        print("    pip install -r requirements.txt")
        print("To install with Poetry, run:")
        print("    poetry install")
        print("    poetry run python loading.py")
        sys.exit(1)

    detect_environment()

    print("\nAnalyzing Matrix data...")

    # Late imports are used here to ensure they only execute after
    # check_dependencies() verifies the packages are actually installed.
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Processing 1000 data points...")
    num_points: int = 1000

    # Simulate data using numpy mathematical functions rather
    # than hardcoding data.
    np.random.seed(42)
    time_series: np.ndarray = np.linspace(0, 100, num_points)
    # Generate a base sine wave signal and inject Gaussian noise
    signal_core: np.ndarray = np.sin(
        time_series) + np.random.normal(0, 0.1, num_points)

    # Use pandas DataFrame to structure and analyze the simulated data
    df: pd.DataFrame = pd.DataFrame({
        'Time': time_series,
        'Matrix_Signal': signal_core
    })

    # Apply a rolling window mean to smooth the noisy data for analysis
    df['Signal_Smoothed'] = df['Matrix_Signal'].rolling(window=20).mean()

    print("Generating visualization...")

    # Generate the required data visualization using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Matrix_Signal'], alpha=0.4, label='Raw Signal')
    plt.plot(df['Time'], df['Signal_Smoothed'], color='red',
             linewidth=2, label='Smoothed Matrix Signal')
    plt.title('The Matrix - Data Analysis')
    plt.xlabel('Time')
    plt.ylabel('Signal Strength')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Save the plot to a file instead of displaying
    # it to ensure it runs headlessly
    filename: str = 'matrix_analysis.png'
    plt.savefig(filename)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {filename}")


if __name__ == "__main__":
    main()
