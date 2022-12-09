import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
from dash import html, dcc
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineering.settings")
django.setup()
from home.models import Academy

app = DjangoDash("academy_treemap_bar")

academy = Academy.objects.all().values()
df01 = pd.DataFrame(academy)
df01 = df01[['gugun_id', 'lesson_category', 'academy_name']]
df01 = df01.groupby(['gugun_id', 'lesson_category']).size().to_frame(name='count').reset_index()
df01 = pd.DataFrame(df01)

df02 = pd.DataFrame(academy)
df02 = df02.groupby('lesson_category').size().to_frame(name='count').reset_index()
df02 = pd.DataFrame(df02)


# figure
fig = px.treemap(df01, path=[px.Constant('서울특별시'), 'gugun_id', 'lesson_category'],values='count', title='자치구별 학원수 & 교습분류별 학원수', height=750)
fig.update_traces(root_color='lightgrey')
fig.update_layout(margin = dict(t=50, l=25, b=25))

fig02 = px.bar(df02, x = 'count', y = 'lesson_category', orientation='h', height=800).update_layout(xaxis_title=None, yaxis_title=None)
fig02.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})


# html
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='academy_bar', figure=fig02)
    ],style={'width' : '40%', 'height' : '800px'}
    ),
    html.Div([
        dcc.Graph(id='academy_graphic', figure=fig)
    ], style={'width' : '58%', 'height': '800px'})
], style={'display' : 'flex', 'width' : '98%', 'border':'2px solid lightgrey', 'border-radius':'20px'})
