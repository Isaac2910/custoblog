
from django.conf import settings

from django.shortcuts import redirect, render

# Create your views here.
from django.contrib.auth import authenticate, login, logout

from . import forms
"""from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator

from django.forms import formset_factory
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models"""





from django.views.generic import View





class LoginPageView(View):

    template_name = 'authentication/login.html'

    form_class = forms.LoginForm



    def get(self, request):

        form = self.form_class()

        message = ''

        return render(request, self.template_name, context={'form': form, 'message': message})

        

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = authenticate(

                username=form.cleaned_data['username'],

                password=form.cleaned_data['password'],

            )

            if user is not None:

                login(request, user)

                return redirect('home')

        message = 'Identifiants invalides.'

        return render(request, self.template_name, context={'form': form, 'message': message})

# views.py
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})


def logout_user(request):
    
    logout(request)
    return redirect('login')


#fonction pour le forms d'inscription


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})