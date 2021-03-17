from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class HomeView(ListView):
    """ Home View Define"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 6
    ordering = "created"
    context_object_name = "rooms"  # object_list 대신 rooms


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room
    pk_url_kwarg = "pk"  # pk이름을 바꾸는 것  pk_url_kwarg = "potato" <= urls.py pa th("<int:potato>", views.RoomDetail.as_view(), name="detail")


def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
