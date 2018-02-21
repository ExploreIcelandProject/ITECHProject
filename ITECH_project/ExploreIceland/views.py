from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from ExploreIceland.models import attractionCategory
from ExploreIceland.models import attractionPage
from ExploreIceland.forms import UserForm, UserProfileForm


# Create your views here.

def index(request):
    return render(request, 'ExploreIceland/index.html')


def about(request):
    return render(request, 'ExploreIceland/about.html',)

def attraction(request):
    
    category_list=attractionCategory.objects.order_by('-likes')
    context_dict = {'categories': category_list}
    
    return render(request, 'ExploreIceland/attraction.html', context=context_dict)


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

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'ExploreIceland/register.html',
              {'user_form': user_form,
              'profile_form': profile_form,
              'registered': registered})













