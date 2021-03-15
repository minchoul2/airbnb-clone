import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):
    help = "this command create user"
    # print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="how many users do you want creat"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        # all_users = user_models.User.objects.all()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 19),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bathrooms": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
            },
        )
        # 사진 넣기
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))

        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.Rule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)  # 포링키 인스턴스
            for i in range(3, random.randint(10, 30)):  # 사진몇개넣을지
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,  # 포링키
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                )
            # 다대다 필드추가
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenity.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facility.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.rule.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number}rooms created!"))