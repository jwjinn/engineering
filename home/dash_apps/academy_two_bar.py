import dash
import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go
from django_plotly_dash import DjangoDash
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineering.settings")
django.setup()
from home.models import Academy

app = DjangoDash("academy_two_bar")


# df
academy = Academy.objects.all().values()
df = pd.DataFrame(academy)
n = df[df['academy_name'].str.contains('학고재독서실')].index
# 학고재 독서실 교습시간 99999999라서 제외
df.drop(n, inplace=True)
df = df[['gugun_id', 'lesson_hours', 'lesson_fee']]
df = df.groupby('gugun_id').mean().reset_index()
df = pd.DataFrame(df)

df['lesson_hours'] = round((df['lesson_hours']/60), 0)
df['lesson_fee'] = round((df['lesson_fee']/10000),0)


# # figure
gugun = list(df['gugun_id'].values)
hours = list(df['lesson_hours'].values)
fees = list(df['lesson_fee'].values)

fig = go.Figure(data=[
    go.Bar(name='월 평균교습시간', x=gugun, y=hours),
    go.Bar(name='월 평균교습비(만원)', x=gugun, y=fees)
])
fig.update_layout(barmode='group', title_text="서울시 사설학원 평균교습시간(월) & 평균교습비용(월)", title_x=0.5)


# html
app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig)
    ], style={'border' : '2px solid lightgray', 'border-radius' : '20px'})
