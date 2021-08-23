from django.contrib.auth import get_user_model
from django import forms

from .models import Memory

User = get_user_model()


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['title', 'description']
