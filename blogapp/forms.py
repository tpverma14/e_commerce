from django import forms
from blogapp.models import Blog



class CommentForm(forms.Form):


    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Comment '}),
                              required=True)

class Blog_form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
                              required=True)

    name = forms.CharField(
                widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Enter  name'}), required=True)


    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'write blog '}),
                           required=True)


    class Meta():
        model=Blog
        fields= ['title','name','body','image',]

