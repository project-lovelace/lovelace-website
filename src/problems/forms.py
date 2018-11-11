from django import forms


class CodeSubmissionForm(forms.Form):
    code = forms.CharField(required=False, label="Submit code")
    file = forms.FileField(required=False, label="Submit file")

