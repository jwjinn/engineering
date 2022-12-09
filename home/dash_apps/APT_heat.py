from urllib.request import urlopen
from dash import Dash, html, dcc
import json
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from django_plotly_dash import DjangoDash
from home.models import *
from config import mapbox


token = mapbox['key']
with urlopen('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo.json') as response:
    gu = json.load(response)
for x in gu['features']:
    x['id'] = x['properties']['name']

app = DjangoDash('APT_heatmap')

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df =RealEstate.objects.all().values()
df = pd.DataFrame(df)


gugun = df['gugun_id'].unique()
mean_price = []

for i in gugun:
    mean_price.append(df[df['gugun_id'] == i]["price"].mean())

df_s = pd.DataFrame({'gugun':gugun,'avg_price':mean_price})

fig = go.Figure()

fig.add_trace(go.Choroplethmapbox(
    geojson=gu,
    locations=df_s.gugun,
    z = df_s.avg_price,
    colorscale="redor"))

fig.update_layout(mapbox1=dict(style="carto-positron",
                  zoom=9.5, center = {"lat": 37.5453029, "lon": 126.9894348}, accesstoken = token),
                  )

fig.update_layout(coloraxis_showscale=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


app.layout = html.Div(
    # style={"background-color":"red", "overflow": "auto"},
    children=[
    dcc.Graph(
        id='example-graph',
        figure=fig,
        style={'width': '100%', 'height' : '410px','text-align':'center'},
    )
])

