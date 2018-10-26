from django import forms

from django_countries.widgets import CountrySelectWidget

from .models import UserProfile


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['display_name', 'about', 'birthday', 'country', 'location', 'avatar']
        widgets = {
                'country': CountrySelectWidget(
                    layout='{widget}<span class="icon"><img class="country-select-flag" id="{flag_id}" style="margin: 6px 4px 0" src="{country.flag}"></span>'
                    )
                }
