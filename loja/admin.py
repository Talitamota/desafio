from django.contrib import admin

from loja.models import Produto, Foto, Loja, Pesquisa


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('atributos', 'criado_em', 'modificado_em')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Foto)
admin.site.register(Loja)
admin.site.register(Pesquisa)
