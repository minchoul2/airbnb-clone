from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    # list_display = ("username", "email", ...)
    # list_filter = ("language", "currency", ...)
    # 장고는 user을 위한 admin패널이 만들어져 있기 때문에 UserAdmin을 상속 받아 사용했다.

    fieldsets = UserAdmin.fieldsets + (  # 내부 패널 추가
        (
            "Custom Profile",  # 파란거
            {
                "fields": (  # 그안에 필드들이 뭐가 들어갈지
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "is_staff",
        "is_superuser",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)
