from django.contrib import admin
from . import models

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre_categoria',)}
    list_display = ('nombre_categoria', 'slug')

admin.site.register(models.Categoria, CategoryAdmin)