from django.urls import path
from . import views


app_name = "rooms"

urlpatterns = [
    path(
        "<int:pk>",
        views.RoomDetail.as_view(),
        name="detail",
    ),  # room_list.html의 url 태그에 쓰일 namespace room:detail
    path("search/", views.SearchView.as_view(), name="search"),
]
