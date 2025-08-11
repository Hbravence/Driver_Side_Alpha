from dash import dcc, html
from utils.style_config import SUBLABEL_STYLE, DATA_LABEL_STYLE, DATA_LABEL_STYLE_2

def flight_filters(df_flights):
    return html.Div([
        html.Label("Select IATA Code", style=SUBLABEL_STYLE),
        dcc.Dropdown(
            id='iata-dropdown',
            options=[
                {'label': code, 'value': code} for code in sorted(df_flights['arrival_iataCode'].dropna().unique())
            ],
            placeholder='Select IATA code',
            clearable=True,
            searchable=True,
            style=DATA_LABEL_STYLE
            
        )
    ])

def event_filters(df_events):
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    available_days = df_events['Day of the week'].dropna().unique()

    # Preserve order but only include days present in the data
    ordered_days = [day for day in weekday_order if day in available_days]

    return html.Div([
        html.Label("Select Day of Week",style=SUBLABEL_STYLE),
        dcc.RadioItems(
            id='date-picker',
            options=[{'label': day, 'value': day} for day in ordered_days],
            value=ordered_days[0],
            inline=True,
            style=DATA_LABEL_STYLE,
            labelStyle=DATA_LABEL_STYLE_2

        )
    ])
