#from django.http import HttpResponse
from django.views.generic import TemplateView
from config.views import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):

        context = super(Dashboard, self).get_context_data(**kwargs)

        return context

