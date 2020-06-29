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
from django.views.generic import RedirectView

from SICABIO import settings
from site_sicabio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('site_sicabio/all_pacientes/',views.list_all_pacientes),
    path('site_sicabio/pacientes/',views.list_user),
    path('site_sicabio/consultas/',views.list_consulta),
    path('site_sicabio/detalhes/<id>/',views.pacientes_detalhes),
    path('site_sicabio/detalhes_consulta/<id>/',views.consulta_detalhes),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.do_login),
    path("logout/",views.logout_user),
    #path(r'',include('site_sicabio.url',namespace='site_sicabio')),
    path('login/submit',views.submit_login),
    path('menu_paciente/',views.menu_paciente),
    path('site_sicabio/cadastrar_paciente/',views.form_paciente),
    path('site_sicabio/detalhes/<id>/inserir_digital/',views.inserir_digital),
    path('site_sicabio/cadastrar_paciente/submit', views.set_paciente),
    path('site_sicabio/cadastrar_consulta/submit',views.set_consulta),
    path('site_sicabio/detalhes/<id>/inserir_digital/upload',views.cadastrar_digital),
    path('site_sicabio/delete/<id>/',views.delete_paciente),
    path('site_sicabio/delete_consulta/<id>/',views.delete_consulta),
    path('site_sicabio/detalhes/<id>/cadastrar_consulta/',views.form_consulta),
    path('site_sicabio/detalhes/<id>/cadastrar_consulta/submit',views.set_consulta),
    path('site_sicabio/detalhes_consulta/<id>/cadastrar_consulta/',views.form_consulta),
    path('site_sicabio/detalhes_consulta/<id>/cadastrar_consulta/submit',views.set_consulta),
    # path('site_sicabio/cadastrar_consulta/', views.form_consulta),
    # path('site_sicabio/detalhes_consulta/<id>/alterar_consulta/', views.form_consulta),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)