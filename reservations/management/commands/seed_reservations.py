import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten

from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models


NAME = "reservations"


class Command(BaseCommand):
    help = f"this command create {NAME}"
    # print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help=f"how many users do you want {NAME}"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pendig", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(1, 25)),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number}{NAME} created!"))