from django.urls import path

from . import views

app_name = 'loja'

urlpatterns = [
    path('',views.LojaListView.as_view(), name='list'),
    path('<int:loja_id>/', views.LojaDetailView.as_view(), name='detail'),

]
