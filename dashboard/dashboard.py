#from django.http import HttpResponse
from django.views.generic import TemplateView
from config.views import LoginRequiredMixin
from users.models import Teachers, Students


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):

        context = super(Dashboard, self).get_context_data(**kwargs)

        context['teachers'] = Teachers.objects.filter(user=self.request.user)\
            .count()
        context['students'] = Students.objects.filter(user=self.request.user)\
            .count()

        return context

