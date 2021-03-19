from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm  # forms.LoginForm() X->forms.LoginForm O
    success_url = reverse_lazy(
        "core:home"
    )  # reverse 는 core:home 에 가서 url를 반환해줌 / reverse_lazy는 view가 필요할때 호출
    initial = {"email": "sny2128@gmail.com"}

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)

        return super().form_valid(form)  # 이게 호출될 때 success_url로 감


# 로그아웃은 클래스뷰일 필요 없다.
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))