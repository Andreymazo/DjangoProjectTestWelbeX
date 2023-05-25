import csv
import random
from django_tables2 import tables

from cargo.models import Cargo


class CargoTable(tables.Table):
    class Meta:
        model = Cargo
        template_name = "django_tables2/bootstrap.html"
        fields = ("location_pick_up", 'location_delivery', 'location_delivery', 'description')

    def get_values(self):
        filename = 'uszips.csv'

        for i in range(1, 10):
            values = Cargo.objects.create(
                # location_pick_up=names.get_last_name(),
                # location_delivery=randint(1, 100),
                # location_delivery=randint(1, 100),
                # description=names.get_last_name()
            )
            # find size in memory os.path.getsize("/path/to/file.mp3")



            values.save()
            queryset = Cargo.objects.all()
            return queryset
