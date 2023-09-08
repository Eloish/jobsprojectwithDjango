from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.jobs.models import job
from apps.userprofile.models import Userprofile
# Create your views here.

def frontpage(request):
    jobs=job.objects.filter(status=job.ACTIVE).order_by('-created_at')[0:3]
    return render(request, 'core/index.html',{'jobs':jobs})

def signuppage(request):
    if request.method== 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            account_type=request.POST.get('account_type','jobseeker')
            if account_type =='employer':
                userprofile=Userprofile.objects.create(user=user,is_employer=True)
                userprofile.save()
            else:
                userprofile=Userprofile.objects.create(user=user)
                userprofile.save()

            login(request,user)
            return redirect('dashboard')
    else:
        form= UserCreationForm()
    return render(request,'core/signup.html',{'form':form})