from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import HomeworkForm, HomeworkForm2
from django.contrib import messages
from .models import Homework
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"index.html")



def about(request):
    return render(request,"about.html")



@login_required(login_url = "user:login")
def dashboard(request):
    if request.user.is_superuser == 1:

        homeworks = Homework.objects.all()
        context = {
            "homeworks" : homeworks
        }
        return render(request,"dashboard.html",context)
    else:
        messages.info(request,"Bu URL ye Giriş Hakkınız Yoktur!!!")
        return redirect("index")


@login_required(login_url = "user:login")
def detail(request,id):
    homework = get_object_or_404(Homework, id = id)
    
    context = {
        "homework" : homework
    }
    return render(request,"detail.html",context)



@login_required(login_url = "user:login")
def userhomeworks(request):
    homeworks = Homework.objects.filter(student = request.user)    
    context = {
        "homeworks" : homeworks
    }
    return render(request,"userhomeworks.html",context)



@login_required(login_url = "user:login")
def addhomework(request):
    if request.user.is_superuser == 1:

        form = HomeworkForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Ödev, Başarı ile Kaydedilmiştir...")
            return redirect("homework:dashboard")
        context = {
            "form" : form
        }
        return render(request,"addhomework.html",context)
    else:
        messages.info(request,"Bu URL ye Giriş Hakkınız Yoktur!!!")
        return redirect("index")  



@login_required(login_url = "user:login")
def update(request,id):
    if request.user.is_superuser == 1:

        homework = get_object_or_404(Homework,id = id)
        form = HomeworkForm(request.POST or None, request.FILES or None,instance = homework)
        context = {
            "form" : form
        } 
        if form.is_valid():
            form.save()
            messages.success(request,"Ödev Başarı ile Güncellenmiştir...")
            return redirect("homework:dashboard")
        return render(request,"update.html",context)
    else:
        messages.info(request,"Bu URL ye Giriş Hakkınız Yoktur!!!")
        return redirect("index")    



@login_required(login_url = "user:login")
def delete(request,id):
    if request.user.is_superuser == 1:
        homework = get_object_or_404(Homework,id = id)
        homework.delete()
        messages.success(request,"Ödev, Başarı ile Silinmiştir")
        return redirect("homework:dashboard")
    else:
        messages.info(request,"Bu URL ye Giriş Hakkınız Yoktur!!!")
        return redirect("index")     



@login_required(login_url = "user:login")
def userupdate(request,id):
    homework = get_object_or_404(Homework,id = id)
    form = HomeworkForm2(request.POST or None, instance = homework)
    context = {
        "form" :  form
    }

    if form.is_valid():
        form.save()
        messages.success(request,"Ödeviniz Başarı ile Güncellenmiştir...")
        return redirect("homework:userhomeworks")
    return render(request,"userupdate.html",context)



