from django.test import TestCase, Client
from django.urls import reverse


class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello_view(self):
        response = self.client.get(reverse("hello"))
        # print(response)
        expect_data = "GeekTech"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), expect_data)