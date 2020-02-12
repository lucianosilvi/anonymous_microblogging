from django.test import TestCase
from rest_framework.test import APIClient


class TweetsTest(TestCase):
    def test_send_tweet(self):
        client = APIClient()
        response = client.post('/save',
                               {"name": "Carl",
                                "message": "Hi there! This is my first tweet"
                                })
        self.assertEqual(response.status_code, 200)
        answer = response.json()

        self.assertFalse(answer['error'])

    def test_send_long_tweet(self):
        client = APIClient()
        response = client.post('/save',
                               {"name": "Peter",
                                "message": ("Hi there! This is my first tweet."
                                            "This time I wrote a long one, just"
                                            "to test if the system accepts it."
                                            )
                                })
        self.assertEqual(response.status_code, 200)
        answer = response.json()

        self.assertTrue(answer['error'])
    
    def test_send_tweet_and_list(self):
        client = APIClient()

        response = client.get('/tweets/')
        self.assertEqual(response.status_code, 200)
        answer = response.json()

        self.assertEqual(len(answer), 0)

        response = client.post('/save',
                               {"name": "John",
                                "message": "Hi there! This is my first tweet"
                                })
        self.assertEqual(response.status_code, 200)
        answer = response.json()

        self.assertFalse(answer['error'])

        response = client.get('/tweets/')
        self.assertEqual(response.status_code, 200)
        answer = response.json()

        self.assertGreater(len(answer), 0)
