from django.http import HttpResponse
from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):

        context = super(Dashboard, self).get_context_data(**kwargs)

        return context