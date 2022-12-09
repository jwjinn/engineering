from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
from home.models import *

app = DjangoDash('APT')

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df =RealEstate.objects.all().values()
df = pd.DataFrame(df)



gugun = df['gugun_id'].unique()
mean_price = []
total_price = []
mean_area = []
total_area = []

for i in gugun:
    mean_price.append(df[df['gugun_id'] == i]["price"].mean())

for i in gugun:
    total_price.append(df[df['gugun_id'] == i]["price"].sum())

for i in gugun:
    mean_area.append(df[df['gugun_id'] == i]["building_area"].mean())

for i in gugun:
    total_area.append(df[df['gugun_id'] == i]["building_area"].sum())


df_s = pd.DataFrame({'gugun':gugun,'avg_price':mean_price,'total_price':total_price,'avg_area':mean_area,'total_area':total_area})



app.layout = html.Div([

    dcc.Tabs(id='yaxis-type',value='total_price',
             children=[
                dcc.Tab(label= "전체 가격", value= 'total_price'),
                dcc.Tab(label= "평균 가격", value= 'avg_price'),
                dcc.Tab(label= "전체 공간", value= 'total_area'),
                dcc.Tab(label= "평균 공간", value= 'avg_area')],

    ),
    dcc.Graph(
        id='graph',
        style={'height' : '370px'}
        )]
)

@app.callback(
    Output('graph', 'figure'),
    Input('yaxis-type', 'value'),
)
def update_graph(yaxis_type):

    fig = px.bar(df_s, x="gugun",
                y=yaxis_type,
                color='gugun')
    fig.update_layout(margin=dict(t=30, l=0, r=0, b=0))
    return fig



