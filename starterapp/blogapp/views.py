from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import BlogPost, Category,PostComment
from .forms import SignUpForm,PostCreateForm,PostCommentForm
# Create your views here.


def index(request):
    queryset = BlogPost.objects.all().order_by('-created_at')
    featured = BlogPost.objects.all().filter(is_featured=True)[:1]
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    blog_posts = paginator.get_page(page)
    context = {'blog_posts':blog_posts,'featured':featured}
    return render(request, 'blogapp/blogpost_list.html',context)

# latest_posts_list = BlogPost.objects.all().order_by('-created_at')[:5]
# category_list = Category.objects.all()
# context = {'latest_posts_list': latest_posts_list,
#            'category_list': category_list}

def post_detail(request,blogpost_id):
    post = get_object_or_404(BlogPost, pk=blogpost_id)
    posts_category = post.category
    other_posts = BlogPost.objects.filter(category=posts_category)  
    post_comment = PostComment.objects.all().filter(comment_post=blogpost_id)
    user = request.user
    form = None 
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
           comment =  form.save(commit=False)
           comment.comment_author = request.user
           comment.comment_post = post
           comment.save()
           return redirect('/')


    else:
            form = PostCommentForm
    context = {'post': post,'post_comment':post_comment,'form':form,'other_posts':other_posts}
    return render(request, 'blogapp/blogpost_detail.html', context)

def category(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'blogapp/category_list.html', context)
def dashboard(request):
    user = request.user
    users_posts = BlogPost.objects.filter(author=user)
    context = {'users_posts':users_posts,}
    return render(request, 'blogapp/dashboard.html',context)

def category_detail(request, category_id):
    category_posts_list = BlogPost.objects.all().filter(
        category_id=category_id).order_by('-created_at')
    category = get_object_or_404(Category, pk=category_id)
    context = {'category': category,
               'category_posts_list': category_posts_list}
    return render(request, 'blogapp/category_detail.html', context)
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')

    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
def postcreate(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post = form.save()
            return redirect('/')
        

    else:
        form = PostCreateForm()
    return render(request, 'blogapp/blogpost_form.html', {'form': form})
    #success_url = '/'
class PostUpdate(UpdateView):
    model = BlogPost
    
      
        # fields = ('title','body','category','feat_img','author')
    form_class = PostCreateForm
    template_name_suffix = '_update_form'
    success_url = ('/')

class PostDelete(DeleteView):
    model = BlogPost
    success_url = ('/')
def post_archive(request,created_at):
    post_date_list = BlogPost.objects.all().filter(created_at=BlogPost.created_at)
    post = get_object_or_404(BlogPost, pk=created_at)
    context = {'post_date_list':post_date_list,'post':post}
    return render(request, 'blogapp/blogpost_form.html', {'form': form})
