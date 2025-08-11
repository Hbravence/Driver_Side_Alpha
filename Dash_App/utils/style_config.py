# style_config.py

# 🌑 Base Colors
COLORS = {
    'background': '#121212',
    'text': '#E0E0E0',
    'accent': '#00C9A7',
    'danger': '#FF6B6B',
    'card': '#1E1E1E',
    'border': '#333333'
}
CLUSTER_COLORS = [
    '#00C9A7',  # accent
    '#FF6B6B',  # danger
   
    '#1982C4',  # sky
    '#A0E7E5',  # mint
    '#FFB5B5'   # rose
]



# 🧠 Typography
HEADER_STYLE = {
    'fontFamily': 'Raleway, sans-serif',
    'fontWeight': '600',
    'fontSize': '28px',
    'color': COLORS['accent'],
    'textAlign': 'center',
    'marginBottom': '20px'
}

# 📊 Graph Containers
GRAPH_CONTAINER_STYLE = {
    'padding': '20px',
    'backgroundColor': COLORS['card'],
    'borderRadius': '10px',
    'boxShadow': '0 2px 8px rgba(0,0,0,0.3)',
    'marginBottom': '20px'
}

GRAPH_STYLE = {
    'height': '400px',
    'width': '100%',
    'backgroundColor': COLORS['card']
}

MAP_STYLE = {
    'height': '500px',
    'width': '100%',
    'backgroundColor': COLORS['card']
}

# 📋 Table Styling
TABLE_CONTAINER_STYLE = {
    'padding': '20px',
    'backgroundColor': COLORS['border'],
    'borderRadius': '10px',
    'overflowX': 'auto',
    'maxHeight': '400px',
    'border': f'1px solid {COLORS["border"]}',
    'color': COLORS['text']
}

# 🧱 Page Background
PAGE_STYLE = {
    'backgroundColor': COLORS['background'],
    'color': COLORS['text'],
    'padding': '40px'
}
# style_config.py

# Fonts
TITLE_FONT = "Raleway, sans-serif"
BODY_FONT = "Inter, sans-serif"
DATA_FONT = "Roboto Mono, monospace"

# Font weights
FONT_WEIGHT_BOLD = 600
FONT_WEIGHT_MEDIUM = 500
FONT_WEIGHT_REGULAR = 400

# Font sizes
FONT_SIZE_TITLE = "28px"
FONT_SIZE_SUBTITLE = "22px"
FONT_SIZE_BODY = "16px"
FONT_SIZE_DATA = "14px"

# Label styles
LABEL_STYLE = {
    'fontFamily': TITLE_FONT,
    'fontWeight': FONT_WEIGHT_BOLD,
    'fontSize': FONT_SIZE_TITLE,
    'color': COLORS['accent'],
    'textAlign': 'center',
    'marginBottom': '20px'
}

SUBLABEL_STYLE = {
    'fontFamily': TITLE_FONT,
    'fontWeight': FONT_WEIGHT_MEDIUM,
    'fontSize': FONT_SIZE_SUBTITLE,
    'color': COLORS['accent'],
    'textAlign': 'Left',
    'marginBottom': '12px'
}

DATA_LABEL_STYLE = {
    'fontFamily': DATA_FONT,
    'fontWeight': FONT_WEIGHT_REGULAR,
    'fontSize': FONT_SIZE_DATA,
    'color': '#333333',
    'textAlign': 'left'
}

Active_LABEL_STYLE = {
    'fontFamily': BODY_FONT,
    'fontWeight': FONT_WEIGHT_BOLD,
    'fontSize': FONT_SIZE_TITLE,
    'color': COLORS['danger'],
    'textAlign': 'center',
    'marginBottom': '20px'
}

DATA_LABEL_STYLE_2 = {
    'fontFamily': DATA_FONT,
    'fontWeight': FONT_WEIGHT_REGULAR,
    'fontSize': FONT_SIZE_DATA,
    'color': COLORS['text'],
    'textAlign': 'left'
}