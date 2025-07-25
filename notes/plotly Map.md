Here’s your architecture summary saved as a Markdown file, ready for documentation or version control:

<AttachedFile name="DSA_Hybrid_Dashboard_Architecture.md" content="# 🧠 DSA Hybrid Dashboard Architecture (City-Specific Access)

## 🧱 Core Principles

- Single Dash App hosted on EC2  
- Modular city components for layout, logic, and data  
- Scoped data access—each city only sees its own data  
- No cross-city visibility unless explicitly allowed  
- Future-proof for authentication, routing, and scaling  

---

## 📁 Folder Structure

```
dsa_dash_app/
├── app.py                      # Main Dash app
├── data_loader.py              # Abstracted data access
├── /components/
│   ├── /cities/
│   │   ├── nyc.py              # NYC-specific layout + logic
│   │   └── chicago.py
│   └── /shared/
│       └── header.py           # Shared UI components
├── /assets/                    # Optional styling
└── /data/
    ├── nyc.csv
    └── chicago.csv
```

---

## 🧩 Key Logic

### `app.py`

- Dropdown or URL param selects city  
- Dynamically loads that city’s layout  
- Only that city’s data is loaded and rendered  

### `data_loader.py`

```python
def load_data(city):
    return pd.read_csv(f\"data/{city}.csv\")
```

### `components/cities/nyc.py`

```python
def layout():
    df = load_data(\"nyc\")
    fig = px.bar(df, x=\"category\", y=\"value\")
    return html.Div([dcc.Graph(figure=fig)])
```

---

## 🛡️ Security & Isolation

- Each city module is self-contained  
- No shared state or data unless explicitly passed  
- Easy to enforce access control later (auth, tokens, IAM)  

---

## 🚀 Deployment Strategy

- Package and deploy on a single EC2 instance  
- Use Gunicorn + Nginx for production  
- Open port 80 or 8050 for access  
- Optional: use subdomains or URL routing for city-specific access  

---

## 🔮 Future Enhancements

| Feature | Benefit |
|---------|---------|
| **URL routing** (`/nyc`, `/chicago`) | Cleaner UX, easier to secure |
| **User authentication** | Restrict access per city |
| **Athena integration** | Replace CSVs with scalable, cloud-native queries |
| **Subdomain routing** | `nyc.dsa.io` → loads NYC module only |
| **Multi-tenant IAM** | Enforce data access at the cloud level |
"/>
