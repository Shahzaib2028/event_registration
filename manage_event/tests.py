from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class EventAppTesting(APITestCase):

    def create_and_login_new_user(self, username, mobile_number , email , password):
        url = reverse('user:register')
        register = {
            "username": username,
            "email": email,
            "mobile_number": mobile_number,
            "password": password
        }
        self.client.post(url, register, format='json')

        url = reverse('user:login')
        Login_payload = {
            "username": register['username'],
            "password": register['password'],
        }
        self.client.post(url, Login_payload, format='json')





    def setUp(self):
        
        self.create_and_login_new_user("Tester", "03322453672" , "tester@gmail.com" , "test123")
        url = reverse('manage_event:create')
        create_event1 = {
            "title": "Wedding",
            "description": "A wedding anneverisy",
            "date": "2010-12-23T07:28:25.109517Z",
            "location": "Lahore"
        }
        response_1 = self.client.post(url, create_event1, format='json')

        url = reverse('manage_event:create')
        create_event2 = {
            "title": "IEEE conference",
            "description": "IEEE biggest conference",
            "date": "2022-03-25T07:30:15.109517Z",
            "location": "Karachi"
        }
        response_2 = self.client.post(url, create_event2, format='json')

        self.event_ids = {
            response_1.json().get('id'): create_event1, 
            response_2.json().get('id'): create_event2,
        }


    def test_list_events(self):
        url = reverse('manage_event:events_retreive')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)





    def test_get_specific_event(self):

        for event_id in self.event_ids.keys():
            url = reverse('manage_event:event_retreive', kwargs={"pk": event_id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)





    def test_creating_a_event(self):

        url = reverse('manage_event:create')
        create_event = {
            "title": "Test creating a event",
            "description": "This is testing for creating a event",
            "date": "2021-05-29T07:32:15.109517Z",
            "location": "Engalnd"
        }
        response = self.client.post(url, create_event, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Event successfully created")





    def test_create_event_failure(self):

        url = reverse('manage_event:create')
        create_event = {
            "title": "Test creating a event",
            "description": "This is testing for creating a event",
            "date": "2022-03-29T07:30:15.109517Z",
        }
        response = self.client.post(url, create_event, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Not created because Location is required")




    def test_updating_deleting_event(self):


        for event_id, data in self.event_ids.items():
            url = reverse('manage_event:manage', kwargs={"id": event_id})
            new_update_data = {
                **data,
                "title": "Title is updated...."
            }
            response = self.client.put(url, new_update_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("successfully updated ")



        for event_id in self.event_ids.keys():
            url = reverse('manage_event:manage', kwargs={"id": event_id})
            response = self.client.delete(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        print("successfully deleted")



        


    def test_updating_event_fail(self):

        self.create_and_login_new_user("newUser", "03366106291" , "newUser@gmail.com" , "newuser123")
        for event_id, data in self.event_ids.items():
            url = reverse('manage_event:manage', kwargs={"id": event_id})
            updated_data = {
                **data,
                "title": "Title is updated...."
            }
            response = self.client.put(url, updated_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("As the event was not created by this user, so user can not update this event")


        for event_id in self.event_ids.keys():
            url = reverse('manage_event:manage', kwargs={"id": event_id})
            response = self.client.delete(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("As the event was not created by this user, so user can not delete this event")




    def test_attendee(self):

        for event_id in self.event_ids.keys():
            url = reverse('manage_event:attend', kwargs={"id": event_id})
            response = self.client.post(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        print("attendee added...")



    def test_attendee_without_login(self):

        url = reverse('user:logout')
        self.client.post(url, format='json')

        for event_id in self.event_ids.keys():
            url = reverse('manage_event:attend', kwargs={"id": event_id})
            response = self.client.post(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        print("User need to login first...")
