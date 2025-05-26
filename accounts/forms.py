from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    face_auth = forms.BooleanField(required=False, initial=False, label='Face Recognition')
    voice_auth = forms.BooleanField(required=False, initial=False, label='Voice Authentication')
    gesture_auth = forms.BooleanField(required=False, initial=False, label='Gesture Recognition')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'face_auth', 'voice_auth', 'gesture_auth', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email
