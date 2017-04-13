from rest_framework import serializers
from housing_backend.models import *


class DemographicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demographic
        exclude = ('id',)


class HousingSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HousingSize
        exclude = ('id',)


class NeighborhoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Neighborhood
        exclude = ('id',)
        depth = 1

class ReportYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportYear
        exclude = ('id',)
        depth = 1


class AffordableSerializer(serializers.ModelSerializer):
    demographic = DemographicSerializer()
    housing_size = HousingSizeSerializer()
    neighborhood = NeighborhoodSerializer()

    class Meta:
        model = Affordable
        fields = ('affordable', 'demographic', 'housing_size', 'neighborhood')

class RentSerializer(serializers.ModelSerializer):
    housing_size = HousingSizeSerializer()
    nh_id = NeighborhoodSerializer()
    year = ReportYearSerializer()

    class Meta:
        model = NeighborhoodRent
        fields = ('year', 'rent_amt', 'housing_size', 'nh_id')
        depth = 1


class ProdVsCostSerializer(serializers.ModelSerializer):
    neighborhood = NeighborhoodSerializer()

    class Meta:
        model = HousingProductionVsCost
        fields = (
                'year',
                'neighborhood',
                'single_unit_growth',
                'multi_unit_growth',
                'home_price_growth',
                'rent_growth'
                )



