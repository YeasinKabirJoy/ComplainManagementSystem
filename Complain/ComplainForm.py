from django.forms import ModelForm,CheckboxSelectMultiple
from .models import Complain

class ComplainForm(ModelForm):
    class Meta:
        model = Complain
        fields = ('image', 'description', 'type','tag')
        widgets={
            'tag':CheckboxSelectMultiple()
        }
