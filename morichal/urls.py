"""morichal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

API_VERSION = '1.0'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Dashboard
    url(r'^d/', include('dashboard.urls')),

    # Config
    url(r'^', include('config.urls')),

    # Users
    url(r'^u/', include('users.urls')),

    # schools
    url(r'^c/', include('schools.urls')),

    # ClassRoom
    url(r'classroom/', include('classroom.urls')),

    url(r'^api/' + API_VERSION + '/a/', include('api.urls')),

    # OAuth
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
