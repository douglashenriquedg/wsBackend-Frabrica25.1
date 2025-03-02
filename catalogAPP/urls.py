from django.urls import path
from .views import FilmeListView, FilmeCreateView, FilmeUpdateView, FilmeDeleteView, index

urlpatterns = [
    path('', index, name='index'), 
    path('filme/', FilmeListView.as_view(), name='filme-list'),
    path('adicionar/', FilmeCreateView.as_view(), name='filme-create'),
    path('editar<int:pk>/', FilmeUpdateView.as_view(), name='filme-update'),
    path('excluir<int:pk>/', FilmeDeleteView.as_view(), name='filme-delete'),
]
