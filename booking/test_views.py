from django.test import TestCase


# Create your tests here.
class TestViews(TestCase):

    def test_index_view(self):
        response = self.client.get('self.index_url')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
