from django.contrib import admin
from .models import Produkty, Producent, Kategoria, Movies

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Produkty)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Movies, MovieAdmin)