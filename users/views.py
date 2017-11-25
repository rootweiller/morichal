from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView

from rest_framework import viewsets

from users.forms import StudentsAddForm
from .serializers import TeachersSerializers, StundentsSerializers
from .models import Teachers, Students


class Teachers(viewsets.ModelViewSet):

    serializer_class = TeachersSerializers

    model = Teachers

    queryset = model.objects.all()

    def filter_queryset(self, queryset):

        return self.queryset

    def filter_queryset(self, queryset):

        query = {}

        if self.request.GET.get('document_number'):
            query['document_number'] = self.request.GET.get('document_number')
        if self.request.GET.get('document_type'):
            query['docuemnt_type'] = self.request.GET.get('document_type')

        return self.model.objects.filter(**query)

        return self.queryset


class Students(viewsets.ModelViewSet):

    serializer_class = StundentsSerializers
    model = Students
    queryset = model.objects.all()

    def filter_queryset(self, queryset):

        query = {}

        if self.request.GET.get('document_number'):
            query['document_number'] = self.request.GET.get('document_number')
        if self.request.GET.get('document_type'):
            query['docuemnt_type'] = self.request.GET.get('document_type')

        return self.model.objects.filter(**query)

        return self.queryset


class StudentsAddFrontend(FormView):

    template_name = 'students/frontend/add.html'

    form_class = StudentsAddForm

    success_url = '/dashboard'

    def post(self, request, *args, **kwargs):

        form_class = self.get_form_class()

        form = self.get_form(form_class)

        if form.is_valid():

            return self.form_valid(form, **kwargs)

        else:

            return self.form_invalid(form, **kwargs)

    def form_invalid(self, form, **kwargs):

        context = self.get_context_data(form=form)

        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):

        context = self.get_context_data(**kwargs)

        context['form'] = form

        form.save()

        return HttpResponseRedirect(self.get_success_url())