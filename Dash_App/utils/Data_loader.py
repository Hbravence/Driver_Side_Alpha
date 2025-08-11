# utils/data_loader.py
import os
import glob
import pandas as pd

def load_latest_csv(city: str, data_type: str, pattern: str = "*.parquet") -> pd.DataFrame:
    """
    Load the latest CSV file from a modeled directory for a given city and data type.
    
    Args:
        city (str): City name (e.g., 'LA')
        data_type (str): 'Events' or 'flights'
        pattern (str): Filename pattern to match (e.g., 'event_clustering*.csv')
    
    Returns:
        pd.DataFrame: Loaded DataFrame from the latest matching file
    
    Raises:
        FileNotFoundError: If no matching file is found
    """
    base_dir = os.getcwd()
    root_dir = os.path.dirname(base_dir)

    if data_type.lower() == "events":
        folder_path = os.path.join(root_dir, city, "Events", "events_data", f"{city}_events", "modeled")
    elif data_type.lower() == "flights":
        folder_path = os.path.join(root_dir, city, "flights", "flight_data", "modeled")
    else:
        raise ValueError(f"Unsupported data_type: {data_type}")

    csv_files = glob.glob(os.path.join(folder_path, pattern))
    if not csv_files:
        raise FileNotFoundError(f"No files matching {pattern} found in {folder_path}")

    latest_file = max(csv_files, key=os.path.getmtime)
    return pd.read_parquet(latest_file)