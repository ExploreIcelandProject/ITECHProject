
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                                'ITECH_project.settings')
import django
django.setup()
from ExploreIceland.models import attractionCategory, attractionPage
def populate():
    
    attraction_pages = [
        {"title": "Northern Light",
        "url":"http://facebook.com"},
        {"title":"Volcano",
        "url":"http://facebook.com/"},
        {"title":"Hot Spring",
        "url":"http://facebook.com"},
        {"title":"Waterfall",
        "url":"http://facebook.com"},
        {"title":"Glacier",
        "url":"http://facebook.com"}]
    city_pages = [
        {"title":"Reykjavík",
        "url":"http://facebook.com"},
        {"title":"Keflavík",
        "url":"http://facebook.com"},
        {"title":"Akureyri",
        "url":"http://facebook.com"},
        {"title":"Egilstaðir",
        "url":"http://facebook.com"},
        {"title":"Ísafjörður",
        "url":"http://facebook.com"}]
    activity_pages = [
        {"title":"Hiking",
        "url":"http://facebook.com"},
        {"title":"Ski",
        "url":"http://facebook.com"},
        {"title":"Ice Cave Exploring",
        "url":"http://facebook.com"},
        {"title":"Whale Cruise",
        "url":"http://facebook.com"},
        {"title":"Diving",
        "url":"http://facebook.com"},
        {"title":"Horse riding",
        "url":"http://facebook.com"}
         ]
    cats = {"Attraction": {"pages": attraction_pages},
            "City": {"pages": city_pages},
            "Activity": {"pages": activity_pages} }

    for cat, cat_data in cats.items():
        c= add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])
    # Print out the categories we have added.
    for c in attractionCategory.objects.all():
        for p in attractionPage.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = attractionPage.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
    
def add_cat(name):
    c = attractionCategory.objects.get_or_create(name=name)[0]
    c.save()
    return c
    
    
    # Start execution here!
if __name__ == '__main__':
    print("Starting Explore Iceland population script...")
    populate()
