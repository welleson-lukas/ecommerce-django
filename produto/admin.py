from django.contrib import admin
from .models import Produto, Variacao

class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_preco_formatado', 'get_preco_promocional_formatado', 'slug']
    inlines = [
        VariacaoInLine
    ]

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)