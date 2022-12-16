from django import forms

from apps.products.models import REPORT_DATA,RefCustomer,JUMLAHREFF,JUMLAHREFFCS,KURS_DUTY

class DateForm(forms.Form):
    from_date = forms.DateField(widget=forms.DateInput({'class':'input-append span5',
        'placeholder':'YYYY-MM-DD'}))
    until_date = forms.DateField(widget=forms.DateInput({'class':'input-append span5',
        'placeholder':'YYYY-MM-DD'}))
    #status = forms.ChoiceField(choices=STATUS_UPDATE,widget=forms.Select({'class':'input-text span5'}),required=False)
    report = forms.ChoiceField(choices=REPORT_DATA,widget=forms.Select({'class':'input-text span5'}))

class KursDutyForm(forms.ModelForm):
    kurs_duty = forms.ChoiceField(choices=KURS_DUTY,widget=forms.Select({'class':"input-small"}))

    class Meta:
        model = RefCustomer
        fields =['kurs_duty']
    

class RefForm(forms.ModelForm):
    jumlahreff = forms.ChoiceField(choices=JUMLAHREFF,label="Jumlah REF | Customer Ref",widget=forms.Select({'class':"input-small"}))
    jumlahreffcs = forms.ChoiceField(choices=JUMLAHREFFCS,widget=forms.Select({'class':"input-small"}))
    ref1 = forms.CharField(widget=forms.TextInput({'class':"input-small 1 2 3 4 5 6 7 8 9 10 ref",'placeholder':'Ref 1'}),required=False )
    ref2 = forms.CharField(widget=forms.TextInput({'class':"input-small 2 3 4 5 6 7 8 9 10 ref",'placeholder':'Ref 2'}),required=False )
    ref3 = forms.CharField(widget=forms.TextInput({'class':"input-small 3 4 5 6 7 8 9 10 ref",'placeholder':'Ref 3'}),required=False)
    ref4 = forms.CharField(widget=forms.TextInput({'class':"input-small 4 5 6 7 8 9 10 ref ",'placeholder':'Ref 4'}),required=False )
    ref5 = forms.CharField(widget=forms.TextInput({'class':"input-small 5 6 7 8 9 10 ref",'placeholder':'Ref 5'}),required=False )
    ref6 = forms.CharField(widget=forms.TextInput({'class':"input-small 6 7 8 9 10 ref",'placeholder':'Ref 6'}),required=False )
    ref7 = forms.CharField(widget=forms.TextInput({'class':"input-small 7 8 9 10 ref ",'placeholder':'Ref 7'}),required=False )
    ref8 = forms.CharField(widget=forms.TextInput({'class':"input-small 8 9 10 ref",'placeholder':'Ref 8'}),required=False )
    ref9 = forms.CharField(widget=forms.TextInput({'class':"input-small 9 10 ref",'placeholder':'Ref 9'}),required=False )
    ref10 = forms.CharField(widget=forms.TextInput({'class':"input-small 10 ref",'placeholder':'Ref 10'}),required=False )

    csref1 = forms.CharField(widget=forms.TextInput({'class':"input-small 11 12 13 14 15 16 17 18 19 20 cs",'placeholder':'CSREF 1'}),required=False )
    csref2 = forms.CharField(widget=forms.TextInput({'class':"input-small 12 13 14 15 16 17 18 19 20 cs",'placeholder':'CSREF 2'}),required=False )
    csref3 = forms.CharField(widget=forms.TextInput({'class':"input-small 13 14 15 16 17 18 19 20 cs",'placeholder':'CSREF 3'}),required=False )
    csref4 = forms.CharField(widget=forms.TextInput({'class':"input-small 14 15 16 17 18 19 20 cs",'placeholder':'CSREF 4'}),required=False )
    csref5 = forms.CharField(widget=forms.TextInput({'class':"input-small 15 16 17 18 19 20 cs ",'placeholder':'CSREF 5'}),required=False )
    csref6 = forms.CharField(widget=forms.TextInput({'class':"input-small 16 17 18 19 20 cs",'placeholder':'CSREF 6'}),required=False )
    csref7 = forms.CharField(widget=forms.TextInput({'class':"input-small 17 18 19 20 cs",'placeholder':'CSREF 7'}),required=False )
    csref8 = forms.CharField(widget=forms.TextInput({'class':"input-small 18 19 20 cs",'placeholder':'CSREF 8'}),required=False )
    csref9 = forms.CharField(widget=forms.TextInput({'class':"input-small 19 20 cs",'placeholder':'CSREF 9'}),required=False )
    csref10 = forms.CharField(widget=forms.TextInput({'class':"input-small 20 cs",'placeholder':'CSREF 10'}),required=False )

    class Meta:
        model = RefCustomer
        fields ='__all__'
