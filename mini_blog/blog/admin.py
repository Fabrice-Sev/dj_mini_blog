from django.contrib import admin
from .models import BlogPost, Blogger,Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model=Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=['name','post_date','blog_author']
    list_filter=['blog_author']
    inlines=[CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display=['blog', 'comment_author','post_date','comment_text']#Decide what attributes to display
    list_filter=['blog',] #Filter
    fields=[('blog','comment_author'),'post_date','comment_text']#Decide of the order

class BloggerAdmin(admin.ModelAdmin):
    list_display=['user','get_full_name','date_joined',]
    list_filter=['date_joined']



admin.site.register(Comment,CommentAdmin)
admin.site.register(Blogger,BloggerAdmin)