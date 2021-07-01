from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html

# Register your models here.
admin.site.register(Slider)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','myPhoto','first_name','last_name','role','created_date']
    # clicable fields
    list_display_links = ['id','first_name']
    # search fields
    search_fields = ['id','role']
    # filter by values
    list_filter = ['role']

    def myPhoto(self,obj):
        return format_html("<img width='40' src='{}' />".format(obj.photo.url))
