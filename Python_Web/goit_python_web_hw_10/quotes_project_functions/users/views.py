from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

# from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.shortcuts import render

from .forms import RegisterForm


class RegisterView(View):
    template_name = 'users/signup.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:root")
        return super().dispatch(request, *args, **kwargs)
    # dispatch попереджає перехід на signup залогіненому юзеру
    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, message=f'Account for {username} was created successfully')
            return redirect(to="users:login")
        return render(request, self.template_name, context={"form": form})


class CustomLogoutView(View):
    template_name = "users/logout.html"

    def post(self, request):
        logout(request)
        return render(request, self.template_name)
