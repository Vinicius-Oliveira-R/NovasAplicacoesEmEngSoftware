from django import forms
from django.forms import ModelForm
from .models import (
    Campus, Modalidade, Etapa, Jogador, Campeonato, 
    Inscricao, Jogo, Medico, Consulta, Atendimento
)


class CampusForm(ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do campus'
            })
        }


class ModalidadeForm(ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: LOL, CS, Fifa'
            })
        }


class EtapaForm(ModelForm):
    class Meta:
        model = Etapa
        fields = ['nome', 'sequencia', 'quantidade_jogos']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sequencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade_jogos': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class JogadorForm(ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'id_jogador', 'campus', 'usuario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'id_jogador': forms.TextInput(attrs={'class': 'form-control'}),
            'campus': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }


class CampeonatoForm(ModelForm):
    class Meta:
        model = Campeonato
        fields = ['nome', 'campus', 'data', 'data_inscricao', 'modalidades']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'campus': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'data_inscricao': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'modalidades': forms.CheckboxSelectMultiple(),
        }


class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome_time', 'jogadores', 'campeonato', 'modalidade', 'confirmada']
        widgets = {
            'nome_time': forms.TextInput(attrs={'class': 'form-control'}),
            'jogadores': forms.CheckboxSelectMultiple(),
            'campeonato': forms.Select(attrs={'class': 'form-control'}),
            'modalidade': forms.Select(attrs={'class': 'form-control'}),
            'confirmada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields = ['time_1', 'time_2', 'data_hora', 'etapa', 'modalidade', 'vencedor', 'resultado']
        widgets = {
            'time_1': forms.Select(attrs={'class': 'form-control'}),
            'time_2': forms.Select(attrs={'class': 'form-control'}),
            'data_hora': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'etapa': forms.Select(attrs={'class': 'form-control'}),
            'modalidade': forms.Select(attrs={'class': 'form-control'}),
            'vencedor': forms.Select(attrs={'class': 'form-control', 'required': False}),
            'resultado': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'usuario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control', 'required': False}),
        }


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class AtendimentoForm(ModelForm):
    class Meta:
        model = Atendimento
        fields = ['consulta', 'descricao', 'realizado']
        widgets = {
            'consulta': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'realizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

