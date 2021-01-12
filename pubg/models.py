from django.db import models
from django.utils import timezone
# Create your models here.
class Seasons(models.Model):
    name=models.CharField(max_length=50,null=True)
    starting_date=models.DateField(auto_now_add=False,null=True)
    ending_date=models.DateField(auto_now_add=False,null=True)
    description=models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Seasons"

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name=models.CharField(max_length=50,null=True)
    logo=models.ImageField(null=True,blank=True,upload_to='sponsor_logo')
    website_link=models.URLField(max_length=200,blank=True,null=True)

    class Meta:
        verbose_name_plural = "Sponsor"

    def __str__(self):
        return self.name

class Organizations(models.Model):
    name=models.CharField(max_length=50,null=True)
    ceo=models.CharField(max_length=50,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    headquator_address=models.CharField(max_length=120,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    logo=models.ImageField(null=True,blank=True,upload_to='organizations_logo')
    sponsor=models.ManyToManyField(Sponsor,blank=True)
    website_link=models.URLField(max_length=200,blank=True,null=True)
    fb_link=models.URLField(max_length=200,blank=True,null=True)
    instagram_link=models.URLField(max_length=200,blank=True,null=True)
    yt_link=models.URLField(max_length=200,blank=True,null=True)
    twitter_link=models.URLField(max_length=200,blank=True,null=True)
    class Meta:
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name

class Teams(models.Model):
    name=models.CharField(max_length=50,null=True)
    short_name=models.CharField(max_length=10,null=True,blank=True)
    description=models.TextField(max_length=200,null=True,blank=True)
    organizations=models.ManyToManyField(Organizations,related_name='organizations_backing_teams',blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    logo=models.ImageField(null=True,blank=True,upload_to='teams_logo')
    sponsor=models.ManyToManyField(Sponsor,blank=True)
    website_link=models.URLField(max_length=200,blank=True,null=True)
    fb_link=models.URLField(max_length=200,blank=True,null=True)
    instagram_link=models.URLField(max_length=200,blank=True,null=True)
    yt_link=models.URLField(max_length=200,blank=True,null=True)
    twitter_link=models.URLField(max_length=200,blank=True,null=True)

    class Meta:
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.short_name

class RolesInCommunity(models.Model):
    role=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "RolesInCommunity"

    def __str__(self):
        return self.role

class Peoples(models.Model):
    GENDER = ( 
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name=models.CharField(max_length=50,null=True,blank=True)
    ingame_name=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=20,null=True,choices=GENDER)
    pubg_id=models.CharField(max_length=30,null=True,blank=True)
    team=models.ForeignKey(Teams,null=True, on_delete=models.SET_NULL)
    rolesInCommunity=models.ManyToManyField(RolesInCommunity, related_name='peoples_roles_in_Community')
    mobile_no=models.PositiveIntegerField(blank=True,null=True)
    address=models.CharField(max_length=200,blank=True,null=True)
    total_matches_played=models.PositiveIntegerField(null=True,blank=True,default=0)
    total_kills=models.PositiveIntegerField(null=True,blank=True,default=0)
    total_knockout=models.PositiveIntegerField(null=True,blank=True,default=0)
    total_damage=models.PositiveIntegerField( null=True,blank=True,default=0)

    fb_link=models.URLField(max_length=200,blank=True,null=True)
    instagram_link=models.URLField(max_length=200,blank=True,null=True)
    yt_link=models.URLField(max_length=200,blank=True,null=True)
    twitter_link=models.URLField(max_length=200,blank=True,null=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Peoples"

    def __str__(self):
        return self.ingame_name

class PeoplesHistory(models.Model):
    STATUS = ( 
        ('Active Squad', 'Active Squad'),
        ('Former Players', 'Former Players'),
        ('Temporary stand-ins','Temporary stand-ins'),
    )
    team=models.ForeignKey(Teams,blank=True,null=True,on_delete=models.SET_NULL)
    people=models.ForeignKey(Peoples,blank=True,null=True,on_delete=models.SET_NULL)
    date=models.DateField(auto_now_add=False,null=True,blank=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

    class Meta:
        verbose_name_plural = "PeoplesHistory"

    def __str__(self):
        return self.people + self.status

class TournamentTags(models.Model):
    tags=models.CharField(max_length=100,blank=False,null=True)

    class Meta:
        verbose_name_plural = "TournamentTags"

    def __str__(self):
        return self.tags


class TotalTournament(models.Model):

    priorityLevel = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    season= models.ForeignKey(Seasons,null=True, on_delete=models.SET_NULL)
    name=models.CharField(max_length=100,null=True)
    short_name=models.CharField(max_length=20,null=True,blank=True)
    teams= models.ManyToManyField(Teams,related_name='teams_participating_in_tournaments')
    description=models.TextField(blank=True,null=True)
    starting_date=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    endings_date=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    subtournament=models.OneToOneField('self',blank=True,null=True,on_delete=models.SET_NULL)
    tags=models.ManyToManyField(TournamentTags,blank=True)
    prize_pool=models.PositiveIntegerField(null=True,blank=True,default=0)
    priorites=models.CharField(null=True,blank=False,choices=priorityLevel,max_length=4)

    class Meta:
        verbose_name_plural = "TotalTournament"

    def __str__(self):
        return self.short_name

    @property
    def upcomingTournament(self):
        return self.starting_date > timezone.now()

    @property
    def ongoingTournament(self):
        return self.starting_date <= timezone.now() and self.endings_date >= timezone.now()

    @property
    def endedTournament(self):
        return self.endings_date < timezone.now()

class Prize(models.Model):
    tournament=models.ForeignKey(TotalTournament,null=True,on_delete=models.CASCADE)
    position=models.PositiveIntegerField(null=True)
    money=models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural="Prize"

    def __str__(self):
        return self.tournament+"  Position->  "+ str(self.position)

class Awards(models.Model):
    tournament=models.ForeignKey(TotalTournament,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=200,null=True,blank=True)
    award_money=models.PositiveIntegerField(null=True)
    side_benfits=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural="Awards"

    def __str__(self):
        return self.tournament+" Title->  "+ self.title

class TournamentGroup(models.Model):
    tournament=models.ForeignKey(TotalTournament,null=True,on_delete=models.SET_NULL)
    group_name=models.CharField(max_length=50,null=True)
    teams_in_group=models.ManyToManyField(Teams)

    class Meta:
        verbose_name_plural="TournamentGroup"
    
    def __str__(self):
        return self.tournament+" group-> "+ self.group_name

##############################################################

class Maps(models.Model):
    name=models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name_plural = "Maps"

    def __str__(self):
        return self.name

class PointsTableType(models.Model):
    type=models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name_plural = "PointsTableType"

    def __str__(self):
        return self.type

class PointsTable(models.Model):
    pointsTableType=models.ForeignKey(PointsTableType,null=True,on_delete=models.SET_NULL)
    rank=models.PositiveIntegerField(null=True)
    placement_point=models.PositiveIntegerField(null=True)
    kill_points=models.PositiveIntegerField(null=True,default=1)

    class Meta:
        verbose_name_plural = "PointsTable"

    def __str__(self):
        return "Position-> "+str(self.rank)+", "+"Points Table Type-> "+self.pointsTableType.type

class Matches(models.Model):

    match_no = ( 
        ('Match 1', 'Match 1'),
        ('Match 2', 'Match 2'),
        ('Match 3', 'Match 3'),
        ('Match 4', 'Match 4'),
        ('Match 5', 'Match 5'),
        ('Match 6', 'Match 6'),
    )

    DAY_NO = (
        ('Day 1', 'Day 1'),
        ('Day 2', 'Day 2'),
        ('Day 3', 'Day 3'),
        ('Day 4', 'Day 4'),
        ('Day 5', 'Day 5'),
    )

    days=models.CharField(null=True,blank=True,max_length=20,choices=DAY_NO)
    teams=models.ManyToManyField(Teams)
    match_starting_time=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    maps=models.ForeignKey(Maps,null=True,on_delete=models.SET_NULL)
    total_tournament=models.ForeignKey(TotalTournament,null=True,on_delete=models.SET_NULL)
    tournament_match_no=models.CharField(max_length=10,null=True,blank=True,choices=match_no)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return "Tournament -> "+self.total_tournament.short_name+", "+"Starting Time-> "+ str(self.match_starting_time)+", "+"Maps -> "+self.maps.name

class Results(models.Model):
    teams=models.ForeignKey(Teams,null=True,on_delete=models.SET_NULL)
    points_table_type=models.ForeignKey(PointsTableType,null=True,on_delete=models.SET_NULL)
    position= models.PositiveIntegerField(blank=True,null=True)
    kills=models.PositiveIntegerField(blank=True,null=True)
    matches=models.ForeignKey(Matches,null=True,on_delete=models.CASCADE)
    placement_point=models.PositiveIntegerField(null=True,default=0)
    kill_points=models.PositiveIntegerField(null=True,default=0)
    Total_points=models.PositiveIntegerField(null=True,default=0)
    class Meta:
        verbose_name_plural = "Results"

    def __str__(self):
        return "Match Id-> "+str(self.matches.id)+", "+ "Team-> "+str(self.teams.name)

class PlayerResult(models.Model):
    teams=models.ForeignKey(Teams,null=True,on_delete=models.CASCADE)
    peoples=models.ForeignKey(Peoples,null=True,on_delete=models.CASCADE)
    matches=models.ForeignKey(Matches,null=True,on_delete=models.CASCADE)
    kills=models.PositiveIntegerField(null=True,default=0)
    damageDealt=models.PositiveIntegerField(null=True,default=0)
    knockout=models.PositiveIntegerField(null=True,default=0)

    class Meta:
        verbose_name_plural = "PlayerResult"

    def __str__(self):
        return "Match Id-> "+str(self.matches.id)+", "+self.peoples.ingame_name

##############################################################
############################################################