from django.shortcuts import render, redirect
import random
from .forms import EntradaValoresForm
from .models import QUESTOES
from .forms import PessoaForm

def home_view(request):
    return render(request, 'burnout2_app/home.html')

def teste_view(request):
    return render(request, 'burnout2_app/teste.html')

def depoimentos_view(request):
    depoimentos = [
        {'texto': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
        {'texto': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'},
        {'texto': 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'}
        # Adicione mais depoimentos aqui
    ]

    if request.method == 'POST':
        depoimento_texto = request.POST.get('depoimento')
        if depoimento_texto:
            novo_depoimento = {'texto': depoimento_texto}
            depoimentos.append(novo_depoimento)
    elif request.method == 'GET':
        depoimento_remover = request.GET.get('remover')
        if depoimento_remover:
            depoimentos = [dep for dep in depoimentos if dep['texto'] != depoimento_remover]

    return render(request, 'burnout2_app/depoimentos.html', {'depoimentos': depoimentos})

def contatos_view(request):
    nomes = ['Dr. João Silva', 'Dra. Maria Santos', 'Dr. Pedro Oliveira', 'Dra. Ana Fernandes', 'Dr. Rafael Almeida', 'Dra. Camila Rodrigues', 'Dr. Lucas Santos', 'Dra. Fernanda Lima', 'Dr. André Silva', 'Dra. Julia Ferreira']
    contatos = []
    
    for nome in nomes:
        contato = {
            'nome': nome,
            'telefone': f'({random.randint(10, 99)}) {random.randint(1000, 9999)}-{random.randint(1000, 9999)}',
            'email': nome.lower().replace(' ', '.') + '@example.com',
            'endereco': f'Rua {random.choice("ABCDEFGHIJ")}, {random.randint(100, 999)} - {random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "Brasília", "Salvador", "Recife", "Belém", "Manaus"])}'
        }
        contatos.append(contato)
    
    return render(request, 'burnout2_app/contatos.html', {'contatos': contatos})

def excluir_depoimento(request, texto):
    # Lógica para excluir o depoimento com base no texto
    # Por exemplo, você pode usar um loop para procurar o depoimento com o texto correspondente
    # Após excluir, redirecione para a página de depoimentos
    depoimentos = [
        # ... lista de depoimentos com dicionários contendo texto e outras informações ...
    ]

    # Encontre e remova o depoimento com base no texto
    depoimento_removido = None
    for depoimento in depoimentos:
        if depoimento['texto'] == texto:
            depoimento_removido = depoimento
            depoimentos.remove(depoimento)
            break

    # Redirecione para a página de depoimentos
    return redirect('depoimentos')

def exibir_pagina_teste(request):
    form = EntradaValoresForm()

    if request.method == 'POST':
        form = EntradaValoresForm(request.POST)
        if form.is_valid():
            # Processar valores do formulário (entradas)
            respostas = []
            for i in range(len(QUESTOES)):
                resposta = request.POST.get(f'resposta_{i}')
                if resposta is not None:
                    respostas.append(int(resposta))
            
            media = sum(respostas) / len(respostas)
            return render(request, 'burnout2_app/resultado.html', {'media': media})

    questoes_enum = QUESTOES  # Remova 'enumerate' para manter o formato das questões
    return render(request, 'burnout2_app/teste.html', {'form': form, 'questoes_enum': questoes_enum})


def exibir_pagina_resultado(request):
    # Aqui você pode implementar a lógica para exibir o resultado com base na média
    # e também os botões "Muito bem", "Cuidado" e "Refazer"
    media = 0  # Substitua isso pela média real
    resultado = "Muito bem" if media <= 3 else "Cuidado"
    return render(request, 'burnout2_app/resultado.html', {'media': media, 'resultado': resultado})

from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import Pessoa

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'cadastro.html', {'form': form})

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'pessoas': pessoas})

def editar_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'editar.html', {'form': form})

def excluir_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('listar_pessoas')
