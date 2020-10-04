from django.urls import path
from .views import home,tournamentResult,dashboard,pubgMainPage,singleMainTournament
urlpatterns = [
    path('',home,),
    path('pubg',pubgMainPage,name='pubg'),
    path('single',singleMainTournament,name='single'),
    path('tournamentresult/<str:pk>/',tournamentResult,name='tournament'),
    path('dashboard',dashboard,name='dashboard')
]