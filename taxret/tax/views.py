from django.shortcuts import render, redirect
from .models import user, tax_on_capital_gain, Income_Tax_Slab, Salary, Capital_gain, Deduction, Other_Income
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from django.http import HttpResponse
from .forms import userform, oiform, tocgform, Itsform, Salaryform, cgform, deductionform 


# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"tutorials":user.objects.all()})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("/fillform")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def logout_request(request):
    
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")
def fillform123(request):
    return render(request = request,
                  template_name='main/fillform.html',
                  context = {"tutorials":tax_on_capital_gain.objects.all()})

def account(request):
    return render(request = request,
                  template_name='main/account.html',
                  context = {"sal":Salary.objects.all(),"toc":tax_on_capital_gain.objects.all()})
def user123(request):
    return render(request = request,
                  template_name='main/user123.html',
                  context = {"tutorials":user.objects.all()})
def tocg(request):
    return render(request = request,
                  template_name='main/tocg.html',
                  context = {"tutorials":tax_on_capital_gain.objects.all(),"usr":user.objects.all()})
def Its(request):
    return render(request = request,
                  template_name='main/Its.html',
                  context = {"tutorials":Income_Tax_Slab.objects.all()})
def Salary123(request):
        return render(request = request,
                  template_name='main/Salary123.html',
                  context = {"tutorials":Salary.objects.all()})
def cg(request):
    return render(request = request,
                  template_name='main/cg.html',
                  context = {"tutorials":Capital_gain.objects.all()})
def deduction(request):
        return render(request = request,
                  template_name='main/deduction.html',
                  context = {"tutorials":Deduction.objects.all()})

def oi(request):
    
    return render(request = request,
                  template_name='main/oi.html',
                  context = {"tutorials":Other_Income.objects.all()})

def fillform123(request):
    return render(request = request,
                  template_name = 'main/fillform.html',
                  context = {"tutorials":user.objects.all()})

def userformview(request):
    form = userform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
            }
           
    return render(request, "main/userform123.html", context)
    
    
def tocgformview(request):
            
    form = tocgform(request.POST)
    if form.is_valid():
        form.save()
    context = {
        'form':form
            }

           
    return render(request, "main/tocgform123.html", context)

def Itsformview(request):
    form = Itsform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
            }
           
    return render(request, "main/Itsform123.html", context)

def salaryformview(request):
    form = Salaryform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
            }
           
    return render(request, "main/Salaryform123.html", context)


def cgformview(request):
    form = cgform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
            }
           
    return render(request, "main/cgform123.html", context)

def dformview(request):
    form = deductionform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
            }
           
    return render(request, "main/deductionform123.html", context)

def calculationview(request):
    return render(request = request,
                  template_name='main/calculation.html',
                  context = {"user":user.objects.all(),"tocg":tax_on_capital_gain.objects.all(),
                             "Its":Income_Tax_Slab.objects.all(),"Sal":Salary.objects.all(),
                             "Cg":Capital_gain.objects.all(),"ded":Deduction.objects.all(),
                             "Oi":Other_Income.objects.all()})
    
def oiformview(request):
    form = oiform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
            }
           
    return render(request, "main/oiform123.html", context)
    

    
    
