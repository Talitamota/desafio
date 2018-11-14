from django.views.generic import ListView, DetailView, DeleteView

from django.shortcuts import get_object_or_404, render_to_response
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from loja.models import Loja


class LojaListView(ListView):
    model = Loja

    def get_queryset(self, **kwargs):
        return Loja.objects.all()

class LojaDeleteView(DeleteView):
    model = Loja
    success_url = reverse_lazy('loja:list')
    template_name = 'loja/loja_confirm_delete.html'

    def get(self, request, loja_id):
        loja = get_object_or_404(Loja, pk=loja_id)
        context = {'loja':loja}
        return self.render_to_response(context)

    def delete(self, request, loja_id):
        loja = get_object_or_404(Loja, pk=loja_id)
        loja.delete()
        return HttpResponseRedirect(self.success_url)

class LojaDetailView(DetailView):
    model = Loja

    template_name = 'loja/loja_detail.html'

    def get(self, request, loja_id):
        loja = get_object_or_404(Loja, pk=loja_id)
        context = {'loja':loja}
        return self.render_to_response(context)




'''
criar as seguintes views para o modelo Loja:
ListView
DeleteView
DetailView
CreateView

'''
