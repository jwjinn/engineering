import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engineering.settings")
django.setup()

from home.models import Academy

app = DjangoDash("academy_heatmap")


# df
academy = Academy.objects.all().values()
df = pd.DataFrame(academy)
df = df[['gugun_id', 'lesson_category', 'lesson_fee']]
df = df.groupby(['gugun_id', 'lesson_category']).mean().reset_index()
df = pd.DataFrame(df)
df['lesson_fee'] = df['lesson_fee']/10000
df['lesson_fee'] = df['lesson_fee'].round(0)
df = df.pivot(index='lesson_category', columns='gugun_id', values='lesson_fee')
df = df.fillna(29) # 널값을 교습비의 평균값으로 채워줌.





seoul_area = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구',
                 '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구',
                 '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구',
                 '양천구', '영등포구', '용산구', '은평구', '종로구', '중구','중랑구'] # 서울 자치구 리스트


# html
app.layout = html.Div([
    html.Div([dcc.Graph(id="graph")]),
    html.Div([html.P("자치구별로 확인하기👇"),
    dcc.Checklist(
        id='gugun',
        options=seoul_area,
        value=seoul_area)
    ])
], style={'border' : '2px solid lightgrey', 'border-radius' : '20px', 'width' : '98%', 'height' : '600px'})


# figure
@app.callback(
    Output("graph", "figure"),
    Input("gugun", "value"))
def filter_heatmap(cols, **kwargs):
    fig = px.imshow(df[cols], labels=dict(x='자치구', y='학습분류'), title="자치구별 & 학원 교습분류별 한달 평균 교습비(만원)").update_layout(title_x=0.5)
    return fig
