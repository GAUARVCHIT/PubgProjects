from django.db.models.signals import post_save
from .models import *

#         post_save.disconnect(customer_profile, sender=sender)
#         result=Results.objects.get(id=instance.id)
#         result.placement_point=20
#         result.save(update_fields=['placement_point'])
#         post_save.connect(customer_profile, sender=sender)

def save_favorite(sender, instance, **kwargs):
   result_filter=Results.objects.filter(id=instance.id)
   result_get=Results.objects.get(id=instance.id)
   position = result_get.position
   kills=result_get.kills

   
   for i in PointsTable.objects.all():
       if i.pointsTableType.id==result_get.points_table_type.id and i.rank==position :
           result_filter.update(placement_point=i.placement_point,kill_points=i.kill_points*kills,Total_points=i.placement_point+i.kill_points*kills)
           break 

post_save.connect(save_favorite, sender=Results)


def player_career(sender,instance,created,**kwargs):
   # player_result_update=PlayerResult.objects.filter(id=instance.id)
   # player_result_get=PlayerResult.objects.get(id=instance.id)

   # peoples_get_id=player_result_get.peoples.id
   # print(peoples_get_id)

   # peoples_result_filter=Peoples.objects.filter(id=peoples_get_id)
   # peoples_result_get=Peoples.objects.get(id=peoples_get_id)
   # peoples_result_filter.update(total_kills=player_result_get.kills+peoples_result_get.total_kills)
   
   if created:
         player_result_get=PlayerResult.objects.get(id=instance.id)

         peoples_get_id=player_result_get.peoples.id
         print(peoples_get_id)

         peoples_result_filter=Peoples.objects.filter(id=peoples_get_id)
         peoples_result_get=Peoples.objects.get(id=peoples_get_id)
         peoples_result_filter.update(total_kills=player_result_get.kills+peoples_result_get.total_kills)


post_save.connect(player_career,sender=PlayerResult)