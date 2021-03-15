from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add: 모델을 생성할 때마다 날짜,시간 저장
    updated = models.DateTimeField(auto_now=True)  # auto_now_add: 모델을 저장할 때마다 날짜 업데이트

    class Meta:
        abstract = True