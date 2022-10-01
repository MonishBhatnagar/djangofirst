from wsgiref.util import request_uri
from django.shortcuts import render,redirect,get_object_or_404
from todo.forms import ContactForm, TodoForm
from todo.models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')  
@login_required
def service(request):
    return render(request,'service.html')
@login_required
def contact(request): 
    Contactform=ContactForm(request.POST or None)
    if Contactform.is_valid():
        Contactform.save()
        return redirect("home")

    return render(request,'contact.html',{'form':Contactform})
@login_required
def todoadd(request):
    todoform=TodoForm(request.POST or None)
    if todoform.is_valid():
        todoform.save()
        return redirect("todolist")


    return render(request,'todoadd.html',{'form':todoform})
@login_required
def todolist(request):
    allfeedback=Todo.objects.all()
    return render(request,'todolist.html',{'todos':allfeedback})
@login_required
def todoedit(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    todoform=TodoForm(request.POST or None,instance=todo)
    if todoform.is_valid():
        todoform.save()
        return redirect("todolist")  
    return render(request,'todoadd.html',{'form':todoform}) 
@login_required
def tododelete(request,pk):   
    todo=get_object_or_404(Todo,pk=pk)
    if request.method=='POST':
        todo.delete()
        return render('todolist')
    return render(request,'tododelete.html',{'todo':todo})

