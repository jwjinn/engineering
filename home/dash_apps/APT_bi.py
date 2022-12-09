from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
from home.models import *


app = DjangoDash('APT_bi')

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
real_estate = RealEstate.objects.all().values()
real_estate = pd.DataFrame(real_estate)
seoul = SeoulInfo.objects.all().values()
seoul = pd.DataFrame(seoul)
school = School.objects.all().values()
school = pd.DataFrame(school)

gugun = real_estate['gugun_id'].unique()
mean_price = []
total_price = []
mean_area = []
total_area = []
pop = seoul['population']
gugun_area =seoul['area']
den = seoul['population_dentisy']
stu =[]
tea =[]

for i in gugun:
    mean_price.append(real_estate[real_estate['gugun_id'] == i]["price"].mean())

for i in gugun:
    total_price.append(real_estate[real_estate['gugun_id'] == i]["price"].sum())

for i in gugun:
    mean_area.append(real_estate[real_estate['gugun_id'] == i]["building_area"].mean())

for i in gugun:
    total_area.append(real_estate[real_estate['gugun_id'] == i]["building_area"].sum())

for i in gugun:
    stu.append(school[school['gugun_id'] == i]["students_number"].sum())

for i in gugun:
    tea.append(school[school['gugun_id'] == i]["teachers_number"].sum())


df_s = pd.DataFrame({'gugun':gugun,'avg_price':mean_price,'total_price':total_price,
                     'avg_area':mean_area,'total_area':total_area
                     ,'pop':pop,'gugun_area':gugun_area,'den':den
                     ,'stu':stu,'tea':tea
                     })

app.layout = html.Div(children=[
    dcc.RadioItems([
        {"label": "전체 가격", "value": 'total_price'},
        {"label": "전체 공간", "value": 'total_area'},
        {"label": "평균 공간", "value": 'avg_area'},
        {"label": "인구수", "value": 'pop'},
        {"label": "자치구별 면적", "value": 'gugun_area'},
        {"label": "인구 밀도", "value": 'den'},
        {"label": "학생수", "value": 'stu'},
        {"label": "교원수 ", "value": 'tea'},
    ],
        'avg_price',
        id='yaxis-type',
        inline=True),

    dcc.Graph(
        id='graph',
        style={'width': '', 'height' : '410px'}
        ),

])


@app.callback(
    Output('graph', 'figure'),
    Input('yaxis-type', 'value'),
)
def update_graph(yaxis_type):
    fig = fig = px.scatter(df_s, x='avg_price', y=yaxis_type, color='gugun', size='total_price')
    fig.update_layout(margin=dict(t=30, l=0, r=0, b=0))
    return fig



