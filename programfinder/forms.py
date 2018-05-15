from django import forms

class FindScholarshipForm(forms.Form):
    lower_amount = forms.IntegerField(label='Lower Amount', min_value=0, required=False)
    upper_amount = forms.IntegerField(label='Upper Amount', min_value=0, required=False)
    deadline_month = forms.IntegerField(label='Deadline Month', min_value=1, max_value=12, required=False)
