from django.urls import path
from blogapp.views import PostUpdate,PostDelete
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'posts'

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/post/add', views.postcreate),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html',redirect_field_name='/dashboard')),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='blogapp/blogpost_list.html',next_page='/')),
    path('', views.index, name='index'),
    path('<int:blogpost_id>',views.post_detail , name='post_detail' ),
    path('categories/<int:category_id>', views.category_detail, name='category'),
    path('accounts/post/edit/<int:pk>',PostUpdate.as_view()),
    path('accounts/post/delete/<int:pk>',PostDelete.as_view()),
    

]
