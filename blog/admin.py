from django.contrib import admin
from blog.models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "-N/A-"
    list_display = ('title', 'author', 'published_date', 'created_date', 'status', 'counted_views')
    list_filter = ['status', 'author']
    search_fields = ['title', 'content']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)