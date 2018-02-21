from django.contrib import admin
from ExploreIceland.models import attractionCategory, attractionPage
from ExploreIceland.models import UserProfile



class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(attractionCategory,CategoryAdmin)
admin.site.register(attractionPage,PageAdmin)
admin.site.register(UserProfile)
