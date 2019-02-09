import json
import unittest
from Forum.app.api.v1.models.parties.parties_models import PartiesModel
from Forum.tests.v1.__init__ import BaseTest
from Forum.app.__int__ import create_app

class PartyData:
    def setUp(self):
        self.app = create_app
        self.client = self.app.test_client()
        Party = PartiesModel()
        party1 = {
            "id":4,
            "name":"office1",
            "logoUrl":"logoUrl1",
            "hqAddress":"hqAddress1"

        }
        party2 = {
            "id":9,
            "name":"office2",
            "logoUrl":"logoUr2",
            "hqAddress":"hqAddress2"
        }
class BaseOfficeClass(PartyData,BaseTest):
    """sets up the path for endpoints"""
    path ="/api/v1/parties"

class TestEndpoints(PartyData, unittest.TestCase):
    
    def test_create_parties(self):
        resp = self.client.post(path, data=json.dumps(self.politicaloffice1), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
    def test_get_all_parties(self):
        """tests endpoint to get all parties"""
        resp = self.client.get(path, content_type='application/json')
        self.assertEqual(resp.status_code, 200)
    
    def test_get_specific_parties(self):
        """tests the endpoint to get a specific office"""        
        post = self.client.post(path='', data=json.dumps(self.politicaloffice1), content_type='application/json')
        int_id = int(post.json['blog_id'])
        path = '{}'.format(int_id)
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()

