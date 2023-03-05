from django.db import models

# Create your models here.
class kontakt(models.Model):
    name = models.CharField(verbose_name("Name"), max_length=250)
    tele = models.CharField(verbose_name("Telefon"), max_length=50)
    mail = models.CharField(verbose_name("E-Mail"), max_length=50)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Kontakte"
        verbose_name = "Kontakt"
        ordering = ['name']
    