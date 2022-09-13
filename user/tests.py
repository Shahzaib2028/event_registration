# from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class UserTest(APITestCase):

    def setUp(self):
        register_url = reverse('user:register')
        data = {
            "username":"Tester",
            "email":"tester@gmail.com",
            "password":"tester123",
            "mobile_number":"03322917356"
        }

        self.client.post(register_url, data, format='json')


    def test_user_can_register(self):
        register_url = reverse('user:register')
        data = {
            "username":"Tester1",
            "email":"tester1@gmail.com",
            "password":"tester123",
            "mobile_number":"03322911356"
        }
        response = self.client.post(register_url , data , format='json')
        self.assertEqual(response.status_code ,status.HTTP_201_CREATED)
        print("Successfully registred")




    def test_user_regiter_failed(self):

        url = reverse('user:register')
        data = {
            "username": "Tester",
            "email": "tester@gmail.com",
            "mobile_number": "03322917356",
            "password": "tester123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Usename and phone numner already exists....")




    def test_login(self):
        url = reverse('user:login')
        data = {
            "username": "Tester",
            "password": "tester123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("successfully logged in")
        




    def test_login_failed(self):

        url = reverse('user:login')
        data = {
            "username": "Tester",
            "password": "PasswordNotCorrect"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Invalid credentials...")




