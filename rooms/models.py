# 파이썬
from django.db import models  # 쟝고
from django.urls import reverse  # url name이 필요, retrun url
from django_countries.fields import CountryField  # 써드파티
from core import models as core_models  # 사용자패키지
from users import models as user_models

# 룸의 여러 설정들
class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "RoomType"
        ordering = ["created"]

    pass


class Amenity(AbstractItem):
    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"

    pass


class Facility(AbstractItem):
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"

    pass


class Rule(AbstractItem):
    """ HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"

    pass


# 사진
class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        "Room", related_name="photos", on_delete=models.CASCADE
    )  # Room은 밑에있기 떄문에 인식x -> string으로 바꿔줘서 패스시킬수 있다.

    def __str__(self):
        return self.caption


# 기본 룸 정보
class Room(core_models.TimeStampedModel):

    """Rooom Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField(null=True)
    beds = models.IntegerField()
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    istant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",  # user_model.User -> "users.User"
    )  # 1대 다 관계는 포링키필드 //유저삭제시 룸도삭제//on_delete는 포링키에만
    # related_name은 user가 어떻게 우릴찾기 원합니까
    room_type = models.ForeignKey(
        "RoomType",
        on_delete=models.SET_NULL,
        related_name="rooms",
        null=True,
        blank=True,
    )  # 다대다 관계는 매니투매니필드
    amenity = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facility = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    rule = models.ManyToManyField("Rule", related_name="rooms", blank=True)

    def __str__(self):  # admin패널에 나오는 이름을 name으로 보기 위해//원래는 RoomObject(1)
        return self.name

    def save(self, *args, **kwargs):  # 장고의 save를 오버라이딩
        # self.city = str.capitalize(self.city)  # 앞글자를 대문자로
        self.city = self.city.title()  # 모든 단어 첫글자를 대문자로
        super().save(*args, **kwargs)

    # 오버라이딩 한 것
    # admin에서 view on site 버튼 생성
    def get_absolute_url(self):
        return reverse(
            "rooms:detail", kwargs={"pk": self.pk}
        )  # namespace(config.url.py):name(rooms.url.py)

    # room은 리뷰평균을 가지고 있고 사용자화면에서 보이니까 model에서 정의
    # review 모델에 room이 있기 때문에 room도 리뷰를 가지고 있는 것과 마찬가지다.
    def total_rating(self):
        all_reviews = self.reviews.all()  # related name이 reviews이기 때문에
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
