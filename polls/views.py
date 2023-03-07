from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def home(request):
   return render(request=request, template_name="polls/home.html")
def user_page(request):
   return render(request=request, template_name="polls/user_page.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("user_page")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	#print(render (request=request, template_name="polls/register.html", context={"register_form":form}))
	return render (request=request, template_name="polls/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print(form.cleaned_data)
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("user_page")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="polls/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")