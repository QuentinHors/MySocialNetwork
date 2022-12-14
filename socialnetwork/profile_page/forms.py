from django import forms
from .models import Profile, Post, Comment


class ProfileForms(forms.ModelForm):
    first_name = forms.CharField(max_length=60,
                                 widget=forms.TextInput(attrs={'placeholder': 'Prénom'}))
    last_name = forms.CharField(max_length=60,
                                widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    description = forms.CharField(max_length=500,
                                  widget=forms.Textarea(attrs={'placeholder': 'A propos'}))
    image_profile = forms.ImageField(required=False, label="")

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'description', 'image_profile']


class PostForm(forms.ModelForm):
    text = forms.CharField(max_length=255,
                           widget=forms.TextInput(attrs={'placeholder': 'Texte...'}))
    image = forms.ImageField(required=False, label="")

    class Meta:
        model = Post
        fields = ['text', 'image']


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=255,
                           widget=forms.TextInput(attrs={'placeholder': 'Texte...'}))
    image = forms.ImageField(required=False, label="")

    class Meta:
        model = Comment
        fields = ['text', 'image']