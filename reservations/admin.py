from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Reservation Admin Definition """

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = (
        "status",
        # "in_progress",
        # "is_finished",
    )


# in_progress,is_finished 어드민패널에서 필터링 하는 것
# https://nomadcoders.co/airbnb-clone/lectures/958 댓글참조
class ProgressListFilter(admin.SimpleListFilter):
    pass