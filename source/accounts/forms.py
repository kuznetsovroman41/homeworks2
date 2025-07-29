from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        first = cleaned_data.get("first_name")
        last = cleaned_data.get("last_name")

        if not first and not last:
            raise forms.ValidationError("Введите хотя бы имя или фамилию.")

        return cleaned_data
