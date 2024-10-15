from django import forms
class userform(forms.Form):
    num1 = forms.CharField(label= "value1", widget=forms.Textarea(attrs={'class':"form-control"}))
    num2 = forms.CharField(label="value2",widget=forms.Textarea(attrs={'class':"form-controls"}))
    