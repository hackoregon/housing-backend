from rest_framework import serializers
from .models import Affordable, NeighborhoodRent, HousingProductionVsCost, HHToolTip, PopToolTip


class AffordableSerializer(serializers.ModelSerializer):
    demographic = serializers.CharField(source='demographic.name', read_only=True)
    housing_size = serializers.CharField(source='housing_size.household_type', read_only=True)
    neighborhood = serializers.CharField(source='neighborhood.name', read_only=True)
    NP_ID = serializers.IntegerField(source='neighborhood.NP_ID', read_only=True)
    year = serializers.IntegerField(source='year.year', read_only=True)

    class Meta:
        model = Affordable
        fields = ('affordable', 'demographic', 'housing_size', 'NP_ID', 'neighborhood', 'year')


class RentSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField(source='year.year', read_only=True)
    housing_size = serializers.CharField(source='housing_size.household_type', read_only=True)
    nh_id = serializers.IntegerField(source='nh_id.NP_ID', read_only=True)
    nh_name = serializers.CharField(source='nh_id.name', read_only=True)

    class Meta:
        model = NeighborhoodRent
        fields = ('year', 'rent_amt', 'housing_size', 'nh_id', 'nh_name')
        depth = 1


class ProdVsCostSerializer(serializers.ModelSerializer):
    neighborhood = serializers.CharField(source='neighborhood.name', read_only=True)
    NP_ID = serializers.IntegerField(source='neighborhood.NP_ID', read_only=True)
    year = serializers.CharField(source='year.year', read_only=True)

    class Meta:
        model = HousingProductionVsCost
        fields = (
                'year',
                'NP_ID',
                'neighborhood',
                'single_unit_growth',
                'multi_unit_growth',
                'home_price_growth',
                'rent_growth'
                )


class HHToolTipSerializer(serializers.ModelSerializer):
    neighborhood = serializers.CharField(source='neighborhood.name', read_only=True)
    NP_ID = serializers.IntegerField(source='neighborhood.NP_ID', read_only=True)
    year = serializers.CharField(source='year.year', read_only=True)


    class Meta:
        model = HHToolTip
        fields = (
            'NP_ID',
            'neighborhood',
            'demographic',
            'households',
            'year',
        )


class PopToolTipSerializer(serializers.ModelSerializer):
    neighborhood = serializers.CharField(source='neighborhood.name', read_only=True)
    NP_ID = serializers.IntegerField(source='neighborhood.NP_ID', read_only=True)
    year = serializers.CharField(source='year.year', read_only=True)

    class Meta:
        model = PopToolTip
        fields = (
            'NP_ID',
            'neighborhood',
            'ethnicity',
            'population',
            'year',
        )
