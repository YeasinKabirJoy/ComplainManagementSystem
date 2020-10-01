from django import forms
from .models import Verified_User

class User_Verification_Form(forms.ModelForm):
    class Meta:
        model = Verified_User
        fields = ('email', 'image_of_id')