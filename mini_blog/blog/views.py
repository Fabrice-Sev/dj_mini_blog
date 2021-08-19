from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import BlogPost, Blogger, Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .forms import CommentForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.



def index(request):
    num_users=User.objects.count()
    num_blogs=BlogPost.objects.count()
    num_comments=Comment.objects.count()
    num_bloggers=Blogger.objects.count()
    num_visits=request.session.get('num_visits',0)



    context={
        'num_users':num_users,
        'num_bloggers':num_bloggers,
        'num_blogs':num_blogs,
        'num_comments':num_comments,
        'num_visits':num_visits
    }
    # print(User._meta.get_fields()) To get fields of a model
    return render(request,'blog/index.html',context=context)

class BlogPostView(generic.ListView):
    model=BlogPost
    paginate_by=5

    # def get_queryset(self):
    #     return BlogPost.objects.all().order_by('-post_date')
        

    # To add the number of context variables
    def get_context_data(self, **kwargs):
        """**kwargs is used when you don't know the number of params""" 
        # Call the base implementation first to get the context
        context = super(BlogPostView, self).get_context_data(**kwargs)
        
        #Add data to the context variable
        context['num_blogs'] = BlogPost.objects.count()
        return context

class BlogPostDetail(generic.DetailView):
    model=BlogPost

def bloggers(request):
    bloggers=Blogger.objects.all()
    num_bloggers= Blogger.objects.count()
    
    context={
        'blogger_list': bloggers,
        'num_bloggers': num_bloggers,
    }
    return render(request,'blog/blogger_list.html',context)

def bloggerDetail(request,author_id):

    blogger=get_object_or_404(Blogger,pk=author_id)
    bloglist=blogger.blogpost_set.all()
    context={
        'blogger': blogger,
        'bloglist': bloglist
    }
    return render(request,'blog/blogger_detail.html',context)


def addComment(request,pk):
    blogpost=get_object_or_404(BlogPost,pk=pk)

    #Check if the post has been sent before or if it's the first time
    if request.method == 'POST':
        form = CommentForm(request.POST)
        newComment=Comment()

        if form.is_valid():
            newComment.comment_text =form.cleaned_data['comment_text']
            newComment.blog=blogpost
            newComment.comment_author=request.user
            newComment.post_date=timezone.now()
            newComment.save()
            #if a view is passed
            # redirect(BlogPostView.as_view())
            # if a link is passed
            # redirectLink='/blogs/'+ str(blogpost.pk)
            print( str(newComment.comment_text)+ ' ' + str(newComment.blog)+ ' '+ str(newComment.post_date)+ ' ' + str(newComment.comment_author))
            return redirect(blogpost)
    else :
        #First time receiving form
        placeholder="New Comment"
        form=CommentForm(initial={'comment_text':placeholder})
    
    context={
        'form': form,
        'blogpost' : blogpost
    }


    return render(request,'blog/comment_add.html',context)

def signUp(request):
    if request.method == 'POST':
        username= request.POST["username"]
        email= request.POST["email"]
        password= request.POST["password"]
        firstName= request.POST["first_name"]
        lastName= request.POST["last_name"]
        
        try:
            user=User.objects.create_user(username,email,password)
            user.first_name= firstName
            user.last_name= lastName
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect(reverse('blog:index'))
        except IntegrityError:
            print("Oops, User already exists")
            return(redirect(reverse('blog:login')))
    return render(request,'registration/signUp.html',{})

def log_in(request):
    next=request.GET.get('next')
    template='registration/login.html'
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(next)
        else:
            print('Could not log in')
            return redirect(reverse('blog:login'))
    
    context={}
    if next is not None:
        context.update({"next":next})
    else:
        context.update({"next":'/'})
    return render(request,template,context=context)

def log_out(request):
    logout(request)
    return redirect(reverse('blog:login'))