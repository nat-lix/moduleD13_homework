from django.shortcuts import render, redirect
from .models import DisposCode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from .forms import RegisterForm, LoginForm
import random
import os
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'sign/register.html'
    success_url = '/index'

    def form_valid(self, form):
        user = form.save()
        code = random.choice('12345')
        DisposCode.objects.create(code=code, user=user)
        user_email = form.cleaned_data['email']
        subject = 'Одноразовый код для регистрации'
        message = f'Ваш одноразовый код для регистрации: {code}'
        from_email = os.getenv('talathecat@yandex.ru')
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        group = Group.objects.get_or_create(name='basic')[0]

        user.groups.add(group)
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    model = User
    form_class = LoginForm
    template_name = 'sign/login.html'
    success_url = '/index'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'sign/logout.html'


    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/posts')