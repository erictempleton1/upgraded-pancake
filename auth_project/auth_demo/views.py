from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.template.response import TemplateResponse


def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
  else:
    form = UserCreationForm()
  return render(request, 'register.html', {'form': form})

def home(request):
  return TemplateResponse(request, 'home.html')
