from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Produto
from .forms import ProdutoForm
import logging

logger = logging.getLogger('django')
level = logging.getLevelName('DEBUG')
logger.setLevel(level)

# Create your views here.

def home_view(request):
    logger.info(request)
    return render(request, 'home.html')

def novo_produto_view(request):
    context = {}
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    context['form'] = form
    return render(request, 'produto_formulario.html', {'form': form})

def listar_produtos_view(request):
    context = {}
    produtos = Produto.objects.all()
    context['produtos'] = produtos
    return render(request, "produto_lista.html", context)

def editar_produtos_view(request,id):
    context = {}
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    context['form'] = form
    return render(request, 'produto_formulario.html', {'form': form})

def deletar_produtos_view(request,id):
    context = {}
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        produto.delete()
        return redirect('lista_produtos')
    context['form'] = form
    return render(request, 'produto_formulario_deletar.html', {'form': form})