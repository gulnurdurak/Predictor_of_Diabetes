"""pod2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path
from pod2 import views

urlpatterns = [
    re_path(r'^$', views.login_redirect, name='login_redirect'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^account/', include('accounts.urls', namespace='account')),
    re_path(r'^results/', include('results.urls', namespace='result')),
    re_path(r'^doctor/', include('doctor.urls', namespace='doctor')),
    re_path(r'^predictions/', include('predict.urls', namespace='predict')),
    re_path(r'^', include('django.contrib.auth.urls')),
]
