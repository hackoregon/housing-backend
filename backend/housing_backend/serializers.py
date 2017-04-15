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
    demographic = serializers.CharField(source='demographic.name', read_only=True)
    housing_size = serializers.CharField(source='housing_size.household_type', read_only=True)
    neighborhood = serializers.CharField(source='neighborhood.name', read_only=True)

    class Meta:
        model = Affordable
        fields = ('affordable', 'demographic', 'housing_size', 'neighborhood')


class RentSerializer(serializers.ModelSerializer):
    year = serializers.CharField(source='year.year', read_only=True)
    housing_size = serializers.CharField(source='housing_size.household_type', read_only=True)
    nh_id = serializers.CharField(source='nh_id.name', read_only=True)

    class Meta:
        model = NeighborhoodRent
        fields = ('year', 'rent_amt', 'housing_size', 'nh_id')
        depth = 1


class ProdVsCostSerializer(serializers.ModelSerializer):
    neighborhood = serializers.CharField(source='neighborhood.name', read_only=True)
    year = serializers.CharField(source='year.year', read_only=True)
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



