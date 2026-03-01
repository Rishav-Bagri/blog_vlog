from django.contrib import admin

from blogs.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}

    list_display=['title', 'author', 'category','status', 'is_featured']
    list_editable=['is_featured']
    search_fields=['id','title', 'status', 'category__category_name', 'is_featured']
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)