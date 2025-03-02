from django.shortcuts import render
from django.views.generic import ListView,  CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Filme
from .forms import FilmeForm
import requests
from .omdb_service import procurafilme


# Página inicial (index)
def index(request):
    busca = request.GET.get('filme', '')
    filme = None

    if busca:
        filme = procurafilme(busca)

    return render(request, 'index.html', {'filme': filme, 'busca': busca})

# crud de filmes
class FilmeListView(ListView):
    model = Filme
    template_name = 'filme_list.html' 
    context_object_name = 'filmes'  

class FilmeCreateView(FormView):
    template_name = 'filme_form.html'
    form_class = FilmeForm
    success_url = '/filme/'  

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)

class FilmeUpdateView(UpdateView):
    model = Filme
    template_name = 'filme_form.html'
    form_class = FilmeForm
    success_url = '/filme/'  

    def form_valid(self, form):
        filme = form.save(commit=False)     
        filme.save()                        
        return super().form_valid(form)

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme_confirm_delete.html'
    success_url = reverse_lazy('filme-list')        