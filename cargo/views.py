import random
import time

from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, get_object_or_404, GenericAPIView, \
    RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response

from cargo.forms import CargoForm, CarForm
from cargo.management.commands.create_number import unik_number_creation
from cargo.management.commands.distance_to_car import distance_to_point
from cargo.models import Cargo, Car

from django_tables2 import SingleTableView

from cargo.serializer import CargoSerializer, CarSerializer
from cargo.tables import CargoTable, CarTable


class CargoListView(SingleTableView):
    model = Cargo
    table_class = CargoTable
    template_name = 'cargo/cargo_list.html'
    queryset = Cargo.objects.all()
    filter_backends = [DjangoFilterBackend]

    for i in Car.objects.all():
        for j in Cargo.objects.all():
            filterset_fields = ['weigh',
                                f'{distance_to_point(j.latitude_pick_up, j.longtitude_pick_up, i.latitude, i.longtitude)}']


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


class CargoDetail(DetailView):
    model = Cargo
    form_class = CargoForm


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

        for i in queryset:
            # querysett.update({"distance": distance_to_point(float(i.latitude), float(i.longtitude), float(c1), float(c2))})

            print(f'Distance {i.slug} to {Cargo_item.slug}  = ',
                  distance_to_point(float(i.latitude), float(i.longtitude), float(c1), float(c2)))

        return queryset

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


from geopy.geocoders import Nominatim


def generate_cars():
    values = Car.objects.create(
        slug=f'{unik_number_creation()}',
        latitude=random.uniform(10.0, 75.0),
        longtitude=random.uniform(10.0, 75.0),

    )
    values.save()
    # queryset = Car.objects.all()
    # return queryset


class CarListApiView20(ListAPIView):
    serializer_class = CarSerializer

    queryset = Car.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Car.objects.all()
        print('___________________________')
        # if self.request.method == 'GET':
        self.list = queryset
        while True:
            time.sleep(10)
            for i in self.list:
                i.longtitude = random.uniform(10.0, 75.0)
                i.latitude = random.uniform(10.0, 75.0)
                i.save()
                # return queryset
                # return self.list(request, *args, **kwargs)

            queryset = Car.objects.all()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class CarCreateApiView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarUpdateApiView(UpdateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarRetrieveAPIView(RetrieveAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'slug'


