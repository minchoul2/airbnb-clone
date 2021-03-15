from datetime import datetime
from django.shortcuts import render

# from django.http import HttpResponse
from . import models


def all_rooms(request):  # 뷰 이름은 urls.py에서 path 의 이름과 같아야함
    all_rooms = models.Room.objects.all()
    return render(
        request,
        "home/home.html",  # 템플릿이름은 반드시 templates폴더의 있는 파일명과 같아야함 (요구사항)
        context={"rooms": all_rooms},  # html에 사용할 변수
    )
