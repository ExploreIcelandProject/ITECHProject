from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    context_dict = {'boldmessage': "homepage!"}
    return render(request, 'ExploreIceland/index.html', context=context_dict)


def about(request):
    return render(request, 'ExploreIceland/about.html',)

def attraction(request):
    return render(request, 'ExploreIceland/attraction.html',)
