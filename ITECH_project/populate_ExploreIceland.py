
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                                'ITECH_project.settings')
import django
django.setup()
from ExploreIceland.models import attractionCategory, attractionPage
def populate():
    
    attraction_pages = [
        {"title": "Northern Light",
        "url":"northernlights","views":100},
        {"title":"Volcano",
        "url":"volcano","views":100},
        {"title":"Hot Spring",
        "url":"hotspring","views":100},
        {"title":"Waterfall",
        "url":"waterfall","views":100},
        {"title":"Glacier",
        "url":"glacier","views":100}]
    city_pages = [
        {"title":"Reykjavík",
        "url":"reykjavik","views":100},
        {"title":"Husavik",
        "url":"husavik","views":100},
        {"title":"Akureyri",
        "url":"akureyri","views":100},
        {"title":"Egilstaðir",
        "url":"egilsstadir","views":100},
        {"title":"Ísafjörður",
        "url":"isafjordur","views":100}]
    activity_pages = [
        {"title":"Hiking",
        "url":"hiking","views":100},
        {"title":"Ski",
        "url":"ski","views":100},
        {"title":"Ice Cave Exploring",
        "url":"icecaveexploring","views":100},
        {"title":"Whale Cruise",
        "url":"whalecruise","views":100},
        {"title":"Diving",
        "url":"diving","views":100},
        {"title":"Horse riding",
        "url":"horseriding","views":100}
         ]
    wildanimal_pages = [
        {"title":"Whale",
        "url":"whale","views":100},
        {"title":"seal",
        "url":"seal","views":100},
        {"title":"Icelandic horse",
        "url":"horse","views":100},
        {"title":"Puffin",
        "url":"puffin","views":100},
        {"title":"Reindeer",
        "url":"reindeer","views":100},
                          ]
    cats = {"Attraction": {"pages": attraction_pages,"views":100,"likes":100},
            "City": {"pages": city_pages,"views":100,"likes":100},
            "Activity": {"pages": activity_pages,"views":100,"likes":100},
            "Wildanimal": {"pages": wildanimal_pages,"views":100,"likes":100}
}

    for cat, cat_data in cats.items():
        c= add_cat(cat,cat_data["views"],cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],p["views"])
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
    
def add_cat(name,views=0,likes=0):
    c = attractionCategory.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c
    
    
    # Start execution here!
if __name__ == '__main__':
    print("Starting Explore Iceland population script...")
    populate()
