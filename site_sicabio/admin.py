from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission

from .models import *


admin.site.register(Profissional)
admin.site.register(Permission)
class ProfAdmin(admin.ModelAdmin):
    list_display = ['id','nome','especialidade']

admin.site.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['id','nome']

admin.site.register(ImpressaoDigital)
class ImpAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(MaoEsquerda)
class MeAdmin(admin.ModelAdmin):
    list_display = ['nome_dedo','padrao']

admin.site.register(MaoDireita)
class MdAdmin(admin.ModelAdmin):
    list_display = ['nome_dedo','padrao']

admin.site.register(Padrao)
class PadraoAdmin(admin.ModelAdmin):
    list_display = ['id','padrao']

admin.site.register(Analise)
class AnaliseAdmin(admin.ModelAdmin):
    list_display = ['id','paciente']

admin.site.register(Potencialidade)
class PotencialidadeAdmin(admin.ModelAdmin):
    list_display = ['id']