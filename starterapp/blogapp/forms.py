from django import forms
from django.forms import Textarea,ModelForm,TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost,PostComment

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
      
        # fields = ('title','body','category','feat_img','author')
        fields = ('title','body','category','feat_img',)
        widgets = {
            'body': Textarea(attrs={'cols': 50, 'rows': 20,'class':'form-control','id':'editor',}),
            'title':TextInput(attrs={'class':'form-control'})
        }
        
class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment_body',)
        widgets = {'comment_body':Textarea(attrs={'cols':20,'rows':5,'class':'form-control'})}