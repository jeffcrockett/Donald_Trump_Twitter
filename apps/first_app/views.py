from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.core import serializers
import json

def index(request):
    return render(request, 'first_app/index.html')

def parse(request):
    words = Word.objects.all()
    pos_string = ''
    s = request.POST['line'].split(' ')
    for item in s:
        for word in words:
            if item == word.name:
                pos_string += word.pos + ' '
    context = {'pos':pos_string}
    return render(request, 'first_app/parse.html', context)

def alltweets(request):
    tweets = TrumpTweet.objects.all()
    return render(request, 'first_app/all.html', {'tweets':tweets})

def all_json(request):
    words = Word.objects.all()
    tweets = TrumpTweet.objects.all()
    return HttpResponse(serializers.serialize("json", words), content_type="application/json")

# Create your views here.
def all_html(request):
    return render(request, "first_app/all.html", {'tweets': TrumpTweet.objects.all()})

def find(request):
    return render(request, 'first_app/all.html', {'tweets': TrumpTweet.objects.filter(content__contains=request.POST['first_name_starts_with'])})

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'] )
    return render(request, 'first_app/all.html', {'users': User.objects.order_by('-id')})
