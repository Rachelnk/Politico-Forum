import unittest
import json
from Forum.app.__int__ import create_app
#from Forum.app.api.v1.models.offices.__init__ import OfficesModel


class BaseTestCase(unittest.TestCase):
    "base class for test"
    """path = "/api/v1" """
    def setUp(self):
        """configures the settings to be used to test"""
        self.app = create_app(config_name='testing')
        self.app.testing = True
        self.client = self.app.test_client()
