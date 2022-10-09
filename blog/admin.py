from django.contrib import admin
from blog.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "-N/A-"
    list_display = ('title', 'published_date', 'status', 'counted_views')

admin.site.register(Post,PostAdmin)
