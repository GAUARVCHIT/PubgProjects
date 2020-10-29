from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import localdate
from django.db.models import Q

# Create your views here.

def home(request):
    todayDate= timezone.now()
    noOfTournaments = TotalTournament.objects.exclude(starting_date__gt=todayDate+timedelta(days=3)).filter(starting_date__gte=todayDate-timedelta(days=3)).filter(priorites='5')|TotalTournament.objects.exclude(endings_date__gt=todayDate+timedelta(days=3)).filter(endings_date__gte=todayDate-timedelta(days=3)).filter(priorites='5')
    print('Priorities', noOfTournaments)     
    
    context={
        'mostImpTournaments': noOfTournaments,
    }                                                                                                 ### number of tournament between starting and ending between 7 days

    return render(request,'pubg/home.html',context)

def pubgMainPage(request):
    # noOfTournaments = TotalTournament.objects.filter( pub_date__gte=datetime.now()-timedelta(days=7))   
    todayDate= timezone.now()
    after3Day=todayDate+timedelta(days=3)
    after2Day=todayDate+timedelta(days=2)
    after1Day=todayDate+timedelta(days=1)
    today0Day=todayDate+timedelta(days=0)
    before1Day=todayDate-timedelta(days=1)
    before2Day=todayDate-timedelta(days=2)
    before3Day=todayDate-timedelta(days=3)
    
    noOfTournaments = TotalTournament.objects.exclude(starting_date__gt=todayDate+timedelta(days=3)).filter(starting_date__gte=todayDate-timedelta(days=3))|TotalTournament.objects.exclude(endings_date__gt=todayDate+timedelta(days=3)).filter(endings_date__gte=todayDate-timedelta(days=3))
    noOfImpTournaments = noOfTournaments.filter(Q(priorites='5')|Q(priorites='4'))

    matchOn3afterDay = Matches.objects.filter(match_starting_time__date=after3Day)
    matchOn2afterDay = Matches.objects.filter(match_starting_time__date=after2Day)
    matchOn1afterDay = Matches.objects.filter(match_starting_time__date=after1Day)
    matchOnNow = Matches.objects.filter(match_starting_time__date=today0Day)
    matchOn1beforeDay = Matches.objects.filter(match_starting_time__date=before1Day)
    matchOn2beforeDay = Matches.objects.filter(match_starting_time__date=before2Day)
    matchOn3beforeDay = Matches.objects.filter(match_starting_time__date=before3Day)
    
    print('matchOnNow', matchOnNow.count())

    context={
        'ImpTournamentsIn7Days': noOfImpTournaments,
        'TournamentsIn7Days': noOfTournaments,
        'matchOn3afterDay': matchOn3afterDay,
        'matchOn2afterDay': matchOn2afterDay,
        'matchOn1afterDay': matchOn1afterDay,
        'matchOnNow': matchOnNow,
        'matchOn1beforeDay': matchOn1beforeDay,
        'matchOn2beforeDay': matchOn2beforeDay,
        'matchOn3beforeDay': matchOn3beforeDay,
        
        'after3Day': after3Day,
        'after2Day': after2Day,
        'after1Day': after1Day,
        'today0Day': today0Day,
        'before1Day': before1Day,
        'before2Day': before2Day,
        'before3Day': before3Day,
    }
    return render(request,'pubg/pubg.html',context)

def singleMainTournament(request,pk):
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


    context = {
        'tournament': tournament,
        'resultList': resultList,
        'matchesPlayed': matchesPlayed,
    }
    return render(request, 'pubg/singleTournament.html',context)

def singleMatch(request,pk):
    match=Matches.objects.get(id=pk)

    results=Results.objects.filter( matches__id=pk).order_by('-Total_points','-kill_points')
    map=match.maps.name
    context={
        'match': match,
        'matchResults': results,
        'map': map,
    }

    context = {
        'match': match,
    }
    return render(request, 'pubg/singleMatch.html',context)

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