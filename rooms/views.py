from math import ceil
from datetime import datetime
from django.shortcuts import render

# from django.http import HttpResponse
from . import models


def all_rooms(request):  # 뷰 이름은 urls.py에서 path 의 이름과 같아야함
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]

    page_count = ceil(models.Room.objects.count() / page_size)  # ceil은 올림 함수(from math)
    return render(
        request,
        "home/home.html",  # 템플릿이름은 반드시 templates폴더의 있는 파일명과 같아야함 (요구사항)
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(
                1, page_count + 1
            ),  # html 에서 range를 쓸 수 없어서 iterator 를 만들어서 넘겨준다
        },  # html에 사용할 변수
    )
