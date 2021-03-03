from django.core import paginator
from django.shortcuts import render, get_object_or_404,redirect
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def tasklist(request):

    search = request.GET.get('search')

    if search:
        
        tasks = Task.objects.filter(title__icontains=search)
    else: 

        #Faz select e ordena pela data de criacao
        tasks_list = Task.objects.all().order_by('-created_at')
        #Paginador, recebe a lista com os objetos e a quantidade de objetos por pagina
        paginator = Paginator(tasks_list, 3)
        #Pega a pagina atual da minha requisição
        page = request.GET.get('page')
        #Salva o paginador no objeto
        tasks = paginator.get_page(page)

    return render(request,'tasks/list.html', {'tasks':tasks})

@login_required
def taskView(request, id):
    #retorna meu item do banco ou uma pag 404, precisa de dois argumentos (Model e ID)
    task = get_object_or_404(Task,pk=id)
    return render(request,'tasks/task.html',{'task':task})


    #Metodo para imprimir um formulario. Ver Models.py, forms.py e addtask.html
@login_required
def newTask (request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            #Realiza o save do formulario no objeto task porém não faz commit automatico, aguarda até a próxima instrução
            task = form.save(commit=False)
            task.done = 'doing'
            #Agora sim grava no banco
            task.save()
            return redirect('/')

    form = TaskForm()
    return render(request,'tasks/addtask.html', {'form' : form})

@login_required
def editTask(request,id):
    task = get_object_or_404(Task,pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request,'tasks/edittask.html', {'form':form, 'task':task})
    else: 
        return render(request,'tasks/edittask.html', {'form':form, 'task':task})

@login_required
def deleteTask(request,id):
    task = get_object_or_404(Task,pk=id)
    task.delete()

    #Mensagem de retorno para o usuario (Ver HTML list.html)
    messages.info(request, 'Tarefa deletada com Sucesso')

    return redirect('/')

def yourname(request,name):
    return render(request, 'tasks/yourname.html', {'name':name})

