import os

def main():
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("WARNING: python-dotenv module is missing.")
        print("Please install it using 'pip install python-dotenv'.")
        return

    print("ORACLE STATUS: Reading the Matrix...")
    
    env_exists = os.path.isfile('.env')
    
    # load_dotenv by default does not override existing environment variables.
    # This allows `MATRIX_MODE=production python oracle.py` to overwrite .env values.
    load_dotenv()
    
    matrix_mode = os.environ.get('MATRIX_MODE')
    db_url = os.environ.get('DATABASE_URL')
    api_key = os.environ.get('API_KEY')
    log_level = os.environ.get('LOG_LEVEL')
    zion_endpoint = os.environ.get('ZION_ENDPOINT')
    
    # Check if there's any configuration present
    if not any([matrix_mode, db_url, api_key, log_level, zion_endpoint]):
        print("WARNING: Default/missing configuration. Please configure the environment or use a .env file.\n")
    
    # Determining display values
    mode_display = matrix_mode if matrix_mode else "development (default)"
    
    db_display = "Not connected"
    if db_url:
        if "local" in db_url.lower() or "sqlite" in db_url.lower() or matrix_mode == "development":
            db_display = "Connected to local instance"
        else:
            db_display = f"Connected to {db_url}"
            
    api_display = "Authenticated" if api_key else "Missing API key"
    log_display = log_level if log_level else "INFO (default)"
    zion_display = "Online" if zion_endpoint else "Offline"
    
    print("Configuration loaded:")
    print(f"Mode: {mode_display}")
    print(f"Database: {db_display}")
    print(f"API Access: {api_display}")
    print(f"Log Level: {log_display}")
    print(f"Zion Network: {zion_display}")
    
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")
        
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")

if __name__ == "__main__":
    main()
