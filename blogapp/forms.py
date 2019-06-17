from django import forms

class CommentForm(forms.Form):

    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email '}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name '}), required=True)
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Comment '}),
                              required=True)
