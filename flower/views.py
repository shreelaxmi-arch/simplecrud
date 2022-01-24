


from tkinter import E
from django.shortcuts import render,HttpResponse,redirect
#loading StudentForm from form.py inside students app
#from app_name.form import ModelForm_name
from flower.form import FlowerForm
from flower.models import Flower
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def index(request):
    if request.method=="POST":
        form=FlowerForm(request.POST)
        if form.is_valid():
            form.save()#persist data in database, using queryset(Django ORM API) method ==> create
            return redirect('../show')
            #return render(request,'show.html',{'form':form})
        else:
            pass
    else:
        obj=FlowerForm()
        return render(request,'index.html',{'stu':obj}) #HTTP GET Method for displaying an empty form
        
def show(request):  
        flowers = Flower.objects.all()  #similar to select * from student
        return render(request,"show.html",{'stu_list':flowers})  


#just display a form with filled fields
def edit(request, id):  
        stu = Flower.objects.get(id=id)  
        return render(request,'edit.html', {'stu':stu})

def update(request, id):  
        stu =Flower.objects.get(id=id)  
        form=FlowerForm(request.POST, instance = stu)  
        if form.is_valid():  
            form.save()  
            return redirect("../show")
            #return render(request,'show.html')
        return render(request, 'edit.html', {'stu': stu})  

def destroy(request, id):  
    stu=Flower.objects.get(id=id)  
    stu.delete() 
    return redirect("../show") 
    #return render(request,'show.html')

def new_func():
    return redirect('show')
    
    
def upload(request):
    obj=FlowerForm()
    return render(request,'upload.html',{'stu':obj})

