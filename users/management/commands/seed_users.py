from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models


class Command(BaseCommand):
    help = "this command create user"
    # print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="how many users do you want creat"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(
            user_models.User, number, {"is_staff": False, "is_superuser": False}
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number}user created!"))