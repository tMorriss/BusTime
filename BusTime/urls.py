from django.urls import path
from BusTime import views

app_name = 'BusTime'
urlpatterns = [
    path('', views.index, name='index')
]