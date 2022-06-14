from django.db import models

# Create your models here.

class Producent(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)
    #blank True means it could be but it's not necessary

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"

class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Movies(models.Model):
    name = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to='Produkty/images')


class Produkty(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Movies, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"





