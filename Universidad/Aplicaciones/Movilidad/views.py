from django.shortcuts import render
from .models import Aspirantes
# Create your views here.

def home(request):
    Aspiranteslistados = Aspirantes.objects.all()
    return render(request, "gestionAspirantes.html", {"Aspirant": Aspiranteslistados})