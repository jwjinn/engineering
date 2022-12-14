from django.urls import path
from . import views

from home.dash_apps import APT_heat,APT_meme,APT_bi,edu_bar,edu_pie,edu_sca
from home.dash_apps import SchoolMap, SchoolNum, StudentTeacherClass, SchoolHeatMap
from home.dash_apps import academy_heatmap, academy_treemap_bar, academy_two_bar
from home.dash_apps import bus_bar, bus_choropleth_map, bus_scatter_map
from home.dash_apps import subway_bar, subway_map

urlpatterns = [
    path('', views.index, name = 'index'),

    path('academy/', views.academy, name = 'academy'),
    path('bus/', views.bus, name='bus'),
    path('education_budget/', views.education_budget, name='education_budget'),
    path('real_estate/', views.real_estate, name='real_estate'),
    path('school/', views.school, name='school'),
    path('subway/', views.subway, name='subway'),
    path('map/', views.map, name = 'map'),
    path('map/geoInfo', views.geoInfo, name = 'geoInfo'),

    path('projectPlan/', views.projectPlan, name = 'projectPlan'),

    #notion_wireFrmae
    path('projectPlan/subwayBusPrivate/', views.subwaybusprivate, name = 'subwayBusPrivate'),
    path('projectPlan/jeong/', views.jeong, name = 'jeong'),
    path('projectPlan/lee/', views.lee, name = 'lee'),

    # ERD
    path('erd/', views.erd, name = 'erd'),

    # DataDefinition
    path('dataDefinition/', views.dataDefinition, name = 'dataDefinition'),

    #tableDefinition
    path('tableDefinition/', views.tableDefinition, name = 'tableDefinition'),

    #architecture
    path('architecture/', views.architecture, name = 'architecture'),



    # 추후 삭제할 것.
    # ajax map praictice
    path('mapractice/geoInfo', views.geoInfo, name = 'geoInfo'),

    # ajax priactice
    path('ajax/', views.ajax, name = 'ajax'),
    path('ajax/show_eng', views.show_eng, name ='show_eng'),
]