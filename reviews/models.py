from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):
    """ Review Model Definition """

    # 모델의 필드
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # 모델의 관계
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    # 커스텀함수를 모델에 정의 -> 모든곳에서 볼 수 있다. //admin에서 정의하면 admin에서만 볼수 있다.
    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "AVG."  # 어드민 패널에 들어갈 이름 설정
