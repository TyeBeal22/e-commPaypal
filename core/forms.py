from django import forms
from cart.models import Product


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your name"
    }))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your email"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your message'
    }))



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
            'available_colors',
            'available_sizes',
        ]