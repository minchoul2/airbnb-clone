from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):
    """ Home View Define"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 6
    ordering = "created"
    context_object_name = "rooms"  # object_list 대신 rooms


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, r"rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
