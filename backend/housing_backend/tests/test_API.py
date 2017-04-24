from django.test import TestCase, Client
from django.urls import reverse
from housing_backend.models import Affordable
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase


## Merged in from ../tests.py

class TestAffordabilityEndpoint(TestCase):
    def setup(self):
        self.client = Client()

    def test(self):
        response = self.client.get('/housing/affordable/')

        self.assertEqual(response.status_code, 200)


class AffordableListEndpointTest(APITestCase):
    def test_affordable_list_endpoint_values(self):
        """ Ensure retrieval of correct data from the /affordable/ endpoint. """

        url = reverse('affordable_list')
        # Create a random model instance
        this_object = mixer.blend(Affordable)
        this_object.save()

        # Testing database has one entry, our newly created object
        response = self.client.get(url)

        # Ensure that API affordable endpoint is working
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         'API get request should return 200 OK')

        # Ensure that API returns values matching the object we just saved
        self.assertEqual(response.data[0]['affordable'], this_object.affordable,
                         'API response value should match inserted model value')
        self.assertEqual(response.data[0]['demographic'], this_object.demographic.name,
                         'API response value should match inserted model value')
        self.assertEqual(response.data[0]['housing_size'], this_object.housing_size.household_type,
                         'API response value should match inserted model value')
        self.assertEqual(response.data[0]['neighborhood'], this_object.neighborhood.name,
                         'API response value should match inserted model value')

    def test_affordable_list_endpoint_returns_all_objects(self):
        """ Ensure that the affordable endpoint returns a list of all values """

        url = reverse('affordable_list')

        # Create and save 5 model instances
        these_objects = list()
        for _ in range(5):
            obj = mixer.blend(Affordable)
            obj.save()
            these_objects.append(obj)

        # Hit the endpoint and store in response
        response = self.client.get(url)

        # Ensure that API affordable endpoint is working
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         'API get request should return 200 OK')

        # Test that API returns all five of the objects we just saved
        self.assertEqual(len(response.data), 5, "Should return 5 item list")

        # Test that each object is included in the returned response
        result_demographic_names = [item['demographic'] for item in response.data]
        for obj in these_objects:
            self.assertTrue(obj.demographic.name in result_demographic_names,
                            'Demographic name should be in list of results')


class AffordableDetailEndpointTest(APITestCase):
    """ Test the affordable detail API endpoint """

    def test_affordable_detail_endpoint_values(self):
        """ Ensure that affordable detail endpoint returns correct object detail"""

        # Create and save a model instance
        this_object = mixer.blend(Affordable)
        this_object.save()

        # Our database has one object, pk=1. Get the appropriate detail url.
        url = reverse('affordable_detail', kwargs={'pk': 1})

        # Hit the endpoint and store in response
        response = self.client.get(url)

        # Ensure that API affordable endpoint is working
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         'API get request should return 200 OK')

        # Ensure that API returns values matching the object we just saved
        self.assertEqual(response.data['affordable'], this_object.affordable,
                         'API response value should match inserted model value')
        self.assertEqual(response.data['demographic'], this_object.demographic.name,
                         'API response value should match inserted model value')
        self.assertEqual(response.data['housing_size'], this_object.housing_size.household_type,
                         'API response value should match inserted model value')
        self.assertEqual(response.data['neighborhood'], this_object.neighborhood.name,
                         'API response value should match inserted model value')
