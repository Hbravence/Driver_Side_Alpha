
from dash import html,dcc, Input, Output, callback
from components.flight_timelines import generate_flight_timelines
from components.event_maps import render_cluster_map, render_event_table
from utils.Data_loader import load_latest_csv
from components.ui_filters import flight_filters, event_filters
from utils.style_config import (HEADER_STYLE, GRAPH_STYLE, TABLE_CONTAINER_STYLE,PAGE_STYLE,GRAPH_CONTAINER_STYLE,MAP_STYLE, LABEL_STYLE,SUBLABEL_STYLE,Active_LABEL_STYLE)
import pandas as pd



def get_layout():
    df_events = load_latest_csv(city="LA", data_type="events", pattern="event_clustering*.parquet")
    df_flights = load_latest_csv(city="LA", data_type="flights", pattern="Top_clusters*.parquet")
    fig_90, fig_180 = generate_flight_timelines(df_flights)
    map_fig = render_cluster_map(df_events)

    return html.Div([
        html.H2("Los Angeles Demand Predictions", style=HEADER_STYLE),
        dcc.Store(id='flight-data', data=df_flights.to_dict('records')),
        dcc.Store(id='event-data', data=df_events.to_dict('records')),
        dcc.Tabs(id='tabs', value='tab-1', children=[
            dcc.Tab(label="Flight Timelines", value='tab-1', style=LABEL_STYLE, selected_style=Active_LABEL_STYLE,
                    children=[
                flight_filters(df_flights),
                html.Div([
                    html.H3("📅 Flight Timeline (90-Minute Clusters)", style=SUBLABEL_STYLE),
                    dcc.Graph(id='flight-graph-90', style=GRAPH_STYLE)
                ], style=GRAPH_CONTAINER_STYLE),
                html.Div([
                    html.H3("📅 Flight Timeline (3-Hour Clusters)", style=SUBLABEL_STYLE),
                    dcc.Graph(id='flight-graph-180', style=GRAPH_STYLE)
                ], style=GRAPH_CONTAINER_STYLE),
            ]),
            dcc.Tab(label="Event Clusters", value='tab-2', style=LABEL_STYLE, selected_style=Active_LABEL_STYLE ,
                     children=[
                event_filters(df_events),
                html.Div([
                    html.H3("🗺️ Clustered Events Map", style=SUBLABEL_STYLE),
                    dcc.Graph(id="scatter_map", style=MAP_STYLE)
                ], style=GRAPH_CONTAINER_STYLE),
                html.Div([render_event_table(df_events)], style=TABLE_CONTAINER_STYLE)
            ])
        ])
    ], style=PAGE_STYLE)

@callback(
    Output("flight-graph-90", "figure"),
    Output("flight-graph-180", "figure"),
    Input("iata-dropdown", "value"),
    Input("flight-data", "data"),
    prevent_initial_call=False
)
def update_flight_graphs(selected_iata, stored_data):
    df_flights = pd.DataFrame(stored_data)

    if selected_iata:
        df_filtered = df_flights[df_flights['arrival_iataCode'] == selected_iata]
    else:
        df_filtered = df_flights

    fig_90, fig_180 = generate_flight_timelines(df_filtered)
    return fig_90, fig_180

@callback(
    Output("scatter_map", "figure"),
    Input("date-picker", "value"),  # assuming your filter uses this ID
    Input("event-data", "data"),
    prevent_initial_call=False
)
def update_event_map(selected_day, stored_event_data):
    df_events = pd.DataFrame(stored_event_data)

    if selected_day:
        df_filtered = df_events[df_events['Day of the week'] == selected_day]
    else:
        df_filtered = df_events

    return render_cluster_map(df_filtered)



