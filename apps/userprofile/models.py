from django.db import models
from django.contrib.auth.models import User

from apps.jobs.models import application 

# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User,related_name='userprofile',on_delete=models.CASCADE)
    is_employer=models.BooleanField(default=False)

User.Userprofile=property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class conversationMessage(models.Model):
    application=models.ForeignKey(application,related_name='conversationmessage',on_delete=models.CASCADE)
    content=models.TextField()
    create_by=models.ForeignKey(User,related_name="conversationmessage",on_delete=models.CASCADE)

    created_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['created_at']


