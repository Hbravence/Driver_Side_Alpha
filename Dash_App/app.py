# app.py
from dash import Dash, dcc, html, Input, Output
from cities import la_layout

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/la':
        return la_layout()
   
    else:
        return html.H1("404 – City Not Found")

if __name__ == "__main__":
    app.run(debug=True)