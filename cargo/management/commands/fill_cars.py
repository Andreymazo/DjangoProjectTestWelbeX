import random

from django.core.management import BaseCommand

from cargo.management.commands.create_number import unik_number_creation
from cargo.models import Car


def generate_cars():

    values = Car.objects.create(
        slug=f'{unik_number_creation()}',
        latitude=random.uniform(10.0, 75.0),
        longtitude=random.uniform(10.0, 75.0),

    )
    # jj = [{"unik_number": f'{unik_number_creation}', "latitude": f'{random.uniform(10.0, 75.0)}',
    #        "longtitude": f'{random.uniform(10.0, 75.0)}'}]
    values.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(0, 20):
            generate_cars()
