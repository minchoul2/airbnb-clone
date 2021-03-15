from django.db import models
from django.utils import (
    timezone,
)  # 장고가 관리하도록 파이썬의 datetime이 아닌 장고의 timezone을 import //setting.pt->TIME_ZONE
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """ Reservation Model Definition  """

    STATUS_PENDING = "pendig"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCLED = "canceled"

    STATUS_CHOICE = (
        (STATUS_CANCLED, "Cancled"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_PENDING, "Pending"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True  # True False를 이모티콘으로 하겠다.

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
