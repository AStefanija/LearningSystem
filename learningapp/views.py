from django.shortcuts import render, redirect
from .models import Course, Message
from .forms import MessageForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")


def aboutUs(request):
    return render(request, "about_us.html")

def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=True)
            message.save()
            return redirect("contact")
    context = {"form": MessageForm}
    return render(request, "contact.html", context = context)

def yourCourse(request):
    return render(request, "your_course.html")

def IntroductionToC(request):
    return render(request, "IntroductionToC++.html")

def Operators(request):
    return render(request, "Operators.html")

def Conditions(request):
    return render(request, "Conditions.html")

def Loops(request):
    return render(request, "Loops.html")

def Arrays(request):
    return render(request, "Arrays.html")

def Functions(request):
    return render(request, "Functions.html")

def Classes(request):
    return render(request, "Classes.html")

def Enum(request):
    return render(request, "Enum.html")


