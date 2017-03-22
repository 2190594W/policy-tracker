from django import forms
from django.contrib.auth.models import User
from policy_tracker_app.models import Country, Policy, Category, UserProfile

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), help_text="Please retype password")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={"class":"test"}),
        }

    def clean(self):
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError("The two passwords entered do not match.")
        cleaned_data = super(UserForm, self).clean()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class CountryForm(forms.ModelForm):
    name = forms.CharField(max_length=64, help_text="Please enter the country name.")
    inPower = forms.CharField(max_length=64, help_text="Please enter the governing body/ruler.")
    map_image_url = forms.CharField(disabled=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Country
        fields = ('name', 'inPower', 'description', 'background_image')
