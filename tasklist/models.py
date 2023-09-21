import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    img = models.ImageField(upload_to="images", blank=True)



# @receiver(post_delete, sender=Tasks)
# def delete_task_image(sender, instance, **kwargs):
#     if instance.img:
#         if os.path.isfile(instance.img.path):
#             os.remove(instance.img.path)
