from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())  # 패스워드 별표처리

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return (
                    self.cleaned_data
                )  # 이메일, 비밀번호 다 맞으면 확인해보자 # clean()을 쓴다면 항상 cleaned_data를 리턴해줘야함
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))

        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
