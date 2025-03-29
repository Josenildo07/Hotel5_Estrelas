from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
from .models import Cliente, Quarto, Reserva, Despesa, Receita, Servico
from .forms import ClienteForm, QuartoForm, ReservaForm, DespesaForm, ReceitaForm, ServicoForm,  UserRegistrationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard') # redireciona para o dashbord após login
    return render(request, 'pdv/login.html')

def logout_view(request):
    logout(request)
    return redirect('login') # Redireciona para a pagina de login após logout



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'pdv/register.html', {'form': form})




@login_required
def dashboard(request):
    return render(request, 'pdv/dashboard.html')



@login_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'pdv/criar_cliente.html', {'form': form})

@login_required
def clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'pdv/clientes.html', {'clientes': clientes})



@login_required
def criar_quarto(request):
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quartos')
    else:
        form = QuartoForm()
    return render(request, 'pdv/criar_quarto.html', {'form': form})  

@login_required
def quartos_view(request):
    quartos = Quarto.objects.all()
    return render(request, 'pdv/quartos.html', {'quartos': quartos})



@login_required
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm()
    return render(request, 'pdv/criar_reserva.html', {'form': form})  

@login_required
def reservas_view(request):
    reservas = Reserva.objects.all()
    return render(request, 'pdv/reservas.html', {'reservas': reservas})



@login_required
def criar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('despesas')
    else:
        form = DespesaForm()
    return render(request, 'pdv/criar_despesa.html', {'form': form})  

@login_required
def despesas_view(request):
    despesas = Despesa.objects.all()
    return render(request, 'pdv/despesas.html', {'despesas': despesas})



@login_required
def criar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receitas')
    else:
        form = ReceitaForm()
    return render(request, 'pdv/criar_receita.html', {'form': form})  

@login_required
def receitas_view(request):
    receitas = Receita.objects.all()
    return render(request, 'pdv/receitas.html', {'receitas': receitas})



@login_required
def criar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicos')
    else:
        form = ServicoForm()
    return render(request, 'pdv/criar_servico.html', {'form': form})

@login_required
def servicos_view(request):
    servicos = Servico.objects.all()
    return render(request, 'pdv/servicos.html', {'servicos': servicos})



@login_required
def relatorios_view(request):
    reservas = Reserva.objects.all()
    total_vendas = sum(reserva.servico.preco for reserva in reservas if reserva.servico)

    return render(request, 'pdv/relatorios.html', {'reservas': reservas, 'total_vendas': total_vendas})