from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import SignUpForm, UserProfileUpdateForm
from accounts.models import Profile


# Create your views here.


class SignUpView(CreateView):
    template_name = 'sing_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

class ProfileUpdateView(UpdateView):
    template_name = "forms/form.html"
    form_class = UserProfileUpdateForm
    model = Profile
    success_url = reverse_lazy('index')