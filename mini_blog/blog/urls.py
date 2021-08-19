from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    # ex:/blog/
    path('',views.index,name='index'),
    # ex:/blog/blogs/
    path('blogs/',views.BlogPostView.as_view(),name='blogs'),
    # ex:/blog/blogs/2/
    path('blogs/<int:pk>',views.BlogPostDetail.as_view(),name='blog_detail'),
    # ex:/blog/blogs/2 (blog-id)/create
    path('blogs/<int:pk>/create',views.addComment,name='add_comment'),
    # ex:/blog/bloggers
    path('bloggers/',views.bloggers ,name='bloggers'),
    # ex:/blog/bloggers/5
    path('bloggers/<author_id>',views.bloggerDetail, name='blogger_detail'),
    # ex: /blog/signup/
    path('signup/',views.signUp,name='signup'),
    # ex: /blog/login/
    path('login/',views.log_in,name='login'),
    # ex: /blog/logout
    path('logout/',views.log_out,name='logout'),

]