from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView
from . import models


class HomeView(ListView):
    """ Home View Define"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 6
    ordering = "created"
    context_object_name = "rooms"  # object_list 대신 rooms


def room_detail(request, pk):
    print(pk)
    return render(request, r"rooms/detail.html")