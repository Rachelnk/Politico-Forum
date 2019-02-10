import unittest

from Forum.tests.v1.helper_methods import create_office
from Forum.tests.v1.base_test import BaseTestCase
#from Forum.tests.v1.sample_data import SampleData

class TestOffice(BaseTestCase):
    
    
    def setUp(self):
        super(TestOffice, self).setUp()

    def test_posting_an_office(self):
        """Test for creating a new office"""
        politicaloffice = {
            "id":9,
            "name":"office1",
            "type":"type1"

        }
        resp = create_office(self, politicaloffice)
        self.assertEqual(resp.status_code, 404)

    def test_getting_all_offices(self):
        """Test for getting all offfices"""
        resp = self.client.get(path='/api/v1/offices/')
        self.assertEqual(resp.status_code, 404)

    """def test_getting_a_single_office(self):
        Test for getting a single office
        politicaloffice = {
            "id":9,
            "name":"office1",
            "type":"type1"

        }
        data = politicaloffice
        post = create_office(self, data)
        #int_id = int(post.json['id'])
        int_id = int(post.json['data'][0]['id'])
        path = '/api/v1/offices/{}'.format(int_id)
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)"""


if __name__ == '__main__':
    unittest.main()
