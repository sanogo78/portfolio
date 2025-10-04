from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request, 'profil/accueil.html')
def diplome(request):
    return render(request, 'profil/diplome.html')
def parcours(request):
    return render(request, 'profil/parcour.html')
def stage(request):
    return render(request, 'profil/stage.html')
def certificat(request):
    return render(request, 'profil/certif.html')
def competence(request):
    return render(request, 'profil/comp.html')
