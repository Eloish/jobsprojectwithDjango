from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Addjobform,applicationForm
from .models import job
from django.contrib import messages

from apps.notifications.utilities import create_notification

def job_detail(request ,job_id):
    jobs=job.objects.get(pk=job_id)
    return render (request,'job_details.html',{'job':jobs})
def search(request):
    return render(request,'search.html')  
  
@login_required
def addjob(request):
    if request.method=="POST":
        form=Addjobform(request.POST)
        if form.is_valid():
            job=form.save(commit=False)
            job.createdby= request.user
            job.save()
            return redirect('dashboard')  
        else:
            messages.success(request,form.errors)
        
            
    else:
        form= Addjobform()
    return render (request,'add_job.html',{'form':form})

@login_required
def edit_job(request,job_id):
    jobs=get_object_or_404(job,pk=job_id,createdby=request.user)
    if request.method=="POST":
        form=Addjobform(request.POST,instance=jobs)
        if form.is_valid():
            Getjob=form.save(commit=False)
            Getjob.status= request.POST.get('status')
            Getjob.save()
            return redirect('dashboard')  
        else:
            messages.success(request,form.errors)
        
            
    else:
        form= Addjobform(instance=jobs)
    return render (request,'edit_job.html',{'form':form,'job':jobs})
@login_required

def apply_for_job(request,job_id):


    jobs=job.objects.get(pk=job_id)
    if request.method=='POST':
        form=applicationForm(request.POST)
        if form.is_valid():
            application=form.save(commit=False)
            application.job=jobs
            application.createdby=request.user
            application.save()
            create_notification(request,jobs.createdby ,"application",application.id)

            return redirect('dashboard')
    else:
        form=applicationForm()
    return render(request,"apply_for_job.html",{'form':form,'job':jobs})





# Create your views here.
