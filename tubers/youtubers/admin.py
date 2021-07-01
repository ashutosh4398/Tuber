from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.
@admin.register(Youtuber)
class YTAdmin(admin.ModelAdmin):

    def YTPhoto(self,instance):
        return format_html("<img src={} width='40' />".format(instance.photo.url))

    list_display = ['id','name','YTPhoto','subs_count','is_featured']
    search_field = ['name','camera_type']
    list_filter = ['city','camera_type']
    list_display_links = ['id','name']
    # editable fields
    list_editable = ['is_featured']