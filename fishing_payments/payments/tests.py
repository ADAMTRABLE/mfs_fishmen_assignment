from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Arrival, Payment
from . serializers import ArrivalCreation , PaymentSerializer

class ArrivalCreateListViewTestCase(TestCase):
    def setUp(self):
        self.arrival_data = {
            "fish": "Salmon",
            "weight": 5.0,
            "cost_per_unit": 10.0
        }
        self.url = reverse('fish')

    def test_create_arrival(self):
        response = self.client.post(self.url, self.arrival_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Arrival.objects.count(), 1)

    def test_list_arrivals(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ArrivalDetailViewTestCase(TestCase):
    def setUp(self):
        self.arrival = Arrival.objects.create(
            fish="Salmon",
            weight=5.0,
            cost_per_unit=10.0
        )
        self.url = reverse('news', args=[self.arrival.id])

    def test_retrieve_arrival(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

def test_update_arrival(self):
    updated_data = {
        "fish": "Tuna",
        "weight": 6.0,
        "cost_per_unit": 12.0
    }
    response = self.client.put(self.url, updated_data, content_type='application/json')  # Specify content type as JSON
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.arrival.refresh_from_db()
    self.assertEqual(self.arrival.fish, updated_data["fish"])


    def test_delete_arrival(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Arrival.objects.count(), 0)

class PaymentCreateListViewTestCase(TestCase):
    def setUp(self):
        self.arrival = Arrival.objects.create(
            fish="Salmon",
            weight=5.0,
            cost_per_unit=10.0
        )
        self.payment_data = {
            "arrival": self.arrival.id
        }
        self.url = reverse('payment', args=[self.arrival.id])

    def test_create_payment(self):
        response = self.client.post(self.url, self.payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

    def test_list_payments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
