from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
    
@login_required
def student(request):
    return render(request, 'users/student1.html')

def faculty(request):
    return render(request, 'users/faculty.html')

def department_head(request):
    return render(request, 'users/dhead.html')

def registrars_office(request):
    return render(request, 'users/officeregister.html')

    