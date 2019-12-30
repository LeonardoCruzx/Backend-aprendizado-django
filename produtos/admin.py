from django.contrib import admin


from .models import *
# Register your models here.
@admin.register(ProdutoModel)
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    list_filter = ('category','price')
    filter_horizontal = ('category',)
    search_fields = ('name','price')

@admin.register(CategoriaModel)
class CategoriaModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)