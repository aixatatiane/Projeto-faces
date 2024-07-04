from django.shortcuts import render

def index(request):
    return render(request, 'core/pages/index.html')

def faces(request):
    return render(request, 'core/pages/faces.html')

def reflexao(request):
    return render(request, 'core/pages/reflexao.html')

def participantes(request):
    return render(request, 'core/pages/participantes.html')

def benvindo(request):
    return render(request, 'core/pages/benvindo.html')
