from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Email-cím',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'írja ide az E-mail-címét'})
    )
    username = forms.CharField(
        label='Felhasználónév',
        required=True,
        help_text="Nem tartalmazhat speciális szimbólumokat, csak kis és nagybetűt és számokat!",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Felhasználónév'})
    )
    password1 = forms.CharField(
        label='Jelszó',
        required=True,
        help_text="Ajánlott minimum 8 karakter, kis és nagy betű, szám, speciális szimbólum pl.: $, @, >.",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Jelszó'})
    )
    password2 = forms.CharField(
        label='Jelszó megerősítése',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Jelszó újra'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email-cím',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'írja ide az E-mail-címét'})
    )
    username = forms.CharField(
        label='Felhasználónév',
        required=True,
        help_text="Nem tartalmazhat speciális szimbólumokat, csak kis és nagybetűt és számokat!",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Felhasználónév'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Fénykép feltöltése',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
