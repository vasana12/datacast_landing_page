from django import forms
from django.db import models
from .models import Boards
from .models import Datacast_request
from .models import Review_product
from .models import Review_search_task
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
        """A form for creating new users. Includes all the required
        fields, plus a repeated password."""
        password1 = forms.CharField(label='패스워드', widget=forms.PasswordInput)
        password2 = forms.CharField(label='패드워드 확인', widget=forms.PasswordInput)

        class Meta:
            model = get_user_model()
            fields = ('username', 'nickname','password1','password2')

        def clean_password2(self):
            # Check that the two password entries match
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise ValidationError("Passwords don't match")
            return password2

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super(UserCreationForm, self).save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            user.is_superuser = 0
            user.is_active = 0
            user.is_staff = 0
            if commit:
                user.save()
            return user
#
# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['username','nickname']
#     def clean_username(self):
#         username = self.cleaned_data["username"]
#         try:
#             get_user_model().objects.get(username=username)
#         except get_user_model().DoesNotExist:
#             return username
#         raise forms.ValidationError(self.error_messages['duplicate_username'])
#
class review_search_task_form(forms.ModelForm):
    model = Review_search_task
    fields = ['user','search_keyword']

class BoardsCreateForm(forms.ModelForm):
    # keyword = forms.CharField(error_messages={'required': 'This field is required'})
    # channel = forms.CharField()
    # period = forms.DateField(input_formats=['%Y-%m-%d'], error_messages={'required':'%Y-%m-%d'})

    class Meta:
        model = Boards
        fields = ['keywordA','channel','periodStartA','periodEndA']