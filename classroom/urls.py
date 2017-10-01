from django.conf.urls import url

from classroom.views import ClassRoom


classroom = ClassRoom.as_view({
    'get':'list',
    'post':'create'
})

urlpatterns = [
    url(r'^classroom/', classroom, name='classroom'),
    ]