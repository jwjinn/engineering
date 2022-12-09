from django.urls import path
from . import views

from home.dash_apps import app1, app3, SchoolMap, SchoolNum,StudentTeacherClass, SchoolHeatMap, APT_heat,APT_meme,APT_bi,edu_bar,edu_pie,edu_sca, academy_treemap_bar, academy_heatmap, academy_two_bar, bus_scatter_map, bus_bar, bus_choropleth_map, subway_bar, subway_map

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


    # 추후 삭제할 것.
    # ajax map praictice
    path('mapractice/', views.mapractice, name = 'mapractice'),
    path('mapractice/geoInfo', views.geoInfo, name = 'geoInfo'),

    # ajax priactice
    path('ajax/', views.ajax, name = 'ajax'),
    path('ajax/show_eng', views.show_eng, name ='show_eng'),
]