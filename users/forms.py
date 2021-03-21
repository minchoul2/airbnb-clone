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


# ModelForm : Model에 연결된 Form / 모델에서 변수를 긁어오지 않아도 됨
# ModelForm이 알아서 clean, save해주기떄문에 메소드 필요없음
class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email", "birthdate")

    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    # 없으면 동일 이메일 가입시 Integrity Error가 발생해서 임의로 추가해줌
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User alreaby exist!!")
        except models.User.DoesNotExist:
            return email

    # password랑 맞는지 확인해야하기 떄문에 남겨둠
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)  # 일단 object는 생성하지만 db에는 적용하지마라
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user.username = email
        user.set_password(password)
        user.save()