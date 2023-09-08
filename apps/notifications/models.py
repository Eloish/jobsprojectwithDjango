from django.db import models

from django.contrib.auth.models import User

class Notificaton(models.Model):
    MESSAGE='message'
    APPLICATION='application'

    CHOICES=(
        (MESSAGE,'message'),
        (APPLICATION,'application')
    )
    to_user=models.ForeignKey(User,related_name="notifications",on_delete=models.CASCADE)
    Notificaton_type=models.TextField(max_length=28,choices=CHOICES)
    is_read=models.BooleanField(default=False)
    extra_id=models.IntegerField(null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name="creatednotifications",on_delete=models.CASCADE)
    
    class Meta:
        ordering=['-created_at']


# Create your models here.
