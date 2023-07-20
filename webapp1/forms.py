from pyexpat import model
from django import forms
from webapp1.models import contact

class nameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
