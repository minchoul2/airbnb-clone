from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):
    help = "this command create facilities"
    # print("hello")

    """    
    def add_arguments(self, parser):
        parser.add_argument("--times", help="helap!!!!!!!!!!!")
    """

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in facilities:
            room_models.Facility.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} created!"))
