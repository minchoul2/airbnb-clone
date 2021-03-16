from django.urls import path
from . import views


app_name = "rooms"

urlpatterns = [
    path("<int:pk>", views.room_detail, name="detail")
]  # room_list.html의 url 태그에 쓰일 namespace room:detail
