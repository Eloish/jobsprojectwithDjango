from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from apps.jobs.models import application,job

from .models import conversationMessage
from apps.notifications.utilities import create_notification

# Create your views here.
@login_required
def dashboard(request):
    return render(request,'userprofile/dashboard.html',{'userprofile':request.user.Userprofile})

@login_required

def viewapplication(request,application_id):

    if request.user.userprofile.is_employer:
        applications=get_object_or_404(application, pk=application_id,job__createdby=request.user)
    else:
        applications=get_object_or_404(application, pk=application_id,createdby=request.user)

    if request.method=="POST":
        content=request.POST.get('content')
        if content:
            conversationmessage=conversationMessage.objects.create(application=applications,content=content,create_by=request.user) 
            create_notification(request,applications.createdby ,"message", applications.id)  

            return redirect('viewapplication',application_id=application_id)
        

       
    return render(request,'userprofile/viewjobapplication.html',{'application':applications})

@login_required
def dashboard_job(request,job_id):
    jobs=get_object_or_404(job, pk=job_id,createdby=request.user)
    return render(request,'userprofile/dashboard_job.html',{'job':jobs})