"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # 장고에서는 from . import settings가 아님

# 이유 : config.settings.py에서 작성한 것이 반영된것을 import 하는 것이기 떄문에
from django.conf.urls.static import static  # path를 return 해주는 도우미역할
from rooms import views as room_views

urlpatterns = [  # path(usl , views)
    path("", include("core.urls", namespace="core")),
    path(
        "rooms/", include("rooms.urls", namespace="rooms")
    ),  # room_list.html의 url 태그에 쓰일 namespace room:detail
    path("admin/", admin.site.urls),
]

if settings.DEBUG:  # 개발자모드일때만 되길 원해
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
