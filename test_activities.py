from app import app
from activities import Activities
import unittest


class InvitedTestCase(unittest.TestCase):

    def setUp(self):
        
        self.tester = app.test_client(self)
        self.activities = Activities()

    def test_add_Activity(self):
        self.assertIsNotNone(self.activities.add_activity('Bootcamp','Studying','12-01-1990','pending','josiah').get('Bootcamp'),msg='Ativity not added')
        

    def test_delete_activity(self):
        self.activities.add_activity('Bootcamp','Studying','12-01-1990','pending','josiah')
        self.assertIsNone(self.activities.delete_activity('Bootcamp'), msg='Activity not removed')

    def test_set_cancel_activity(self):
        
        self.activities.add_activity('Bootcamp','Studying','12-01-1990','pending','josiah')
        self.assertEqual(self.activities.set_canceled('Bootcamp').get('Bootcamp')[-2],'canceled')


    def test_set_pending_activity(self):
        
        self.activities.add_activity('Bootcamp','Studying','12-01-1990','pending','josiah')
        self.assertEqual(self.activities.set_pending('Bootcamp').get('Bootcamp')[-2],'pending')

    def test_set_done_activity(self):
        
        self.activities.add_activity('Bootcamp','Studying','12-01-1990','pending','josiah')
        self.assertEqual(self.activities.set_done('Bootcamp').get('Bootcamp')[-2],'done')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()