from django.urls import path, include

from cargo.views import CargoListView, CargoCreateApiView, CarCreateApiView, CarUpdateApiView, \
    CargoDetail, CarListApiView20, CarListApiView, CarListLess450, CargoDetailWithAllCarsDistance, CarRetrieveAPIView, \
    CargoDestroyAPIView

from get_location import show_location_byuniknumber

urlpatterns = [

    path('cargo_list', CargoListView.as_view(), name='cargo'),
    path('', CarListApiView20.as_view(), name='cargo_list'),
    path('car_list', CarListApiView.as_view(), name='cargo_list'),

    path('cargo_create', CargoCreateApiView.as_view(), name='cargo_create'),
    path('cargo_update/<int:pk>', CargoCreateApiView.as_view(), name='cargo_update'),
    path('funk1/<slug:slug>', CargoDetail.as_view(template_name='cargo/location_bynumber.html'), name='cargo_location'),
    path('funk2/<slug:slug>', CarListLess450.as_view(), name='car_location_450'),
    path('funk3/<slug:slug>', CargoDetailWithAllCarsDistance.as_view(template_name='cargo/distance_bynumber.html'), name='cargo_location'),
    path('car_create', CarCreateApiView.as_view(), name='car_create'),
    path('car_update/<int:pk>', CarUpdateApiView.as_view(), name='car_update'),
    path('car_location/<slug:slug>', CarRetrieveAPIView.as_view(), name='car_update'),
    path('carпo_delete/<int:pk>', CargoDestroyAPIView.as_view(), name='car_update'),

# path('car_update/<int:pk>', CarUpdateApiView.as_view(), name='car_update'),

]