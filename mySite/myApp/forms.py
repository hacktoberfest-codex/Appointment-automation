from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    f_name = forms.CharField(max_length=20)
    l_name = forms.CharField(max_length=20)
    age = forms.IntegerField(required=True)
    # pic = forms.
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        
    
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        self.cleaned_data['email']
        if commit:
            user.save()
        return user

