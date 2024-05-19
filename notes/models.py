from django.db import models

# Klasa modelu tabeli przedmiot
class Przedmiot(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

# Klasa modelu tabeli notatka
class Notatka(models.Model):
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    przedmiot = models.ForeignKey(Przedmiot, on_delete=models.CASCADE)

    def __str__(self):
        return self.tytul
