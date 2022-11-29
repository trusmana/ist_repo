from django import forms

from apps.products.models import REPORT_DATA,STATUS_UPDATE

class DateForm(forms.Form):
    from_date = forms.DateField(widget=forms.DateInput({'class':'input-append span5',
        'placeholder':'YYYY-MM-DD'}))
    until_date = forms.DateField(widget=forms.DateInput({'class':'input-append span5',
        'placeholder':'YYYY-MM-DD'}))
    #status = forms.ChoiceField(choices=STATUS_UPDATE,widget=forms.Select({'class':'input-text span5'}),required=False)
    report = forms.ChoiceField(choices=REPORT_DATA,widget=forms.Select({'class':'input-text span5'}))