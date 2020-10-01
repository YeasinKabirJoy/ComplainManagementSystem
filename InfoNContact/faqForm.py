from django import forms
from .models import FAQ

class FaqForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'