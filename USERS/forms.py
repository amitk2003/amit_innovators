# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# for eventform for user
from .models import Event
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'event_category', 'location', 'description', 'food_type', 'advance_payment_policy']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
