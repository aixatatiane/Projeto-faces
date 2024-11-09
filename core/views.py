from django.shortcuts import render, get_object_or_404, redirect
from .models import Face
from .forms import FacesModelForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone

def index(request):
    faces = Face.objects.all()[:3]

    return render(request, 'core/pages/index.html', { 'faces': faces })

def faces(request):
    objetos = Face.objects.all()
    nome = request.GET.get('nome', '')

    if nome:
        objetos = objetos.filter(nome__icontains=nome)

    paginator = Paginator(objetos, 5)
    page_number = request.GET.get('page')
    faces = paginator.get_page(page_number)
    return render(request, 'core/pages/faces.html', { 'faces': faces })

def reflexao(request):
    return render(request, 'core/pages/reflexao.html')

def participantes(request):
    return render(request, 'core/pages/participantes.html')

def faces_detalhe(request, id):
    face = get_object_or_404(Face, id=id)
    context = {'face': face}
    return render(request, 'core/pages/faces-detalhe.html', context)

def cadastrar_face(request):
    if request.method == 'POST':
        form = FacesModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Face cadastrada com sucesso.')
            return redirect('core:home')
    else:
        form = FacesModelForm()
    
    return render(request, 'core/pages/form.html', {'form': form, 'acao': 'atualizar'})

def atualizar_face(request, id):
    face = get_object_or_404(Face, id=id)

    if request.method == 'POST':
        form = FacesModelForm(request.POST, request.FILES, instance=face)

        if form.is_valid():
            form.save()
            messages.success(request, 'Face atualizada com sucesso.')
            return redirect('core:home')
    else:
        if face.data_nascimento:
            face.data_nascimento = face.data_nascimento.strftime('%Y-%m-%d')
        if face.data_falecimento:
            face.data_falecimento = face.data_falecimento.strftime('%Y-%m-%d')
        
        form = FacesModelForm(instance=face)
    
    return render(request, 'core/pages/form.html', {'form': form, 'face': face, 'acao': 'atualizar'})

def deletar_face(request, id):
    face = get_object_or_404(Face, id=id)

    if request.method == 'POST':
        face.delete()
        messages.success(request, 'Face deletada com sucesso.')
        return redirect('core:home')
    
    return render(request, 'core/pages/deletar_face.html', {'face': face})
