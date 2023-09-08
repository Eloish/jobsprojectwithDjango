from django.shortcuts import render,redirect

from .models import Notificaton
from django.contrib.auth.decorators import login_required
# Create your views here.

def notifications(request):
    goto=request.GET.get('goto','')
    notification_id=request.GET.get('notification',0)
    extra_id=request.GET.get('extra_id',0)

    if goto !='':
        notification=Notificaton.objects.get(pk=notification_id)
        notification.is_read=True
        notification.save()

        if notification.Notificaton_type==Notificaton.MESSAGE:
            return redirect('viewapplication',application_id= notification.extra_id)
        elif notification.Notificaton_type==Notificaton.APPLICATION:
            return redirect('viewapplication',application_id= notification.extra_id)
        
    return render(request ,'notification.html')
             


     

