import json
from apps.jobs.models import job
from django.db.models import Q 
from django.http import JsonResponse


def search_job(request):
    jobList=[]
   
    data= json.loads(request.body)
    query=data['query']
    company_size=data['company_size']
    jobs=job.objects.filter(status=job.ACTIVE).filter(Q(title__icontains=query)|Q(description__icontains=query)|Q(long_description__icontains=query)|Q(company_name__icontains=query)|Q(company_place__icontains=query))

    if company_size:
        jobs=jobs.filter(company_size=company_size)

    for Fjob in jobs:
        obj={
            'id':Fjob.id,
            'title':Fjob.title,
            'company_name':Fjob.company_name,
            'url':'/jobs/%s/' %Fjob.id
        }
        jobList.append(obj)

    return JsonResponse({'jobs': jobList})
        