from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm, UsernameField, PasswordChangeForm, 
    password_validation, PasswordResetForm,
    SetPasswordForm
)

User = get_user_model()


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }),)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
            # 'bio',
            'password',
            
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        }
        
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password and confirm password is not same')
        return super().clean()

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()
        return user


class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=40, widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }))
    

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",
                'class': 'form-control',
                'placeholder': 'Email'
        }),
    )



class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True,
                'class': 'form-control',
                'placeholder': 'Old password'}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 
                'class': 'form-control',
                'placeholder': 'New Password',
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                'class': 'form-control',
                'placeholder': 'New password confirmation'
            }),
    )


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 
                'class': 'form-control',
                'placeholder': 'New Password',
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                'class': 'form-control',
                'placeholder': 'New password confirmation'
            }),
    )
        

