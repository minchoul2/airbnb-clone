# 아무것도 없는 url을 core에 정의 할 것이다.
from django.urls import path
from rooms import views as room_views

# 필수
app_name = "core"

urlpatterns = [
    path("", room_views.all_rooms, name="home"),
]
