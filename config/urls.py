from django.conf.urls import *

from .views import LoginUser, Logout, Landing

urlpatterns = [
    url(r'^$', Landing.as_view(), name='Landing'),
    url(r'^loginuser/', LoginUser.as_view(), name='LoginUser'),
    url(r'^logout/', Logout.as_view(), name='Logout'),
    #url('', include('social.apps.django_app.urls', namespace='social')),
]