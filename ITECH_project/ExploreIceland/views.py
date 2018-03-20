from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from ExploreIceland.models import attractionCategory
from ExploreIceland.models import attractionPage
from ExploreIceland.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

from django.shortcuts import redirect
from ExploreIceland.webhose_search import run_query
# Create your views here.

def index(request):
    request.session.set_test_cookie()
    context_dict={}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    response = render(request, 'ExploreIceland/index.html',context=context_dict)
    return response

def about(request):
    category_list=attractionCategory.objects.order_by('-likes')
    page_list = attractionPage.objects.order_by('-views')
    context_dict = {'categories': category_list,'pages': page_list
}
    return render(request, 'ExploreIceland/about.html',context=context_dict)

def attraction(request):
    
    
    
    return render(request, 'ExploreIceland/attraction.html', )

def glacier(request):
    try:
        page = attractionPage.objects.get(url="glacier")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/glacier.html',)

def vatnajokull(request):
    return render(request, 'ExploreIceland/vatnajokull.html',)

def langjokull(request):
    return render(request, 'ExploreIceland/langjokull.html',)

def hofsjokull(request):
    return render(request, 'ExploreIceland/hofsjokull.html',)

def myrdalsjokull(request):
    return render(request, 'ExploreIceland/myrdalsjokull.html',)

def eyjafjallajokull(request):
    
    return render(request, 'ExploreIceland/eyjafjallajokull.html',)

def city(request):
    return render(request, 'ExploreIceland/city.html',)

def activity(request):
    return render(request, 'ExploreIceland/activity.html',)
def diving(request):
    try:
        page = attractionPage.objects.get(url="diving")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/diving.html',)

def horseriding(request):
    try:
        page = attractionPage.objects.get(url="horseriding")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/horseriding.html',)

def icecaveexploring(request):
    try:
        page = attractionPage.objects.get(id=13)
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/icecaveexploring.html',)

def whalecruise(request):
    try:
        page = attractionPage.objects.get(url="whalecruise")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/whalecruise.html',)

def wildanimal(request):
    return render(request, 'ExploreIceland/wildanimal.html',)

def whale(request):
    try:
        page = attractionPage.objects.get(url="whale")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/whale.html',)

def seal(request):
    try:
        page = attractionPage.objects.get(url="seal")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/seal.html',)

def horse(request):
    
    try:
        page = attractionPage.objects.get(url="horse")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/horse.html',)

def puffin(request):
    try:
        page = attractionPage.objects.get(url="puffin")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/puffin.html',)

def reindeer(request):
    try:
        page = attractionPage.objects.get(url="reindeer")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    
    return render(request, 'ExploreIceland/reindeer.html',)

def bluelagoon(request):
    return render(request, 'ExploreIceland/bluelagoon.html',)
def hotspring(request):
    try:
        page = attractionPage.objects.get(url="hotspring")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass

    return render(request, 'ExploreIceland/hotspring.html',)
def myvatnbath(request):
    return render(request, 'ExploreIceland/myvatnbath.html',)

def goldencircle(request):
    return render(request, 'ExploreIceland/goldencircle.html',)
def kirkjufell(request):
    return render(request, 'ExploreIceland/kirkjufell.html',)
def northernlights(request):
    try:
        page = attractionPage.objects.get(url="northernlights")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    return render(request, 'ExploreIceland/northernlights.html',)
def reynisfjara(request):
    return render(request, 'ExploreIceland/reynisfjara.html',)

def bardarbunga(request):
    return render(request, 'ExploreIceland/bardarbunga.html',)
def katla(request):
    return render(request, 'ExploreIceland/katla.html',)
def maelifell(request):
    return render(request, 'ExploreIceland/maelifell.html',)
def volcano(request):
    try:
        page = attractionPage.objects.get(url="volcano")
        page.views = page.views + 1
        page.save()
        url = page.url
    except:
        pass
    
    return render(request, 'ExploreIceland/volcano.html',)

def gallery(request):
    return render(request, 'ExploreIceland/gallery.html',)

def contact(request):
    return render(request, 'ExploreIceland/contact.html',)

def show_attractioncategory(request, category_name_slug):
    context_dict = {}
    try:
        category= attractionCategory.objects.get(slug=category_name_slug)
        pages = attractionPage.objects.filter(category=category)
        
        context_dict['pages'] = pages
        context_dict['category'] = category
    
    except attractionCategory.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    context_dict['query'] = category.name
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
#            Run our search API function to get the results list!
            result_list = run_query(query)
            context_dict['query'] = query
            context_dict['result_list'] = result_list
    # Go render the response and return it to the client.
    
    return render(request, 'ExploreIceland/attractioncategory.html', context_dict)

def base_bootstrap(request):
    return render(request, 'ExploreIceland/base_bootstrap.html',)




@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")





def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        #update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        # set the last visit cookie
        request.session['last_visit'] = last_visit_cookie
        # Update/set the visits cookie
        request.session['visits'] = visits



def search(request):
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
    # Run our Webhose search function to get the results list!
            result_list = run_query(query)
    return render(request, 'ExploreIceland/search.html', {'result_list': result_list})





def track_url(request):
    page_id = None
    url = '/ExploreIceland/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = attractionPage.objects.get(id=page_id)
               
                url = page.url
            except:
                pass
    return redirect(url)



















