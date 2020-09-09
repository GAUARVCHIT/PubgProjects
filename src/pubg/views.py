from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import localdate

# Create your views here.

def home(request):

    return render(request,'pubg/home.html')

def firstPage(request):
    results=Results.objects.filter( matches__id='15').order_by('-Total_points','-kill_points')
    map=Matches.objects.get(id='15').maps.name
    

    matchesPlayed=Matches.objects.filter(total_tournament__id='1')
    tournamentResults= Results.objects.filter(matches__id__in=matchesPlayed)
    quaryteams=TotalTournament.objects.get(id='1')
    teamsParticipating=quaryteams.teams.all()

    resultList=[]
    
    class Result:
        def __init__(self,teamname,totalkills,totalplacementpoint,totalPoints):
            self.teamname=teamname
            self.totalkills=totalkills
            self.totalplacementpoint=totalplacementpoint
            self.totalPoints=totalPoints

        def __gt__(self, other):
            return (self.totalPoints < other.totalPoints) or (self.totalkills < other.totalkills)

    for i in teamsParticipating:
        totalkills=0
        totalplacementpoint=0
        totalPoints=0
        print(i.name)
        for j in tournamentResults:
            if j.teams.id==i.id:
                totalkills+=j.kill_points
                totalplacementpoint+=j.placement_point
                totalPoints+=j.Total_points
        print(totalPoints)
        resultList.append(Result(i.name,totalkills,totalplacementpoint,totalPoints))
        
        resultList.sort()
    



    context={
        'matchResults': results,
        'map': map,
        'tournamentResults': tournamentResults,
        'teamsParticipating': teamsParticipating,
        'resultList': resultList,
    }
    
    return render(request,'pst/k.html',context)


def dashboard(request):
    # noOfTournaments = TotalTournament.objects.filter( pub_date__gte=datetime.now()-timedelta(days=7))   
    noOfTournaments = TotalTournament.objects.exclude(starting_date__gt=datetime.now()+timedelta(days=3)).filter(starting_date__gte=datetime.now()-timedelta(days=3))|TotalTournament.objects.exclude(endings_date__gt=datetime.now()+timedelta(days=3)).filter(endings_date__gte=datetime.now()-timedelta(days=3))
                                                                                                            ### number of tournament between starting and ending between 7 days
    
    for i in noOfTournaments:                                                                             ### printing
        print(i)

    # listOfMatches = Matches.objects.exclude(starting_time__gt=datetime.now().date()).filter(starting_time__gte=datetime.now()-timedelta(days=1))                 now
    listOfMatches=Matches.objects.filter(match_starting_time__date=datetime.now())

    context={
        'TournamentsIn7Days': noOfTournaments,
        'listOfMatches': listOfMatches,                                                                                                                          
    }


    return render(request,'pubg/dashboard.html',context)

def tournamentResult(request,pk):                                                                           ### result of a tournament
    tournament=TotalTournament.objects.get(id=pk)

    matchesPlayed=Matches.objects.filter(total_tournament__id=pk)
    tournamentResults= Results.objects.filter(matches__id__in=matchesPlayed)
    teamsParticipating=tournament.teams.all()
    resultList=[]
    
    class Result:                                                                       
        def __init__(self,teamname,totalkills,totalplacementpoint,totalPoints):
            self.teamname=teamname
            self.totalkills=totalkills
            self.totalplacementpoint=totalplacementpoint
            self.totalPoints=totalPoints

        def __gt__(self, other):
            return (self.totalPoints < other.totalPoints) or (self.totalkills < other.totalkills)

    for i in teamsParticipating:                                                                           ### ranking implementation
        totalkills=0
        totalplacementpoint=0
        totalPoints=0
        print(i.name)
        for j in tournamentResults:
            if j.teams.id==i.id:
                totalkills+=j.kill_points
                totalplacementpoint+=j.placement_point
                totalPoints+=j.Total_points
        print(totalPoints)
        resultList.append(Result(i.name,totalkills,totalplacementpoint,totalPoints))
        
        resultList.sort()

    context={
        'tournament': tournament,
        'resultList': resultList,
        # 'matchPlayed': matchesPlayed,
    }
    return render(request,'pubg/tournament.html',context)

def matchResult(request,pk):
    results=Results.objects.filter( matches__id=pk).order_by('-Total_points','-kill_points')
    map=Matches.objects.get(id='pk').maps.name
    context={
        'matchResults': results,
        'map': map,
    }
    
    return render(request,'pst/match.html',context)