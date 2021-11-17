from django.urls import path

from . import views

urlpatterns = [
    path('salelistings/<str:city>/<str:state>/', views.getSaleListings, name='getSaleListings'),
    path('nearbystations/<str:lat>/<str:long>/', views.getNearestTrainStations, name='getNearestTrainStations'),
]