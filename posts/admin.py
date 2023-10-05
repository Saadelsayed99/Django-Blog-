from django.contrib import admin

# Register your models here.
from .models import post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','publish_date']
    search_fields =['title','content']
    list_filter = ['publish_date','auther']
    


admin.site.register(post,PostAdmin)