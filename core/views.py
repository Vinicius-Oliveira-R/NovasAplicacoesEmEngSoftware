from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


def index_view(request):
    """Index view - home page"""
    context = {
        'page_title': 'Home'
    }
    return render(request, 'core/index.html', context)


class SobreView(TemplateView):
    """About page view using template view"""
    template_name = 'core/sobre.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Sobre o Projeto'
        return context

