from django.core import serializers
from django.http import HttpResponse
from oauth2_provider.admin import AccessToken
from oauth2_provider.views import ProtectedResourceView

from users.models import Teachers, Students


class TeacherAPI(ProtectedResourceView):

    def get(self, request, *args, **kwargs):

        token = request.META['HTTP_AUTHORIZATION']

        t = token.split(' ')[1]

        token_user = AccessToken.objects.get(token=t)

        if token:
            query = {}
            if self.request.GET.get("teachers") == "all":
                query["teachers"] = self.request.GET.get("all")
                teachers = Teachers.objects.filter(user=token_user.id)
                data = serializers.serialize('json', teachers)

                return HttpResponse(data, status=200)

            else:
                return HttpResponse("parameters inconrrect", status=404)
        else:

            return HttpResponse('No token', status=404)


class StudentsAPI(ProtectedResourceView):

    def get(self, request, *args, **kwargs):

        students = Students.objects.all()
        data = serializers.serialize('json', students)

        return HttpResponse(data, status=200)