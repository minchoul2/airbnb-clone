from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """ Custom User Model """

    # 선택박스용
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENTER_OTHER = "other"

    GENTER_CHOICE = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENTER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICE = ((LANGUAGE_ENGLISH, "english"), (LANGUAGE_KOREAN, "korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICE = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # 입력 필드
    avatar = models.ImageField(upload_to="avatar", blank=True)
    gender = models.CharField(choices=GENTER_CHOICE, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, max_length=2, blank=True, default=LANGUAGE_KOREAN
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICE, max_length=3, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)
