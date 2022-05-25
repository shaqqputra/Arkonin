from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 
        'first_name', 
        'last_name', 
        'email', 
        'password1', 
        'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            email = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This Email Address Already In Use.')

        

    def init(self, args, **kwargs):
            super(SignUpForm, self).init(args, **kwargs)

            self.fields['username']
            self.fields['password1']
            self.fields['password2']