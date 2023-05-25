import random

from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, get_object_or_404

from cargo.forms import CargoForm
from cargo.management.commands.create_number import unik_number_creation
from cargo.models import Cargo, Car

from django_tables2 import SingleTableView

from cargo.serializer import CargoSerializer, CarSerializer
from cargo.tables import CargoTable


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

    def get_context_data(self, **kwargs):
        context = super(CargoDetail, self).get_context_data(**kwargs)
        context['form'] = CargoForm
        return context


class CarListApiView(ListAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


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

    # queryset = Car.objects.all()
    def get_queryset(self, **kwargs):

        if self.request.method == "GET":
            Car.objects.all().delete()
            for i in range(0, 20):
                generate_cars()
        queryset = Car.objects.all()
        return queryset


class CarCreateApiView(CreateAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarUpdateApiView(UpdateAPIView):
    # class LessonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

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
