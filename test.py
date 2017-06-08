import os
import activities
import unittest
import tempfile
from register import User

class ActivitiesTestCase(unittest.TestCase):
    def setUp(self):
        self.U =  User()
        self.app = activities.app.test_client()
    def test_empty_dictionary(self):
        rv = self.app.get('/')
        assert 'No entries' in self.U
if __name__ == '__main__':
    unittest.main()