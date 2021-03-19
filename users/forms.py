from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())  # 패스워드 별표처리

    def clean_email(self):  # clean 하고싶은 데이터는 "clean_필드명" 으로 하자고 약속 in django
        email = self.cleaned_data.get("email")  # user가 보낸 데이터에서 email을 갖는 것
        try:
            models.User.objects.get(username=email)  # User.username 에 email이 있는지 보고
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("USer does not exist")  # 정보 없으면 에러

    def clean_password(self):
        print("clen ps")
