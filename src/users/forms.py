from django import forms
from .models import UserProfile

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
