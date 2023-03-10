# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Profile


# class RegistrationForm(UserCreationForm):
#     idn_or_ssn = forms.IntegerField(label='ID card number')
#     is_elder = forms.BooleanField(required=False)
#     is_volunteer = forms.BooleanField(required=False)
#     location = forms.CharField(max_length=255)
#     bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), max_length=500, required=False)

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'idn_or_ssn', 'is_elder', 'is_volunteer', 'location', 'bio')


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('idn_or_ssn', 'is_elder', 'is_volunteer', 'location', 'bio', 'time_credits')
