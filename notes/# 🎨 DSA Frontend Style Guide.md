# 🎨 DSA Frontend Style Guide

## 🧭 Design Philosophy

- **Modularity**: Each visual element should be self-contained, toggleable, and narratively distinct.
- **Emotional Literacy**: Use color, spacing, and typography to signal pacing, intensity, and coherence.
- **Somatic Feedback**: Visuals should feel like biofeedback—calm when regulated, alert when dysregulated.

---

## 🌈 Color Palette

| Layer              | Color Use                  | Hex Code     | Emotional Cue         |
|-------------------|----------------------------|--------------|------------------------|
| Background         | Soft neutral               | `#F5F5F5`    | Spacious, non-reactive |
| Primary Accent     | Deep teal or indigo        | `#2C3E50`    | Grounded focus         |
| Cluster Highlight  | Gradient by density        | `#3498DB` → `#E74C3C` | Calm → Alert |
| Somatic Overlay    | Light green or amber       | `#27AE60`, `#F39C12` | Hydration, HR zones    |
| Error/Dysregulation| Muted red                  | `#C0392B`    | Alert without panic    |

Use gradients to signal transitions—e.g., hydration moving from optimal to depleted.

---

## 🔤 Typography

| Element         | Font Family     | Weight | Use Case               |
|----------------|------------------|--------|-------------------------|
| Headings       | `Montserrat` or `Raleway` | Bold   | Section titles, tabs     |
| Body Text      | `Open Sans` or `Roboto`   | Regular| Descriptions, tooltips   |
| Data Labels    | `Courier New` or `Inconsolata` | Mono   | Cluster IDs, timestamps  |

- Avoid serif fonts—they signal legacy, not modularity.
- Use letter spacing to signal breath and pacing.

---

## 📐 Spacing & Layout

- **Padding**: `20px` around modules to create emotional breathing room
- **Grid**: Use a **12-column layout** for responsiveness
- **Hierarchy**: Visual weight should follow emotional weight—summary stats are lighter, clustering visuals are heavier

---

## 🧩 Component Styling

### Tabs

```python
style={'backgroundColor': '#F5F5F5', 'fontWeight': 'bold', 'padding': '10px'}