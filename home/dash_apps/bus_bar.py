import plotly.express as px
import pandas as pd
import dash
from dash import Dash, html, dcc, Output, Input
from django_plotly_dash import DjangoDash
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineering.settings")
django.setup()
from home.models import Bus


app = DjangoDash("bus_bar")


# df
bus = Bus.objects.all().values()
df = pd.DataFrame(bus)
df = df[['gugun_id', 'bus_station_id']]
df = df.groupby('gugun_id').count().reset_index()
df = pd.DataFrame(df)


# figure
fig = px.bar(df, x='gugun_id', y='bus_station_id').update_layout(xaxis_title='자치구', yaxis_title='버스정류장 수', title="자치구별 버스정류장 수").update_layout(title_x=0.5)


# html
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='bar_graph', figure=fig)
    ])
], style={'border':'2px solid lightgray', 'border-radius':'20px'})
