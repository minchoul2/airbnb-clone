from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django_countries import countries
from . import models, forms


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


class SearchView(View):# 클래스 뷰 기반으로 옮김(def search(requst)->class ss(View):def get(self, requst))
    def get(self,request):
        country = forms.SearchForm(request.GET)

            if country:
                form = forms.SearchForm(request.GET)
                if form.is_valid():
                    city = form.cleaned_data.get("city")
                    country = form.cleaned_data.get("country")
                    room_type = form.cleaned_data.get("room_type")
                    price = form.cleaned_data.get("price")
                    guests = form.cleaned_data.get("guests")
                    bedrooms = form.cleaned_data.get("bedrooms")
                    beds = form.cleaned_data.get("beds")
                    baths = form.cleaned_data.get("baths")
                    instant_book = form.cleaned_data.get("instant_book")
                    superhost = form.cleaned_data.get("superhost")
                    amenities = form.cleaned_data.get("amenities")
                    facilites = form.cleaned_data.get("facilites")

                    filter_args = {}

                    # city 필터
                    if city != "Antwhere":
                        filter_args["city__startswith"] = city
                    # country 필터
                    filter_args["country"] = country
                    # room_type(foreign key) 필터
                    if room_type is not None:
                        filter_args["room_type"] = room_type
                    # price
                    if price is not None:
                        filter_args["price__lte"] = price

                    # guest
                    if guests is not None:
                        filter_args["guests__gte"] = guests
                    # bedrooms
                    if bedrooms is not None:
                        filter_args["bedrooms__gte"] = bedrooms
                    # bathrooms
                    if baths is not None:
                        filter_args["bathrooms__gte"] = baths
                    # beds
                    if beds is not None:
                        filter_args["beds__gte"] = beds

                    if instant_book is True:
                        filter_args["istant_book"] = True
                    if superhost is True:
                        filter_args[
                            "host__superhost"
                        ] = True  # superhost는 foreign key니까 모델안에서 끌고와야함

                    for a in amenities:
                        filter_args["amenity"] = a

                    for f in facilites:
                        filter_args["facility"] = f
                    print(filter_args)
                    rooms = models.Room.objects.filter(**filter_args)

            else:
                form = forms.SearchForm()

            return render(
                request,
                "rooms/search.html",
                {"form": form, "rooms": rooms},  # 위 딕셔너리들을 다 풀어 놓을 거야
            )


    