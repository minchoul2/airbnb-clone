from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
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
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = str(request.GET.get("countty", "KR"))
    room_type = request.GET.get("countty", "0")
    room_types = models.RoomType.objects.all()

    # request로 받은 정보들
    form = {
        "city": city,
        "selected_country": country,
        "selected_room_type": room_type,
    }
    # 데이터베이스에서 오는 정보들
    choices = {
        "countries": countries,
        "room_types": room_types,
    }
    return render(
        request,
        "rooms/search.html",
        {**form, **choices},  # 위 딕셔너리들을 다 풀어 놓을 거야
    )
