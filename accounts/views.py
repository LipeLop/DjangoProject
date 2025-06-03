
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.serializeer import RegisterForm


class SignUp(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def home(request):
    return render(request, 'home.html')
