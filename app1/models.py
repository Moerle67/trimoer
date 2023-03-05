from django.db import models
from django.urls import reverse

# Create your models here.
class Kontakt(models.Model):
    name = models.CharField(verbose_name="Name", max_length=250)
    tele = models.CharField(verbose_name="Telefon", max_length=50)
    mail = models.CharField(verbose_name="E-Mail", max_length=50)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Kontakte"
        verbose_name = "Kontakt"
        ordering = ['name']

class Geraeteklasse(models.Model):
    klasse = models.CharField(verbose_name="Geräteklasse", max_length=50)
    beschreibung = models.TextField(verbose_name="Beschreibung")
    details = models.TextField(verbose_name="Details", blank=True)
    def __str__(self):
        return f"{self.klasse}"
    class Meta:
        verbose_name_plural = "Geräteklassen"
        verbose_name = "Geräteklasse"
        ordering = ['klasse']

class Ticket(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    beschreibung = models.TextField(verbose_name="Beschreibung")
    klasse = models.ForeignKey(Geraeteklasse, verbose_name=("Geräteklasse"), on_delete=models.CASCADE)
    erstellt = models.DateTimeField(verbose_name="Erstellt", auto_now=False, auto_now_add=True)
    geaendert = models.DateTimeField(geaendert="", auto_now=True, auto_now_add=False)
    class Meta:
        verbose_name = ("Ticket")
        verbose_name_plural = ("Tickets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Ticket_detail", kwargs={"pk": self.pk})
