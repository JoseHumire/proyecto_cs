from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth import password_validation
from django.forms import inlineformset_factory

from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]
        labels = {
            'email': 'Email address',
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Repeat Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last name'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Password confirmation'})


class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = [
            'city', 'phone', 'id_number', 'id_image',
            'status', 'birthdate', 'profile_picture',
        ]
        labels = {
            'city': 'City',
            'phone': 'Phone number',
            'id_number': 'ID Number',
            'status': 'Status',
            'birthdate': 'Birthdate'
        }
        widgets = {
            'city': forms.Select(
                attrs={'class': 'form-control select2bs4',
                       'placeholder': 'City',
                       'style': 'height:100%;'}
            ),
            'phone': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Phone number'}
            ),
            'id_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Identification document'}
            ),
            'status': forms.CheckboxInput(),
            'birthdate': forms.DateInput(
                attrs={'class': 'form-control datetimepicker-input'}),
            'id_image': forms.FileInput(
                attrs={'class': 'custom-file-input'}
            ),
            'profile_picture': forms.FileInput(
                attrs={'class': 'custom-file-input'}
            ),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'profession', 'description', 'start_date', 'finish_date'
        ]
        labels = {
            'profession': 'Profession',
            'description': 'Description',
            'start_date': 'Start Date',
            'finish_date': 'Finish Date',
        }
        widgets = {
            'profession': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'finish_date': forms.DateTimeInput(
                attrs={'class': 'form-control'}
            ),
        }


class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = [
            'school', 'profession', 'name', 'image'
        ]
        labels = {
            'school': 'Institution',
            'profession': 'Profession',
            'name': 'Degree',
        }
        widgets = {
            'school': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(
                attrs={'class': 'custom-file-input'}
            ),
        }


class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = ['city', 'description', 'status']
        labels = {
            'city': 'City',
            'description': 'Description',
            'status': 'Status',
        }
        widgets = {
            'city': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter description'}
            ),
        }


class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = ['profession', 'description', 'reward', 'status']
        labels = {
            'profession': 'Profession',
            'description': 'Description',
            'reward': 'Reward',
            'status': 'Status',
        }
        widgets = {
            'profession': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter description'}
            ),
            'reward': forms.TextInput(
                attrs={'class': 'form-control',
                       'type': 'number'}
            ),
        }


EmploymentInlineFormSet = inlineformset_factory(
    JobOffer, Employment, form=EmploymentForm, extra=2, can_delete=True
)


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )
        labels = {
            'email': 'Email address',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last name'}),
        }


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        )
    )


class UserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'form-control'}
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control'}
        ),
    )
