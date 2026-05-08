from django.contrib import admin
from .models import (
    Campus, Modalidade, Etapa, Jogador, Campeonato,
    Inscricao, Jogo, Medico, Consulta, Atendimento,
    Paciente, Especialidade
)

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sequencia', 'quantidade_jogos']
    search_fields = ['nome']
    ordering = ['sequencia']

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'id_jogador', 'campus', 'cadastrado_em']
    search_fields = ['nome', 'id_jogador']
    list_filter = ['campus', 'cadastrado_em']

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'campus', 'data', 'data_inscricao']
    search_fields = ['nome']
    list_filter = ['campus', 'data']
    filter_horizontal = ['modalidades']

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ['nome_time', 'campeonato', 'modalidade', 'confirmada', 'inscrito_em']
    search_fields = ['nome_time']
    list_filter = ['campeonato', 'modalidade', 'confirmada']
    filter_horizontal = ['jogadores']

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_1', 'time_2', 'data_hora', 'etapa', 'modalidade']
    search_fields = ['time_1__nome_time', 'time_2__nome_time']
    list_filter = ['etapa', 'modalidade', 'data_hora']

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario']
    search_fields = ['nome']

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'medico', 'data', 'criado_em']
    search_fields = ['paciente__nome', 'medico__nome']
    list_filter = ['medico', 'data']

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'consulta', 'realizado', 'realizado_em']
    search_fields = ['consulta__id']
    list_filter = ['realizado', 'realizado_em']

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'id_jogador', 'campus']
    search_fields = ['nome', 'id_jogador']
    list_filter = ['campus']

@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

