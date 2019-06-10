from django import forms
from django.utils.translation import gettext_lazy as _
from cart.models import Checkout


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]


class CartAddProductFrom(forms.Form):

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int, label=_('Quantity'))
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)



class Checkout_form(forms.ModelForm):
    country=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'state/country'}),required=True)

    first_name =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ' , 'placeholder':'Enter first name' }),required=True)

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'Enter last name'}),required=True)


    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Address' }),required=True)

    email =forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control ' , 'placeholder': 'Enter Email'}),required=True)

    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Enter phone no.'}),

                            required=True)
    postal_code = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control ' , 'placeholder':'Enter postal address'}),required=True)

    city =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Enter city' }),required=True)


    other_notes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'other_details' }),required=True)


    class Meta:
        model=Checkout
        fields=['country','first_name','last_name','address','email','phone','postal_code','city','other_notes']


