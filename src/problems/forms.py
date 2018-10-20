from django import forms


class CodeSubmissionForm(forms.Form):
    file = forms.FileField(label='Submit code')
