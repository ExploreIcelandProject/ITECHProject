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

# Create your views here.

def index(request):
    request.session.set_test_cookie()
    context_dict={}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request, 'ExploreIceland/index.html',context=context_dict)
    return response

def about(request):
    return render(request, 'ExploreIceland/about.html',)

def attraction(request):
    
    category_list=attractionCategory.objects.order_by('-likes')
    context_dict = {'categories': category_list}
    
    return render(request, 'ExploreIceland/attraction.html', context=context_dict)

def city(request):
    return render(request, 'ExploreIceland/city.html',)

def activity(request):
    return render(request, 'ExploreIceland/activity.html',)

def wildanimal(request):
    return render(request, 'ExploreIceland/wildanimal.html',)

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














