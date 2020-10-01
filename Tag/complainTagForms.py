from django import forms
from .models import ComplainTag

class ComplainTagForm(forms.ModelForm):
    class Meta:
        model = ComplainTag
        fields = '__all__'