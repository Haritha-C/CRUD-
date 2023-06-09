from django.shortcuts import render, redirect,get_object_or_404
from crudapp.models import Task

# Create your views here.

def index(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        name=request.POST.get('name','')
        desc=request.POST.get('desc','')
        task=Task(slno=slno,name=name,desc=desc)
        task.save();
    return render(request,'home.html',{'task':task1})



def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        task.slno = request.POST.get('slno')
        task.name = request.POST.get('name')
        task.desc = request.POST.get('desc')
        task.save()
        return redirect('/')
    return render(request, 'update.html',{'var':task})




