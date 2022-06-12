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
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'kategoria_produkt': kategoria_produkt,
            'kategorie': kategorie}
    return render(request, 'kategoria_produkt.html', dane)



def produkt (request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user': produkt_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)