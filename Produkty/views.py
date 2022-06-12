from django.http import HttpResponse
from django.shortcuts import render
from .models import Produkty, Kategoria
from django.shortcuts import render


def index(request):
    wszystkie = Produkty.objects.all()
    jeden = Produkty.objects.get(pk=2)
    kat = Produkty.objects.filter(kategoria=1)
    kat_name = Kategoria.objects.get(id=2)
    kategorie = Kategoria.objects.all()
    zawiera = Produkty.objects.filter(opis__icontains='nawilża')
    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)

"""
    context = {'wszystkie': wszystkie,
               'kategorie': kategorie}
    return render(request, 'szablon.html', context)"""

def kategoria (request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)

def produkt (rquest, id):
    produkt_user = Produkty.objects.get(pk=id)
    napis = "<h1>" + str(produkt_user) + "</h1>" + \
        "<p>" + str(produkt_user.opis) + "</p>" + \
        "<p>" + str(produkt_user.cena) + "</p>"
    return HttpResponse(napis)