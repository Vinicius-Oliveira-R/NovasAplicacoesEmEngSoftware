from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from .models import (
    Campus, Modalidade, Etapa, Jogador, Campeonato,
    Inscricao, Jogo, Medico, Consulta, Atendimento
)
from .forms import (
    CampusForm, ModalidadeForm, EtapaForm, JogadorForm, CampeonatoForm,
    InscricaoForm, JogoForm, MedicoForm, ConsultaForm, AtendimentoForm
)


# ==================== CAMPUS VIEWS ====================
class CampusListView(ListView):
    model = Campus
    template_name = 'campeonato/campus_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Campus'
        return context


class CampusCreateView(SuccessMessageMixin, CreateView):
    model = Campus
    form_class = CampusForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('campus-list')
    success_message = "Campus criado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Campus'
        context['form_title'] = 'Novo Campus'
        return context


class CampusDetailView(DetailView):
    model = Campus
    template_name = 'campeonato/detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Campus - {self.object.nome}'
        return context


class CampusUpdateView(SuccessMessageMixin, UpdateView):
    model = Campus
    form_class = CampusForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('campus-list')
    success_message = "Campus atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Campus'
        context['form_title'] = f'Editar {self.object.nome}'
        return context


class CampusDeleteView(SuccessMessageMixin, DeleteView):
    model = Campus
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('campus-list')
    success_message = "Campus removido com sucesso!"


# ==================== MODALIDADE VIEWS ====================
class ModalidadeListView(ListView):
    model = Modalidade
    template_name = 'campeonato/modalidade_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Modalidades'
        return context


class ModalidadeCreateView(SuccessMessageMixin, CreateView):
    model = Modalidade
    form_class = ModalidadeForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('modalidade-list')
    success_message = "Modalidade criada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Modalidade'
        context['form_title'] = 'Nova Modalidade'
        return context


class ModalidadeDetailView(DetailView):
    model = Modalidade
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Modalidade - {self.object.nome}'
        return context


class ModalidadeUpdateView(SuccessMessageMixin, UpdateView):
    model = Modalidade
    form_class = ModalidadeForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('modalidade-list')
    success_message = "Modalidade atualizada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Modalidade'
        context['form_title'] = f'Editar {self.object.nome}'
        return context


class ModalidadeDeleteView(SuccessMessageMixin, DeleteView):
    model = Modalidade
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('modalidade-list')
    success_message = "Modalidade removida com sucesso!"


# ==================== ETAPA VIEWS ====================
class EtapaListView(ListView):
    model = Etapa
    template_name = 'campeonato/etapa_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Etapas'
        return context


class EtapaCreateView(SuccessMessageMixin, CreateView):
    model = Etapa
    form_class = EtapaForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('etapa-list')
    success_message = "Etapa criada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Etapa'
        context['form_title'] = 'Nova Etapa'
        return context


class EtapaDetailView(DetailView):
    model = Etapa
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Etapa - {self.object.nome}'
        return context


class EtapaUpdateView(SuccessMessageMixin, UpdateView):
    model = Etapa
    form_class = EtapaForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('etapa-list')
    success_message = "Etapa atualizada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Etapa'
        context['form_title'] = f'Editar {self.object.nome}'
        return context


class EtapaDeleteView(SuccessMessageMixin, DeleteView):
    model = Etapa
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('etapa-list')
    success_message = "Etapa removida com sucesso!"


# ==================== JOGADOR VIEWS ====================
class JogadorListView(ListView):
    model = Jogador
    template_name = 'campeonato/jogador_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Jogadores'
        return context


class JogadorCreateView(SuccessMessageMixin, CreateView):
    model = Jogador
    form_class = JogadorForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('jogador-list')
    success_message = "Jogador criado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Jogador'
        context['form_title'] = 'Novo Jogador'
        return context


class JogadorDetailView(DetailView):
    model = Jogador
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Jogador - {self.object.nome}'
        return context


class JogadorUpdateView(SuccessMessageMixin, UpdateView):
    model = Jogador
    form_class = JogadorForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('jogador-list')
    success_message = "Jogador atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Jogador'
        context['form_title'] = f'Editar {self.object.nome}'
        return context


class JogadorDeleteView(SuccessMessageMixin, DeleteView):
    model = Jogador
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('jogador-list')
    success_message = "Jogador removido com sucesso!"


# ==================== CAMPEONATO VIEWS ====================
class CampeonatoListView(ListView):
    model = Campeonato
    template_name = 'campeonato/campeonato_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Campeonatos'
        return context


class CampeonatoCreateView(SuccessMessageMixin, CreateView):
    model = Campeonato
    form_class = CampeonatoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('campeonato-list')
    success_message = "Campeonato criado com sucesso!"

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Campeonato'
        context['form_title'] = 'Novo Campeonato'
        return context


class CampeonatoDetailView(DetailView):
    model = Campeonato
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Campeonato - {self.object.nome}'
        context['inscricoes'] = Inscricao.objects.filter(campeonato=self.object)
        return context


class CampeonatoUpdateView(SuccessMessageMixin, UpdateView):
    model = Campeonato
    form_class = CampeonatoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('campeonato-list')
    success_message = "Campeonato atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Campeonato'
        context['form_title'] = f'Editar {self.object.nome}'
        return context


class CampeonatoDeleteView(SuccessMessageMixin, DeleteView):
    model = Campeonato
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('campeonato-list')
    success_message = "Campeonato removido com sucesso!"


# ==================== INSCRICAO VIEWS ====================
class InscricaoListView(ListView):
    model = Inscricao
    template_name = 'campeonato/inscricao_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Inscrições'
        return context


class InscricaoCreateView(SuccessMessageMixin, CreateView):
    model = Inscricao
    form_class = InscricaoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('inscricao-list')
    success_message = "Inscrição criada com sucesso!"

    def form_valid(self, form):
        form.instance.inscrito_por = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Inscrição'
        context['form_title'] = 'Nova Inscrição'
        return context


class InscricaoDetailView(DetailView):
    model = Inscricao
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Inscrição - {self.object.nome_time}'
        return context


class InscricaoUpdateView(SuccessMessageMixin, UpdateView):
    model = Inscricao
    form_class = InscricaoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('inscricao-list')
    success_message = "Inscrição atualizada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Inscrição'
        context['form_title'] = f'Editar {self.object.nome_time}'
        return context


class InscricaoDeleteView(SuccessMessageMixin, DeleteView):
    model = Inscricao
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('inscricao-list')
    success_message = "Inscrição removida com sucesso!"


# ==================== JOGO VIEWS ====================
class JogoListView(ListView):
    model = Jogo
    template_name = 'campeonato/jogo_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Jogos'
        return context


class JogoCreateView(SuccessMessageMixin, CreateView):
    model = Jogo
    form_class = JogoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('jogo-list')
    success_message = "Jogo criado com sucesso!"

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Jogo'
        context['form_title'] = 'Novo Jogo'
        return context


class JogoDetailView(DetailView):
    model = Jogo
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Jogo #{self.object.pk}'
        return context


class JogoUpdateView(SuccessMessageMixin, UpdateView):
    model = Jogo
    form_class = JogoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('jogo-list')
    success_message = "Jogo atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Jogo'
        context['form_title'] = f'Editar Jogo #{self.object.pk}'
        return context


class JogoDeleteView(SuccessMessageMixin, DeleteView):
    model = Jogo
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('jogo-list')
    success_message = "Jogo removido com sucesso!"


# ==================== MEDICO VIEWS ====================
class MedicoListView(ListView):
    model = Medico
    template_name = 'campeonato/medico_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Médicos'
        return context


class MedicoCreateView(SuccessMessageMixin, CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('medico-list')
    success_message = "Médico criado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Médico'
        context['form_title'] = 'Novo Médico'
        return context


class MedicoDetailView(DetailView):
    model = Medico
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Médico - {self.object.nome}'
        return context


class MedicoUpdateView(SuccessMessageMixin, UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('medico-list')
    success_message = "Médico atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Médico'
        context['form_title'] = f'Editar {self.object.nome}'
        return context


class MedicoDeleteView(SuccessMessageMixin, DeleteView):
    model = Medico
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('medico-list')
    success_message = "Médico removido com sucesso!"


# ==================== CONSULTA VIEWS ====================
class ConsultaListView(ListView):
    model = Consulta
    template_name = 'campeonato/consulta_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Consultas'
        return context


class ConsultaCreateView(SuccessMessageMixin, CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('consulta-list')
    success_message = "Consulta criada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Consulta'
        context['form_title'] = 'Nova Consulta'
        return context


class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Consulta #{self.object.pk}'
        return context


class ConsultaUpdateView(SuccessMessageMixin, UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('consulta-list')
    success_message = "Consulta atualizada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Consulta'
        context['form_title'] = f'Editar Consulta #{self.object.pk}'
        return context


class ConsultaDeleteView(SuccessMessageMixin, DeleteView):
    model = Consulta
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('consulta-list')
    success_message = "Consulta removida com sucesso!"


# ==================== ATENDIMENTO VIEWS ====================
class AtendimentoListView(ListView):
    model = Atendimento
    template_name = 'campeonato/atendimento_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Atendimentos'
        return context


class AtendimentoCreateView(SuccessMessageMixin, CreateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('atendimento-list')
    success_message = "Atendimento criado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Atendimento'
        context['form_title'] = 'Novo Atendimento'
        return context


class AtendimentoDetailView(DetailView):
    model = Atendimento
    template_name = 'campeonato/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Atendimento #{self.object.pk}'
        return context


class AtendimentoUpdateView(SuccessMessageMixin, UpdateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('atendimento-list')
    success_message = "Atendimento atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Atendimento'
        context['form_title'] = f'Editar Atendimento #{self.object.pk}'
        return context


class AtendimentoDeleteView(SuccessMessageMixin, DeleteView):
    model = Atendimento
    template_name = 'campeonato/confirm_delete.html'
    success_url = reverse_lazy('atendimento-list')
    success_message = "Atendimento removido com sucesso!"

