from django.urls import path
from . import views

urlpatterns = [
    # Campus URLs
    path('campus/', views.CampusListView.as_view(), name='campus-list'),
    path('campus/criar/', views.CampusCreateView.as_view(), name='campus-create'),
    path('campus/<int:pk>/', views.CampusDetailView.as_view(), name='campus-detail'),
    path('campus/<int:pk>/editar/', views.CampusUpdateView.as_view(), name='campus-update'),
    path('campus/<int:pk>/deletar/', views.CampusDeleteView.as_view(), name='campus-delete'),

    # Modalidade URLs
    path('modalidade/', views.ModalidadeListView.as_view(), name='modalidade-list'),
    path('modalidade/criar/', views.ModalidadeCreateView.as_view(), name='modalidade-create'),
    path('modalidade/<int:pk>/', views.ModalidadeDetailView.as_view(), name='modalidade-detail'),
    path('modalidade/<int:pk>/editar/', views.ModalidadeUpdateView.as_view(), name='modalidade-update'),
    path('modalidade/<int:pk>/deletar/', views.ModalidadeDeleteView.as_view(), name='modalidade-delete'),

    # Etapa URLs
    path('etapa/', views.EtapaListView.as_view(), name='etapa-list'),
    path('etapa/criar/', views.EtapaCreateView.as_view(), name='etapa-create'),
    path('etapa/<int:pk>/', views.EtapaDetailView.as_view(), name='etapa-detail'),
    path('etapa/<int:pk>/editar/', views.EtapaUpdateView.as_view(), name='etapa-update'),
    path('etapa/<int:pk>/deletar/', views.EtapaDeleteView.as_view(), name='etapa-delete'),

    # Jogador URLs
    path('jogador/', views.JogadorListView.as_view(), name='jogador-list'),
    path('jogador/criar/', views.JogadorCreateView.as_view(), name='jogador-create'),
    path('jogador/<int:pk>/', views.JogadorDetailView.as_view(), name='jogador-detail'),
    path('jogador/<int:pk>/editar/', views.JogadorUpdateView.as_view(), name='jogador-update'),
    path('jogador/<int:pk>/deletar/', views.JogadorDeleteView.as_view(), name='jogador-delete'),

    # Campeonato URLs
    path('', views.CampeonatoListView.as_view(), name='campeonato-list'),
    path('criar/', views.CampeonatoCreateView.as_view(), name='campeonato-create'),
    path('<int:pk>/', views.CampeonatoDetailView.as_view(), name='campeonato-detail'),
    path('<int:pk>/editar/', views.CampeonatoUpdateView.as_view(), name='campeonato-update'),
    path('<int:pk>/deletar/', views.CampeonatoDeleteView.as_view(), name='campeonato-delete'),

    # Inscricao URLs
    path('inscricao/', views.InscricaoListView.as_view(), name='inscricao-list'),
    path('inscricao/criar/', views.InscricaoCreateView.as_view(), name='inscricao-create'),
    path('inscricao/<int:pk>/', views.InscricaoDetailView.as_view(), name='inscricao-detail'),
    path('inscricao/<int:pk>/editar/', views.InscricaoUpdateView.as_view(), name='inscricao-update'),
    path('inscricao/<int:pk>/deletar/', views.InscricaoDeleteView.as_view(), name='inscricao-delete'),

    # Jogo URLs
    path('jogo/', views.JogoListView.as_view(), name='jogo-list'),
    path('jogo/criar/', views.JogoCreateView.as_view(), name='jogo-create'),
    path('jogo/<int:pk>/', views.JogoDetailView.as_view(), name='jogo-detail'),
    path('jogo/<int:pk>/editar/', views.JogoUpdateView.as_view(), name='jogo-update'),
    path('jogo/<int:pk>/deletar/', views.JogoDeleteView.as_view(), name='jogo-delete'),

    # Medico URLs
    path('medico/', views.MedicoListView.as_view(), name='medico-list'),
    path('medico/criar/', views.MedicoCreateView.as_view(), name='medico-create'),
    path('medico/<int:pk>/', views.MedicoDetailView.as_view(), name='medico-detail'),
    path('medico/<int:pk>/editar/', views.MedicoUpdateView.as_view(), name='medico-update'),
    path('medico/<int:pk>/deletar/', views.MedicoDeleteView.as_view(), name='medico-delete'),

    # Consulta URLs
    path('consulta/', views.ConsultaListView.as_view(), name='consulta-list'),
    path('consulta/criar/', views.ConsultaCreateView.as_view(), name='consulta-create'),
    path('consulta/<int:pk>/', views.ConsultaDetailView.as_view(), name='consulta-detail'),
    path('consulta/<int:pk>/editar/', views.ConsultaUpdateView.as_view(), name='consulta-update'),
    path('consulta/<int:pk>/deletar/', views.ConsultaDeleteView.as_view(), name='consulta-delete'),

    # Atendimento URLs
    path('atendimento/', views.AtendimentoListView.as_view(), name='atendimento-list'),
    path('atendimento/criar/', views.AtendimentoCreateView.as_view(), name='atendimento-create'),
    path('atendimento/<int:pk>/', views.AtendimentoDetailView.as_view(), name='atendimento-detail'),
    path('atendimento/<int:pk>/editar/', views.AtendimentoUpdateView.as_view(), name='atendimento-update'),
    path('atendimento/<int:pk>/deletar/', views.AtendimentoDeleteView.as_view(), name='atendimento-delete'),
]

