from django.urls import path
from .views import home,tournamentResult,dashboard
urlpatterns = [
    path('',home,),
    path('tournamentresult/<str:pk>/',tournamentResult,name='tournament'),
    path('dashboard',dashboard,name='dashboard')
]