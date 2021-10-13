from django import forms 

class RegisterUser(forms.Form):
    attrs={
        "type":"password"
    }
    name=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Your Name'}))
    email=forms.EmailField(label=False,widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password=forms.CharField(label=False,widget=forms.TextInput(attrs={'type': 'password' , 'placeholder': 'password'}))
    # password=forms.CharField(widget=forms.TextInput(attrs=attrs))

class Contact(forms.Form):
    phone=forms.IntegerField()
    name=forms.CharField()
    msg=forms.CharField()