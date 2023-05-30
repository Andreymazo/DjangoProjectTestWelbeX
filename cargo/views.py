import random
import time

from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, get_object_or_404, GenericAPIView, \
    RetrieveAPIView, DestroyAPIView

from cargo.forms import CargoForm, CarForm
from cargo.management.commands.create_number import unik_number_creation
from cargo.management.commands.distance_to_car import distance_to_point
from cargo.models import Cargo, Car

from django_tables2 import SingleTableView

from cargo.serializer import CargoSerializer, CarSerializer
from cargo.tables import CargoTable, CarTable


class CargoListView(SingleTableView):
    # def get_queryset(self, **kwargs):
    #
    #     jj = [{"unik_number": f'{unik_number_creation}', "latitude": f'{random.uniform(10.0, 75.0)}', "longtitude": f'{random.uniform(10.0, 75.0)}'}]
    #     print('---------------------------0000000000000000---------------------')
    #     if request.method == 'GET':
    #         for j in jj:
    #             rec = Car(unik_number=j["unik_number"], latitude=j["latitude"],
    #                             longtitude=j["longtitude"])
    #             rec.save()

    model = Cargo
    table_class = CargoTable
    template_name = 'cargo/cargo_list.html'
    # generate_values()
    # ordering = ('',)  # quantity, name
    # table_pagination = {"per_page": 5}
    queryset = Cargo.objects.all()
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['weigh',
                        # f'{distance_to_point(Cargo.latitude_pick_up, Cargo.longtitude_pick_up, Car.latitude, Car.longtitude)}']
                        ]


# class Updatevery180Middleware():
#     queryset = Car.objects.all()
#     while True:
#         time.sleep(10)
#         for i in queryset:
#             i.longtitude = random.uniform(10.0, 75.0)
#             i.latitude = random.uniform(10.0, 75.0)
#             i.save()
#         # return queryset


class CargoListApiView(ListAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()


class CargoCreateApiView(CreateAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()


class CargoUpdateApiView(UpdateAPIView):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()


# class CargoDetail(DetailAPIView):


class CargoDetail(DetailView):
    model = Cargo
    form_class = CargoForm

    # def get_context_data(self, **kwargs):
    #     context = super(CargoDetail, self).get_context_data(**kwargs)
    #     context['form'] = CargoForm
    #     return context


class CargoDetailWithAllCarsDistance(SingleObjectMixin, generics.RetrieveAPIView):
    model = Cargo
    form_class = CargoForm
    table_class = CargoTable
    template_name = 'cargo/cargo_list.html'

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get(self.slug_url_kwarg)
        print('kwargs', slug)
        queryset = Car.objects.all()
        Cargo_item = Cargo.objects.all().get(slug=slug)
        print('Cargo_item.latitude_pick_up', Cargo_item.latitude_pick_up)
        # print('self.object', self.object)  # 'Cargo.objects.all().get(self.object.longtitude)',  Cargo.objects.all().get(self.object.longtitude)
        c1 = Cargo_item.latitude_pick_up
        c2 = Cargo_item.longtitude_pick_up
        # querysett = {}
        for i in queryset:
            # querysett.update({"distance": distance_to_point(float(i.latitude), float(i.longtitude), float(c1), float(c2))})

            print(f'Distance {i.slug} to {Cargo_item.slug}  = ',
                  distance_to_point(float(i.latitude), float(i.longtitude), float(c1), float(c2)))
        # return render(querysett, template_name='cargo/distance_bynumber.html')
        return queryset
        # return render('cargo/location_bynumber.html', {'queryset': queryset})

    # def get_object(self, **kwargs):
    #     slug = self.kwargs.get(self.slug_url_kwarg)
    #     # print('kwargs', slug)
    #     return Cargo.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))


# Получение информации о конкретном грузе по ID(локации pick - up, delivery, вес, описание, список номеров ВСЕХ машин с
# расстоянием до выбранного груза);

class CargoDestroyAPIView(DestroyAPIView):
    model = Cargo
    serializer_class = CargoSerializer


class CarListApiView(ListAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


def distance_to_point(lp1, lop1, lp2, lop2):  # Берет координаты двух точек, выдает расстояние между ними
    lat_point1 = lp1
    lon_point1 = lop1
    location1 = f"{lat_point1}, {lon_point1}"
    lat_point2 = lp2
    lon_point2 = lop2
    location2 = f"{lat_point2}, {lon_point2}"
    from geopy.distance import distance
    dist = distance(location1, location2).miles
    # print('Расстояние в милях ', dist)
    return dist


class CarListLess450(ListAPIView):
    serializer_class = CarSerializer

    # queryset = Car.objects.all()
    def get_queryset(self):
        if self.request.method == "GET":
            cargo_item = Cargo.objects.all().first()
            queryset = Car.objects.all()

            for i in queryset:
                ii = distance_to_point(i.latitude, i.longtitude, cargo_item.latitude_pick_up,
                                       cargo_item.longtitude_pick_up)
                print('____________________________________________', i, ii)
                if isinstance(ii, float) and ii < 2800.00:
                    # instance = get_object_or_404(Car, id=i.id)
                    # instance.delete()
                    print('queryset.filter(pk=i.pk)', queryset.filter(pk=i.pk))
                    queryset.get(pk=i.pk).delete()

            return queryset


# class MultipleFieldLookupMixin:
#     """
#     Apply this mixin to any view or viewset to get multiple field filtering
#     based on a `lookup_fields` attribute, instead of the default single field filtering.
#     """

# class RetrieveCargoView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
#     queryset = Cargo.objects.all()
#     serializer_class = CargoSerializer
#     lookup_fields = ['latitude_pick_up', 'longtitude_pick_up']
#
#
#     def get_object(self):
#         queryset = self.get_queryset()  # Get the base queryset
#         queryset = self.filter_queryset(queryset)  # Apply any filter backends
#         filter = {}
#         for field in self.lookup_fields:
#             if self.kwargs.get(field):  # Ignore empty fields.
#                 filter[field] = self.kwargs[field]
#         obj = get_object_or_404(queryset, **filter)  # Lookup the object
#         self.check_object_permissions(self.request, obj)
#         return obj


from geopy.geocoders import Nominatim


def generate_cars():
    values = Car.objects.create(
        slug=f'{unik_number_creation()}',
        latitude=random.uniform(10.0, 75.0),
        longtitude=random.uniform(10.0, 75.0),

    )
    # jj = [{"unik_number": f'{unik_number_creation}', "latitude": f'{random.uniform(10.0, 75.0)}',
    #        "longtitude": f'{random.uniform(10.0, 75.0)}'}]
    values.save()
    # queryset = Car.objects.all()
    # return queryset


class CarListApiView20(ListAPIView):
    serializer_class = CarSerializer

    queryset = Car.objects.all()
    # def get_queryset(self, **kwargs):
    #
    #     if self.request.method == "GET":
    #         Car.objects.all().delete()
    #         for i in range(0, 20):
    #             generate_cars()
    #     queryset = Car.objects.all()
    #     return queryset


class CarCreateApiView(CreateAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarUpdateApiView(UpdateAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    # import time
    # # def update_every180(self):
    # #     j = Car.objects.all()
    # while True:
    #     time.sleep(10)
    #     for i in queryset:
    #         i.longtitude = random.uniform(10.0, 75.0)
    #         i.latitude = random.uniform(10.0, 75.0)
    #         i.save()


class CarRetrieveAPIView(RetrieveAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'slug'

# class CargoList(ListView):
#     model = Cargo
#     queryset = Cargo.objects.all()
#
#
# class CargoCreate(CreateView):
#     model = Cargo
#     queryset = Cargo.objects.all()

# {% load render_table from django_tables2 %}
# <!doctype html>
# <html>
#     <head>
#         <title>List of cargo</title>
#     </head>
#     <body>
#         {% render_table object_list %}
#     </body>
# </html>
