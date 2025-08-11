# components/maps.py
import pandas as pd
import plotly.express as px
from utils.style_config import LABEL_STYLE, CLUSTER_COLORS,SUBLABEL_STYLE
def render_cluster_map(
    df_events: pd.DataFrame,
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    cluster_col: str = "Cluster",
    zoom_default: int = 10,
    map_height: int = 600
):
    """
    Render a clustered event map with dynamic zoom.

    Args:
        df_events (pd.DataFrame): Event data with latitude, longitude, cluster, start_time
        lat_col (str): Latitude column name.
        lon_col (str): Longitude column name.
        cluster_col (str): Cluster ID column name.
        zoom_default (int): Default zoom level.
        map_height (int): Height of the map in pixels.

    Returns:
        plotly.graph_objects.Figure: Clustered event map.
    """
    df = df_events.copy()

    # Dynamic center
    center_lat = df[lat_col].mean()
    center_lon = df[lon_col].mean()

    # Tooltip
    hover_data = {
        'Start Time': True,
        cluster_col: True,
        'Day of the week': True
    }

    # Scatter map
    fig = px.scatter_mapbox(
        df,
        lat=lat_col,
        lon=lon_col,
        color=cluster_col,
        hover_data=hover_data,
        zoom=zoom_default,
        height=map_height,
        color_discrete_sequence=CLUSTER_COLORS
    )

    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_center={"lat": center_lat, "lon": center_lon},
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )
    fig.update_traces(marker=dict(size=12))

    return fig

# components/event_table.py
from dash import dash_table, html


def render_event_table(df_events):
    exclude_cols = ["id", "latitude", "longitude", "pacific_endtime", "lat_rad", "lon_rad"]
    display_cols = [col for col in df_events.columns if col not in exclude_cols]

    return html.Div([
        html.Label("Weekly Event Data", style=SUBLABEL_STYLE),
        dash_table.DataTable(
            id='event-table',
            columns=[{'name': col, 'id': col} for col in display_cols],
            data=df_events[display_cols].to_dict('records'),
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_cell={
                'textAlign': 'left',
                'fontFamily': 'Inter, sans-serif',
                'fontSize': '14px',
                'color': '#333333',
                'backgroundColor': '#FFFFFF',
                'padding': '8px',
            },
            style_header={
                'backgroundColor': '#F2F2F2',
                'fontWeight': 'bold',
                'color': '#000000',
                'borderBottom': '1px solid #CCCCCC',
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#FAFAFA'
                }
            ],
            sort_action='native',
            filter_action='native'
        )
    ])