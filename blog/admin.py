from django.contrib import admin
from .models import Post

# This is where to register models to include them in the Django
# administration site—using this site is optional.

# comment ---- admin.site.register(Post) = @admin.register(Post)


# There is configuration how to display our model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
