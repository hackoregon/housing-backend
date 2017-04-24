# test_models.py

import pytest
from mixer.backend.django import mixer
from housing_backend.models import Affordable, Demographic, HousingSize, Neighborhood, ReportYear,\
                                   HousingSupply, HousingPermits, HousingProductionVsCost
from django.db import models


pytestmark = pytest.mark.django_db


class TestAffordable:
    """ Test housing_backend Affordable model"""

    def test_model_creation(self):
        """ Test creation and saving of Affordable model """

        this_obj = mixer.blend('housing_backend.Affordable')
        assert this_obj.pk == 1, 'Should create a post instance with pk 1'
        assert isinstance(this_obj, Affordable)

    def test_model_has_custom_str_method(self):
        """ Test __str__ method of Affordable model is different than models.Model.__str__"""

        assert Affordable.__str__ is not models.Model.__str__, "__str__ method should have been overridden"

    def test_model_has_custom_repr_method(self):
        """ Test __repr__ method of Affordable model is different than models.Model.__repr__"""

        assert Affordable.__repr__ is not models.Model.__repr__, "__repr__ method should have been overridden"

    def test_model_str_method_return_value(self):
        """ Test __str__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.Affordable')
        template = "{dm} {sz} {nh}"
        attrs = {
                "dm": this_obj.demographic,
                "sz": this_obj.housing_size,
                "nh": this_obj.neighborhood
        }

        assert this_obj.__str__() == template.format(**attrs), "Should return demo, housing_size, neighborhood"

    def test_model_repr_method_return_value(self):
        """ Test __repr__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.Affordable')
        template = "{dm} {sz} {nh}"
        attrs = {
                "dm": this_obj.demographic,
                "sz": this_obj.housing_size,
                "nh": this_obj.neighborhood
        }

        assert this_obj.__repr__() == template.format(**attrs), "Should return demo, housing_size, neighborhood"


class TestDemographic:
    """ Test housing_backend Demographic model"""

    def test_model_creation(self):
        """ Test creation and saving of Demographic model """

        this_obj = mixer.blend('housing_backend.Demographic')
        assert this_obj.pk == 1, 'Should create a post instance with pk 1'
        assert isinstance(this_obj, Demographic), 'Should create an instance of Demographic model'

    def test_model_has_custom_str_method(self):
        """ Test __str__ method of Demographic model is different than models.Model.__str__"""

        assert Demographic.__str__ is not models.Model.__str__, "__str__ method should have been overridden"

    def test_model_has_custom_repr_method(self):
        """ Test __repr__ method of Demographic model is different than models.Model.__repr__"""

        assert Demographic.__repr__ is not models.Model.__repr__, "__repr__ method should have been overridden"

    def test_model_str_method_return_value(self):
        """ Test __str__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.Demographic')
        assert this_obj.__str__() == this_obj.name, "Should return Demographic.name"

    def test_model_repr_method_return_value(self):
        """ Test __repr__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.Demographic')

        assert this_obj.__repr__() == this_obj.name, "Should return Demographic.name"


class TestHousingSize:
    """ Test housing_backend HousingSize model"""

    def test_model_creation(self):
        """ Test creation and saving of HousingSize model """

        this_obj = mixer.blend('housing_backend.HousingSize')
        assert this_obj.pk == 1, 'Should create a post instance with pk 1'
        assert isinstance(this_obj, HousingSize), 'Should create an instance of HousingSize model'

    def test_model_has_custom_str_method(self):
        """ Test __str__ method of HousingSize model is different than models.Model.__str__"""

        assert HousingSize.__str__ is not models.Model.__str__, "__str__ method should have been overridden"

    def test_model_has_custom_repr_method(self):
        """ Test __repr__ method of HousingSize model is different than models.Model.__repr__"""

        assert HousingSize.__repr__ is not models.Model.__repr__, "__repr__ method should have been overridden"

    def test_model_str_method_return_value(self):
        """ Test __str__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.HousingSize')
        assert this_obj.__str__() == this_obj.household_type, "Should return HousingSize.household_type"

    def test_model_repr_method_return_value(self):
        """ Test __repr__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.HousingSize')

        assert this_obj.__repr__() == this_obj.household_type, "Should return HousingSize.household_type"


class TestNeighborhood:
    """ Test housing_backend Neighborhood model"""

    def test_model_creation(self):
        """ Test creation and saving of Demographic model """

        this_obj = mixer.blend('housing_backend.Neighborhood')
        assert this_obj.pk == 1, 'Should create a post instance with pk 1'
        assert isinstance(this_obj, Neighborhood), 'Should create an instance of Neighborhood model'

    def test_model_has_custom_str_method(self):
        """ Test __str__ method of Neighborhood model is different than models.Model.__str__"""

        assert Neighborhood.__str__ is not models.Model.__str__, "__str__ method should have been overridden"

    def test_model_has_custom_repr_method(self):
        """ Test __repr__ method of Demographic model is different than models.Model.__repr__"""

        assert Neighborhood.__repr__ is not models.Model.__repr__, "__repr__ method should have been overridden"

    def test_model_str_method_return_value(self):
        """ Test __str__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.Neighborhood')
        assert this_obj.__str__() == this_obj.name, "Should return Neighborhood.name"

    def test_model_repr_method_return_value(self):
        """ Test __repr__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.Neighborhood')

        assert this_obj.__repr__() == this_obj.name, "Should return Neighborhood.name"


class TestReportYear:
    """ Test housing_backend ReportYear model"""

    def test_model_creation(self):
        """ Test creation and saving of ReportYear model """

        this_obj = mixer.blend('housing_backend.ReportYear')
        assert this_obj.pk == 1, 'Should create a post instance with pk 1'
        assert isinstance(this_obj, ReportYear), 'Should create an instance of ReportYear model'

    def test_model_has_custom_str_method(self):
        """ Test __str__ method of ReportYear model is different than models.Model.__str__"""

        assert ReportYear.__str__ is not models.Model.__str__, "__str__ method should have been overridden"

    def test_model_has_custom_repr_method(self):
        """ Test __repr__ method of ReportYear model is different than models.Model.__repr__"""

        assert ReportYear.__repr__ is not models.Model.__repr__, "__repr__ method should have been overridden"

    def test_model_str_method_return_value(self):
        """ Test __str__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.ReportYear')
        assert this_obj.__str__() == str(this_obj.year), "Should return string of ReportYear.year"

    def test_model_repr_method_return_value(self):
        """ Test __repr__ method returns correctly formatted string"""

        this_obj = mixer.blend('housing_backend.ReportYear')

        assert this_obj.__repr__() == str(this_obj.year), "Should return string of ReportYear.year"


class TestHousingSupply:
    def test_model_creation(self):
        """ Test creation and saving of HousingSupply model """

        this_obj = mixer.blend('housing_backend.HousingSupply')
        assert this_obj.pk == 1, 'Should create a post instance with pk 1'
        assert isinstance(this_obj, HousingSupply), 'Should create an instance of HousingSupply model'

    def test_model_has_custom_str_method(self):
        """ Test __str__ method of HousingSupply model is different than models.Model.__str__"""

        assert HousingSupply.__str__ is not models.Model.__str__, "__str__ method should have been overridden"

    def test_model_has_custom_repr_method(self):
        """ Test __repr__ method of HousingSupply model is different than models.Model.__repr__"""

        assert HousingSupply.__repr__ is not models.Model.__repr__, "__repr__ method should have been overridden"


class TestHousingPermits:
    def test_model_creation(self):
        """ Test creation and saving of HousingPermits model """

        this_obj = mixer.blend('housing_backend.HousingPermits')
        assert this_obj.pk == 1, 'Should create a post instance with pk 1'
        assert isinstance(this_obj, HousingPermits), 'Should create an instance of HousingSupply model'

    def test_model_has_custom_str_method(self):
        """ Test __str__ method of HousingPermits model is different than models.Model.__str__"""

        assert HousingPermits.__str__ is not models.Model.__str__, "__str__ method should have been overridden"

    def test_model_has_custom_repr_method(self):
        """ Test __repr__ method of HousingPermits model is different than models.Model.__repr__"""

        assert HousingPermits.__repr__ is not models.Model.__repr__, "__repr__ method should have been overridden"

class TestHousingProductionVsCost:
    def test_model_creation(self):
        """ Test creation and saving of HousingProductionVsCost model """

        this_obj = mixer.blend('housing_backend.HousingProductionVsCost')
        assert this_obj.pk == 1, 'Should create an instance with pk 1'
        assert isinstance(this_obj, HousingProductionVsCost), 'Should create an instance of ProductionVsCost model'

    #TODO Moar tests here
