from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Blogger(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=CASCADE)
    date_joined=models.DateField(verbose_name='Date Joined')
    blogger_bio=models.CharField(verbose_name='Bio',max_length=1000)

    def get_full_name(self):
        return self.user.first_name+' '+self.user.last_name

    def get_short_name(self):
        return self.user.last_name
        
    def __str__(self) -> str:
        return self.user.username
    
    def set_date_joined(self):
        return self.user.date_joined

class BlogPost(models.Model):
    name=models.CharField(max_length=255)
    blog_author=models.ForeignKey(Blogger,null=True,on_delete=SET_NULL)
    post_date=models.DateField(verbose_name='Post Date',default=timezone.now)
    content=models.CharField( max_length=1000)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-post_date','name']
    
    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.id)])

class Comment(models.Model):
    blog=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    comment_author= models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=SET_NULL)
    post_date=models.DateTimeField(verbose_name='Post Date',default=timezone.now)
    comment_text=models.CharField(verbose_name='Text',max_length=255)
    
    class Meta:
        ordering=['-post_date']

    def __str__(self):
        return self.comment_text[0:75] 