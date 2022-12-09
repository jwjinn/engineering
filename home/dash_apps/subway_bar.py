import plotly.express as px
import pandas as pd
from dash import html, dcc
from django_plotly_dash import DjangoDash
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineering.settings")
django.setup()
from home.models import Subway

app = DjangoDash("subway_bar")


# df
subway = Subway.objects.all().values()
df = pd.DataFrame(subway)
df = df.groupby('gugun_id').size().to_frame(name='count').reset_index()
df = pd.DataFrame(df)


# figure
fig = px.bar(df, x='gugun_id', y='count', title="자치구별 버스정류장 수")


# html
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='bar_graph', figure=fig)
    ], style={'border':'2px solid lightgray', 'border-radius':'20px'})
])
