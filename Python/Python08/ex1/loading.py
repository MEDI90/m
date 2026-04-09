import sys
import importlib

def check_dependencies():
    packages = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'matplotlib': 'Visualization ready'
    }
    
    missing_packages = []
    
    for pkg, desc in packages.items():
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, '__version__', 'unknown')
            print(f"[OK] {pkg} ({version}) - {desc}")
        except ImportError:
            missing_packages.append(pkg)
            # Do not print failure here to match the expected format closer, 
            # or we can print it if we want. The PDF example only showed OKs.
            
    return missing_packages

def main():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    missing = check_dependencies()
    
    if missing:
        print("\nERROR: Missing dependencies detected.")
        print(f"Missing: {', '.join(missing)}")
        print("\nTo install with pip, run:")
        print("    pip install -r requirements.txt")
        print("To install with Poetry, run:")
        print("    poetry install")
        print("    poetry run python loading.py")
        sys.exit(1)
        
    print("Analyzing Matrix data...")
    
    # Deferred imports after dependency check to avoid ModuleNotFoundError
    # Exceptionnally, flake8/mypy errors might occur for this late import
    # but we prevent them gracefully from crashing the check sequence.
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    print("Processing 1000 data points...")
    num_points = 1000
    
    # Generate Matrix data using numpy as the source of the dataset
    # We use numpy linspace and random to create 1000 points
    # Seed for reproducibility in the Matrix
    np.random.seed(42)
    time_series = np.linspace(0, 100, num_points)
    signal_core = np.sin(time_series) + np.random.normal(0, 0.1, num_points)
    
    # Load into pandas for manipulation
    df = pd.DataFrame({
        'Time': time_series,
        'Matrix_Signal': signal_core
    })
    
    # pandas data manipulation: Calculate rolling average
    df['Signal_Smoothed'] = df['Matrix_Signal'].rolling(window=20).mean()
    
    print("Generating visualization...")
    
    # Visualization using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Matrix_Signal'], alpha=0.4, label='Raw Signal')
    plt.plot(df['Time'], df['Signal_Smoothed'], color='red', linewidth=2, label='Smoothed Matrix Signal')
    plt.title('The Matrix - Data Analysis')
    plt.xlabel('Time')
    plt.ylabel('Signal Strength')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the plot
    filename = 'matrix_analysis.png'
    plt.savefig(filename)
    plt.close()
    
    print("Analysis complete!")
    print(f"Results saved to: {filename}")

if __name__ == "__main__":
    main()
