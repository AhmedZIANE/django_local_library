from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    phone = forms.CharField(label='phone', max_length=100)
    message = forms.CharField(widget=forms.Textarea)