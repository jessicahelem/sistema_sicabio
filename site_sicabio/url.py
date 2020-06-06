from django.conf.urls import url

import site_sicabio
from site_sicabio import views

app_name = site_sicabio
urlpatterns = [
    url(r'^cadastro$',views.cadastrar_profissional,name='cadastro'),
]