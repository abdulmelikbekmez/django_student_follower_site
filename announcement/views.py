from django.shortcuts import render,redirect
from .models import Announcement
from django.contrib.auth.decorators import login_required
from .forms import AnnouncementForm
from django.contrib import messages

# Create your views here.

@login_required(login_url = "user:login")
def announcement(request):
    announcements = Announcement.objects.all()
    context = {
        "announcements" : announcements
    }

    return render(request,"announcements.html",context)


@login_required(login_url = "user:login")
def addannouncement(request):
    if request.user.is_superuser == 1:
        form = AnnouncementForm(request.POST or None,request.FILES or None)
        context = {
            "form" : form
        }
        if form.is_valid():
            announcement = form.save(commit=False)
            if announcement.youtube:
                announcement.youtube = announcement.youtube.replace("watch?v=","embed/")
            announcement.save()
            messages.success(request,"Duyurunuz Başarı ile Kaydedilmiştir...")
            return redirect("homework:dashboard")
        return render(request,"addannouncement.html",context)
    else:
        messages.info(request,"Bu URL ye Giriş Hakkınız Yoktur!!!")
        return redirect("index")
    

