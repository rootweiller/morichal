from django.views.generic import TemplateView, FormView, RedirectView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from .forms import LoginForm


class Landing(TemplateView):

    template_name = 'landing/landing.html'

    def get_context_data(self, **kwargs):

        context = super(Landing, self).get_context_data(**kwargs)

        return context


class LoginUser(FormView):

    template_name = 'landing/login.html'

    form_class = LoginForm

    success_url = "/d/Dashboard"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated():

            return HttpResponseRedirect(self.get_success_url())

        else:

            return super(LoginUser, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        login(self.request, form.get_user())

        return super(LoginUser, self).form_valid(form)


class Logout(RedirectView):

    pattern_name = 'Dashboard'

    def get(self, request, *args, **kwargs):

        logout(request)

        return super(Logout, self).get(self, *args, **kwargs)


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated():

            return HttpResponseRedirect(reverse('Landing'))

        else:

            return super(LoginRequiredMixin, self).dispatch(
                request, *args, **kwargs)