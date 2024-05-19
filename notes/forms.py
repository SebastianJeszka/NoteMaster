from django import forms
from .models import Notatka

# Klasa definiująca formularz Django, który pozwala użytkownikom wprowadzać dane dotyczące notatek
class NotatkaForm(forms.ModelForm):
    class Meta:
        model = Notatka
        fields = ['przedmiot', 'tytul', 'tresc']
