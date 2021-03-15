from django.contrib import admin
from django.utils.html import mark_safe  # 썸네일을 사진으로 볼 수 있도록 html문을 신뢰하게 해준다
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.Rule)
class ItemAdmin(admin.ModelAdmin):  # Roomtype 기능 활성화
    """ Itel Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(
    admin.TabularInline
):  # inline을 통해 admin안에 다른 admin을 넣게하기위한 클래스 // admin.StackedInline도 있다 비슷함

    model = models.Photo  # model = 가져올 모델의 클래스


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition"""

    inlines = (PhotoInline,)  # inline 설정 RoomAdmin안에 PhotoInline의 admin이 들어온다

    fieldsets = (  # 필드들을 셋팅하는 것
        (
            "Basic Info",  # 파란 글씨
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                ),  # 베이직인포 필드 안에 있는 것들
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "istant_book")}),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bathrooms",
                    "bedrooms",
                )
            },
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse",),  # 접을 수 있는 템플릿으로 변경
                "fields": (
                    "amenity",
                    "facility",
                    "rule",
                ),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "beds",
        "bathrooms",
        "bedrooms",
        "check_in",
        "check_out",
        "istant_book",
        "count_amenities",  # 사용자 정의 컬럼
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "istant_book",
        "host__superhost",
        "city",
        "room_type",
        "amenity",
        "facility",
        "rule",
        "country",
    )

    raw_id_fields = ("host",)  # host를 따로검색창이뜨도록

    search_fields = (
        "city",
        "^host__username",
    )  # 서치 필드 추가 //  ^(startswith) =(iexact) @(search) default(icontains)
    # 포링키 참조는 언더바 두개(host.username -> host__username)

    filter_horizontal = (
        "amenity",
        "facility",
        "rule",
    )

    def count_amenities(self, obj):  # 사용자 정의 컬럼에 뭐가 나올지/ self는 클래스  objt는 현재열
        return obj.amenity.count()
        # return "pota" # 보여질 것

    # count_amenities.short_description = "hello"  # 칼럼명 정의

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Define """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        # print(dir(obj.file))
        # return obj.file.url
        return mark_safe(f'<img width = "50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"