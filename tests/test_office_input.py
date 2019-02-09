import json
import unittest
from Forum.app.api.v1.models.offices.__init__ import OfficesModel
from Forum.tests.v1.__init__ import BaseTest
from Forum.app.__int__ import create_app

class OfficeData:
    def setUp(self):
        self.app = create_app
        self.client = self.app.test_client()
        Office = OfficesModel()
        politicaloffice1 = {
            "id":9,
            "name":"office1",
            "type":"type1"

        }
        politicaloffice2 = {
            "id":20,
            "name":"office2",
            "type":"type3"
        }
class BaseOfficeClass(OfficeData,BaseTest):
    """sets up the path for endpoints"""
    path ="/api/v1/offices"

class TestEndpoints(OfficeData, unittest.TestCase):
    
    def test_create_office(self):
        resp = self.client.post(path, data=json.dumps(self.politicaloffice1), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
    def test_get_all_offices(self):
        """tests endpoint to get all offices"""
        resp = self.client.get(path, content_type='application/json')
        self.assertEqual(resp.status_code, 200)
    
    def test_get_specific_office(self):
        """tests the endpoint to get a specific office"""        
        post = self.client.post(path='', data=json.dumps(self.politicaloffice1), content_type='application/json')
        int_id = int(post.json['blog_id'])
        path = '{}'.format(int_id)
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()

"""if __name__ == '__main__':
    unnittest.main() """
