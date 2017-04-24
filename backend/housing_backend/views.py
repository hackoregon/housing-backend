from django_filters.rest_framework import FilterSet
from django_filters import NumberFilter, CharFilter

from housing_backend.models import Affordable, NeighborhoodRent, HousingProductionVsCost, HHToolTip, PopToolTip
from housing_backend.serializers import AffordableSerializer, RentSerializer, ProdVsCostSerializer,\
                                        HHToolTipSerializer, PopToolTipSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView


class AffordableFilter(FilterSet):
    demographic = CharFilter(name="demographic__name")
    housing_size = CharFilter(name="housing_size__household_type")

    class Meta:
        model = Affordable
        fields = ['demographic', 'housing_size']


class AffordableList(ListAPIView):
    queryset = Affordable.objects.all()
    serializer_class = AffordableSerializer
    filter_class = AffordableFilter


class AffordableDetail(RetrieveAPIView):
    queryset = Affordable.objects.all()
    serializer_class = AffordableSerializer


class RentFilter(FilterSet):
    rent_amt = NumberFilter(name="rent_amt", lookup_expr="rent")
    rent_amt_gt = NumberFilter(name="rent_amt", lookup_expr="gt")
    rent_amt_lt = NumberFilter(name="rent_amt", lookup_expr="lt")
    housing_size = CharFilter(name="housing_size__household_type")

    class Meta:
        model = NeighborhoodRent
        fields = ['rent_amt', 'housing_size']


class RentList(ListAPIView):
    queryset = NeighborhoodRent.objects.all()
    serializer_class = RentSerializer
    filter_class = RentFilter


class RentDetail(RetrieveAPIView):
    queryset = NeighborhoodRent.objects.all()
    serializer_class = RentSerializer


class ProdVsCostList(ListAPIView):
    queryset = HousingProductionVsCost.objects.all()
    serializer_class = ProdVsCostSerializer

class RentFilter(FilterSet):
    rent_amt = NumberFilter(name="rent_amt", lookup_expr="rent")
    rent_amt_gt = NumberFilter(name="rent_amt", lookup_expr="gt")
    rent_amt_lt = NumberFilter(name="rent_amt", lookup_expr="lt")
    housing_size = CharFilter(name="housing_size__household_type")

    class Meta:
        model = NeighborhoodRent
        fields = ['rent_amt', 'housing_size']


class HHToolTip(ListAPIView):
    queryset = HHToolTip.objects.all()
    serializer_class = HHToolTipSerializer


class PopToolTip(ListAPIView):
    queryset = PopToolTip.objects.all()
    serializer_class = PopToolTipSerializer