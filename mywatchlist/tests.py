from django.test import TestCase, Client

class PostmanTest(TestCase):
    def html_test(self):
        response = Client().get('https://pbp-kd-tugas.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def xml_test(self):
        response = Client().get('https://pbp-kd-tugas.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def json_test(self):
        response = Client().get('https://pbp-kd-tugas.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
