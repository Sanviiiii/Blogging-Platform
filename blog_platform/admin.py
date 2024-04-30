from django.contrib import admin
from .models import PostData

# Register your models here.
class PostdataAdmin(admin.ModelAdmin):
    list_display = ("title_name","author")
    search_fields = ('title_name',)

admin.site.register(PostData, PostdataAdmin)

