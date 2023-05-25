from django.urls import path, include

from cargo.views import CargoListView, CargoCreateApiView, CarCreateApiView, CarUpdateApiView, \
    CargoDetail, CarListApiView
from get_location import show_location_byuniknumber

urlpatterns = [

    # path('', CargoListView.as_view(), name='cargo'),
    path('', CarListApiView.as_view(), name='cargo_list'),
    path('cargo_create', CargoCreateApiView.as_view(), name='cargo_create'),
    path('cargo_update/<int:pk>', CargoCreateApiView.as_view(), name='cargo_update'),
    path('funk1/<slug:slug>', CargoDetail.as_view(template_name='cargo/location_bynumber.html'), name='cargo_location'),


    path('car_create', CarCreateApiView.as_view(), name='car_create'),
    path('car_update/<int:pk>', CarUpdateApiView.as_view(), name='car_update'),
# path('car_update/<int:pk>', CarUpdateApiView.as_view(), name='car_update'),

]