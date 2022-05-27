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

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('This field is required')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError('This field is required')
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            username = User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError('This username Address Already In Use.')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            email = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This Email Address Already In Use.')


    def clean_password(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError(
                "Password Does Not Match"
            )

    def init(self, args, **kwargs):
            super(SignUpForm, self).init(args, **kwargs)

            self.fields['username']
            self.fields['password1']
            self.fields['password2']