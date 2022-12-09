from django.urls import path
from . import views

from home.dash_apps import app1, app3, app4, app5, app6, app7

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