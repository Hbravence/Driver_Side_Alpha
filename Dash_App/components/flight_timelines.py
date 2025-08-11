# components/flight_timelines.py
import pandas as pd
import plotly.express as px

def generate_flight_timelines(df: pd.DataFrame, source_90min: str = "flight_90min"):
    """
    Generate two timeline plots for flights: one for 90-minute clusters, one for others.
    
    Args:
        df (pd.DataFrame): Flight data with start_time, end_time, flight_count, source, rank, flight_date
        source_90min (str): Label used to identify 90-minute clusters
    
    Returns:
        tuple: (timeline_90min_fig, timeline_180min_fig)
    """
    # Parse timestamps
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])

    # Tooltip
    df["tooltip"] = "Flights: " + df["flight_count"].astype(str)

    # Split by source
    flight_90 = df[df['source'] == source_90min]
    flight_180 = df[df['source'] != source_90min]

    # 90-Minute Timeline
    fig_90 = px.timeline(
        flight_90,
        x_start="start_time",
        x_end="end_time",
        color="rank",
        y="flight_date",
        hover_data=["tooltip"],
       
    )
    fig_90.update_yaxes(autorange="reversed")

    # 180-Minute Timeline
    fig_180 = px.timeline(
        flight_180,
        x_start="start_time",
        x_end="end_time",
        color="rank",
        y="flight_date",
        hover_data=["tooltip"]
    )
    fig_180.update_yaxes(autorange="reversed")

    return fig_90, fig_180