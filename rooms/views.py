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
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0) or 0)
    guests = int(request.GET.get("guests", 0) or 0)
    beds = int(request.GET.get("beds", 0) or 0)
    bathrooms = int(request.GET.get("bathrooms", 0) or 0)
    bedrooms = int(request.GET.get("bedrooms", 0) or 0)
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))

    s_amenities = request.GET.getlist("amenities")
    s_facilites = request.GET.getlist("facilites")
    # print(s_amenities, s_facilites)
    # request로 받은 정보들
    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "price": price,
        "beds": beds,
        "guests": guests,
        "bathrooms": bathrooms,
        "bedrooms": bedrooms,
        "s_amenities": s_amenities,
        "s_facilites": s_facilites,
        "instant": instant,
        "superhost": superhost,
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

    filter_args = {}
    # city 필터
    if city != "Antwhere":
        filter_args["city__startswith"] = city
    # country 필터
    filter_args["country"] = country
    # room_type(foreign key) 필터
    if room_type != 0:
        filter_args["room_type__pk"] = room_type
    # price
    if price != 0:
        filter_args["price__lte"] = price

    # guest
    if guests != 0:
        filter_args["guests__gte"] = guests
    # bedrooms
    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms
    # bathrooms
    if bathrooms != 0:
        filter_args["bathrooms__gte"] = bathrooms
    # beds
    if beds != 0:
        filter_args["beds__gte"] = beds

    if instant is True:
        filter_args["istant_book"] = True
    if superhost is True:
        filter_args["host__superhost"] = True  # superhost는 foreign key니까 모델안에서 끌고와야함

    if len(s_amenities) > 0:
        for s_a in s_amenities:
            filter_args["amenity__pk"] = int(s_a)
    if len(s_facilites) > 0:
        for s_a in s_facilites:
            filter_args["facility__pk"] = int(s_a)

    rooms = models.Room.objects.filter(**filter_args)

    return render(
        request,
        "rooms/search.html",
        {**form, **choices, "rooms": rooms},  # 위 딕셔너리들을 다 풀어 놓을 거야
    )
