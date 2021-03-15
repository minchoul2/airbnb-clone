from math import ceil
from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage

# from django.http import HttpResponse
from . import models


def all_rooms(request):  # 뷰 이름은 urls.py에서 path 의 이름과 같아야함
    page = request.GET.get("page", 1)  # 두번째 인자는 default 값, page사용시 필요
    room_list = models.Room.objects.all()  # 사실 쿼리셋을 호출하는 것은 Lazy하게 한다!!
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))  # get_page는 보통 다 갖춰짐 // page는 에러를 컨트롤 해줘야함
        return render(
            request,
            "rooms/home.html",
            context={"page": rooms},
        )
    except EmptyPage:
        return redirect("/")  # 처음으로 돌아가라
