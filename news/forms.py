from django import forms

from .models import News
import re

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# class ContactForm(forms.Form):
#    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class': 'form-control'}))
#    content = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'class': 'form-control'}), )

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
    password2 = forms.CharField(label='Password confirmation:', widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    # title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control'}))
    # is_published = forms.BooleanField(label='Is published?', initial=True)
    # category = forms.ModelChoiceField(empty_label='Choose Category', queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Title no have start with digits')

        return title