from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.views.generic import TemplateView


def signup(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/')
    else:
        form = UserRegisterForm()
        return render(request, 'registration/signup.html', {'form': form})
