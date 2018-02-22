from django.conf.urls import url
from ExploreIceland import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/',views.about, name='about'),
    url(r'^attraction/',views.attraction, name='attraction'),
    url(r'^attractioncategory/(?P<category_name_slug>[\w\-]+)/$',
        views.show_attractioncategory, name='show_attractioncategory'),
    
    
    url(r'^restricted/', views.restricted, name='restricted'),
   url(r'^base_bootstrap/', views.base_bootstrap, name='base_bootstrap'),
]
