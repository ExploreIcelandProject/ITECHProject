from django.conf.urls import url
from ExploreIceland import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/',views.about, name='about'),
    url(r'^attraction/',views.attraction, name='attraction'),
    url(r'^attractioncategory/attraction/glacier/',views.glacier, name='glacier'),
    url(r'^vatnajokull/',views.vatnajokull, name='vatnajokull'),
    url(r'^langjokull/',views.langjokull, name='langjokull'),
    url(r'^hofsjokull/',views.hofsjokull, name='hofsjokull'),
    url(r'^myrdalsjokull/',views.myrdalsjokull, name='myrdalsjokull'),
    url(r'^eyjafjallajokull/',views.myrdalsjokull, name='eyjafjallajokull'),
    url(r'^city/',views.city, name='city'),
    url(r'^activity/',views.activity, name='activity'),
    url(r'^attractioncategory/activity/icecaveexploring/',views.icecaveexploring, name='icecaveexploring'),
    url(r'^attractioncategory/activity/whalecruise/',views.whalecruise, name='whalecruise'),
    url(r'^wildanimal/',views.wildanimal, name='wildanimal'),
    url(r'^attractioncategory/wildanimal/whale',views.whale, name='whale'),
    url(r'^attractioncategory/wildanimal/seal/',views.seal, name='seal'),
    url(r'^attractioncategory/wildanimal/horse/',views.horse, name='horse'),
    url(r'^attractioncategory/wildanimal/puffin/',views.puffin, name='puffin'),
    url(r'^attractioncategory/wildanimal/reindeer/',views.reindeer, name='reindeer'),
    url(r'^gallery/',views.gallery, name='gallery'),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^attractioncategory/(?P<category_name_slug>[\w\-]+)/$',
        views.show_attractioncategory, name='show_attractioncategory'),
    
    
    url(r'^restricted/', views.restricted, name='restricted'),
   url(r'^base_bootstrap/', views.base_bootstrap, name='base_bootstrap'),
]
