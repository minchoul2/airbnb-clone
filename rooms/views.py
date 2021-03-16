from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
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
        raise Http404()  # 원래있던거는 에러에 대응하는 객체를 return/ 지금은 그냥 404에러 일으켜라raise
