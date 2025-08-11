import pandas as pd

def filter_events_by_day(df, target_date, date_column='date'):
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    target = pd.to_datetime(target_date).date()
    
    return df[df[date_column].dt.date == target]


def filter_by_iata(df, iata_code, column='arrival_iataCode'):
    """
    Filters DataFrame by IATA code or list of codes.
    
    Parameters:
    - df: pandas DataFrame
    - iata_code: string or list of strings
    - column: name of the column containing IATA codes
    
    Returns:
    - Filtered DataFrame
    """
    if iata_code is None:
        return df
    if isinstance(iata_code, list):
        return df[df[column].isin(iata_code)]
    return df[df[column] == iata_code]