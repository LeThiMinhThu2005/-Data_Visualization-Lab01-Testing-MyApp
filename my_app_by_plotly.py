from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Dữ liệu mẫu
df = pd.DataFrame({
    "Hãng": ["Hãng A", "Hãng B", "Hãng C", "Hãng A", "Hãng B", "Hãng C"],
    "Lượt bán": [4, 1, 2, 2, 4, 5],
    "Loại": ["Kem dưỡng", "Kem dưỡng", "Kem dưỡng", "Serum", "Serum", "Serum"]
})

fig = px.barmode="group"
fig = px.bar(df, x="Loại", y="Lượt bán", color="Hãng", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Dashboard Thị phần Mỹ phẩm'),
    dcc.Graph(id='example-graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
