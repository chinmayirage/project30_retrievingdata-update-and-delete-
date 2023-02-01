from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)
    
def display_access(request):
    QSA=AccessRecords.objects.all()
    d={'access':QSA}
    return render(request,'display_access.html',d)


def update_webpage(request):
    QSW=Webpage.objects.all()
    Webpage.objects.filter(name='manu').update(url='https://manohar.in')
    Webpage.objects.filter(topic_name='Cricket').update(name='MSD')
    Webpage.objects.filter(name='pooji').update(topic_name='badminton')
    Webpage.objects.filter(name='uma').update(topic_name='cricket')
    Webpage.objects.update_or_create(name='suresh',defaults={'url':'https://suresh.in'})
    T=Topic.objects.get_or_create(topic_name='shuttle')[0]
    T.save()
    Webpage.objects.update_or_create(name='ashu',defaults={'topic_name':T,'url':'https://suresh.in'})
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def delete_webpage(request):
  Webpage.objects.filter(name='Abcdefg').delete()
  Webpage.objects.filter(topic_name='cricket').delete()
  Webpage.objects.filter(name='pooji').delete()
  Webpage.objects.all().delete()
  QSW=Webpage.objects.all()
  d={'webpages':QSW}
  return render(request,'display_webpages.html',d)

    


