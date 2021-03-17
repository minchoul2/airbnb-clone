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

    price = request.GET.get("price", 0)
    guests = request.GET.get("guests", 0)
    beds = request.GET.get("beds", 0)
    bathrooms = request.GET.get("bathrooms", 0)
    bedrooms = request.GET.get("bedrooms", 0)
    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host", False)

    s_amenities = request.GET.getlist("amenities")
    s_facilites = request.GET.getlist("facilites")
    # print(s_amenities, s_facilites)
    # request로 받은 정보들
    form = {
        "city": city,
        "selected_country": country,
        "selected_room_type": room_type,
        "price": price,
        "beds": beds,
        "guests": guests,
        "bathrooms": bathrooms,
        "bedrooms": bedrooms,
        "s_amenities": s_amenities,
        "s_facilites": s_facilites,
        "instant": instant,
        "super_host": super_host,
    }
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilites = models.Facility.objects.all()
    # 데이터베이스에서 오는 정보들
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilites": facilites,
    }
    return render(
        request,
        "rooms/search.html",
        {**form, **choices},  # 위 딕셔너리들을 다 풀어 놓을 거야
    )
