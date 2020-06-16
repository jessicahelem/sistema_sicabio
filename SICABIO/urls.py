"""SICABIO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin, staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path, include

from SICABIO import settings
from site_sicabio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('site_sicabio/all/',views.list_all_pacientes),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.do_login),
    path("logout/",views.logout_user),
    #path(r'',include('site_sicabio.url',namespace='site_sicabio')),
    path('login/submit',views.submit_login),
    path('menu_paciente/',views.menu_paciente),
    path('site_sicabio/cadastrar_paciente/',views.cadastrar_pac),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)