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


class SignUpForm(forms.Form):

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User alreaby exist!!")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        # username,email,password / 암호화된 비밀번호로 유저생성
        user = models.User.objects.create_user(email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
