from django.shortcuts import render

from site_sicabio.models import Profissional

def index(request):
    return render(request,'index.html',
                  {'profissionais':Profissional.objects.all()})