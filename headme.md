#Documentação do Projeto Django - CRUD de Filmes

'''📌 Visão Geral'''

Este projeto é um sistema de cadastro de filmes, onde é possível listar, adicionar, editar e excluir filmes. Além disso, há uma funcionalidade de busca de filmes utilizando um serviço externo.

📁 Estrutura do Projeto

📂 meu_projeto
│── 📂 app_filmes
│   │── 📄 urls.py
│   │── 📄 views.py
│   │── 📄 models.py
│   │── 📄 forms.py
│   │── 📂 templates
│   │── 📄 omdb_service.py
│── 📄 manage.py

urls.py: Define as rotas do aplicativo.

views.py: Contém as classes e funções para manipular as requisições HTTP.

models.py: Define a estrutura do banco de dados.

forms.py: Gerencia os formulários para inserção e edição de filmes.

templates/: Armazena os arquivos HTML para renderização.

omdb_service.py: Módulo externo para buscar informações de filmes.

'''🌍 URLs do Aplicativo (urls.py)'''

from django.urls import path
from .views import FilmeListView, FilmeCreateView, FilmeUpdateView, FilmeDeleteView, index

urlpatterns = [
    path('', index, name='index'),  # Página inicial
    path('filme/', FilmeListView.as_view(), name='filme-list'),  # Lista de filmes
    path('adicionar/', FilmeCreateView.as_view(), name='filme-create'),  # Adicionar filme
    path('editar/<int:pk>/', FilmeUpdateView.as_view(), name='filme-update'),  # Editar filme
    path('excluir/<int:pk>/', FilmeDeleteView.as_view(), name='filme-delete')  # Excluir filme
]

'''🔗 Rotas e Suas Funções'''

index: Página inicial com busca de filmes.

filme-list: Lista os filmes cadastrados.

filme-create: Formulário para adicionar um novo filme.

filme-update: Formulário para editar um filme existente.

filme-delete: Confirmação para excluir um filme.

'''🖥️ Views (views.py)'''

🔎 Função Index (Busca de Filmes)

def index(request):
    busca = request.GET.get('filme', '')
    filme = None
    if busca:
        filme = procurafilme(busca)
    return render(request, 'index.html', {'filme': filme, 'busca': busca})

Essa view permite buscar um filme em um serviço externo e exibir as informações na página inicial.

📝 CRUD de Filmes

📜 Listar Filmes

class FilmeListView(ListView):
    model = Filme
    template_name = 'filme_list.html'
    context_object_name = 'filmes'

Exibe a lista de filmes cadastrados no banco de dados.

'''➕ Criar um Novo Filme'''

class FilmeCreateView(FormView):
    template_name = 'filme_form.html'
    form_class = FilmeForm
    success_url = '/filme/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

Exibe o formulário para adicionar um novo filme e salva no banco de dados.

'''✏️ Editar um Filme'''

class FilmeUpdateView(UpdateView):
    model = Filme
    template_name = 'filme_form.html'
    form_class = FilmeForm
    success_url = '/filme/'

    def form_valid(self, form):
        filme = form.save(commit=False)
        filme.save()
        return super().form_valid(form)

Permite editar os detalhes de um filme existente.

'''🗑️ Excluir um Filme'''

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme_confirm_delete.html'
    success_url = reverse_lazy('filme-list')

Solicita confirmação antes de excluir um filme.

'''🛢️ Modelo do Banco de Dados (models.py)'''

from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=255)
    genero = models.CharField(max_length=255)
    duracao = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    ano = models.CharField(max_length=255)
    capa = models.ImageField(upload_to='capas/', default='default_capa.jpg')
    faixa_etaria_CHOICES = (
        ('L', 'Livre'), ('10', '10 anos'), ('12', '12 anos'), 
        ('14', '14 anos'), ('16', '16 anos'), ('18', '18 anos'),
    )
    faixa_etaria = models.CharField(max_length=2, choices=faixa_etaria_CHOICES)

    def __str__(self):
        return self.titulo


