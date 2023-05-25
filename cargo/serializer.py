from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from cargo.management.commands.create_number import unik_number_creation
from cargo.models import Cargo, Car


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(
        # primary_key=True,
        default=unik_number_creation,
        # editable=False)
    )
    latitude = serializers.DecimalField(max_digits=7, decimal_places=5)
    longtitude = serializers.DecimalField(max_digits=7, decimal_places=5)
    weigh = serializers.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(0)],)
    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        car.save()
        return Car(**validated_data)

    def update(self, instance, validated_data):

        ###Меняем лонгтитуд и латитуд, а юникномер остается прежний###############3
        instance.longtitude = validated_data.get('longtitude', instance.longtitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        return instance
