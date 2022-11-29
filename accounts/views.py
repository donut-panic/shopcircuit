from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from accounts.forms import SignUpForm, UserProfileUpdateForm, LoginForm
from accounts.models import Profile
from shopcircuit import settings


# Create your views here.


class SignUpView(CreateView):
    template_name = 'sing_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')



class ProfileUpdateView(UpdateView):
    template_name = "basic_interaction.html"
    form_class = UserProfileUpdateForm
    model = Profile

    def get_success_url(self):
        return reverse('profile_view',
                    args=[self.request.user.profile.id])






class ProfileDetailsView(LoginRequiredMixin, DetailView):
    template_name = "profile.html"
    model = Profile


class UpdatedLoginView(LoginView):
    form_class = LoginForm


    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is
            self.request.session.modified = True
        return super(UpdatedLoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile_view',
                    args=[self.request.user.profile.id])




@login_required
def home(request):
    return HttpResponseRedirect(
        reverse('profile_view',
                args=[request.user.profile.id]))









