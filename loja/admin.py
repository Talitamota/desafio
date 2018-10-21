from django.contrib import admin

from loja.models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('atributos', 'criado_em', 'modificado_em')


admin.site.register(Produto, ProdutoAdmin)
