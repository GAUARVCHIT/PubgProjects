from django.urls import path
from .views import home,tournamentResult,dashboard,pubgMainPage,singleMainTournament,singleMatch
urlpatterns = [
    path('',home,),
    path('pubg',pubgMainPage,name='pubg'),
    path('singleTournament/<int:pk>',singleMainTournament,name='singleTournament'),
    path('singleMatch/<int:pk>',singleMatch,name='singleMatch'),
    path('tournamentresult/<str:pk>/',tournamentResult,name='tournament'),
    path('dashboard',dashboard,name='dashboard')
]