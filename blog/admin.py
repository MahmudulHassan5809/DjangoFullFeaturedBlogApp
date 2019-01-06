from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('id' , 'title' , 'content' , 'date_posted')
	list_display_links = ('id' , 'title')
	list_filter = ('title',)
	search_fields = ('title','content')
	list_per_page = 25


# Register your models here.
admin.site.register(Post , PostAdmin)
