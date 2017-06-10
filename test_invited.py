from app import app
from invited import Invite
from activities import Activities
import unittest


class InvitedTestCase(unittest.TestCase):

    def setUp(self):
        
        self.tester = app.test_client(self)
        self.invited_guests = Invite()

    def test_subclass_activities(self):
        self.assertTrue(issubclass(Invite,Activities),msg="Should inherit from Activities" ) 


    def test_add_friend_to_activity(self):
        self.invited_guests.add_friend('bootcamp','josiah','nyarega',status='pending')
        self.assertEqual(self.invited_guests.invited.get('bootcamp_josiah'),['bootcamp','josiah','nyarega','pending'],msg='Josiah not added to bootcamp activity')

    def test_delete_friend_from_activity(self):
        self.invited_guests.add_friend('bootcamp','josiah','nyarega',status='pending')
        self.invited_guests.delete_friend('bootcamp','josiah')
        self.assertEqual(None,self.invited_guests.invited.get('bootcamp_josiah'))

    def test_delete_friends_by_title(self):
        
        self.invited_guests.add_friend('bootcamp','josiah','nyarega',status='pending')
        self.assertIsNone(self.invited_guests.delete_friends_by_title('bootcamp').get('bootcamp'),None)
        
    def test_confirm_attending(self):
        
        self.invited_guests.add_friend('bootcamp','josiah','nyarega',status='pending')
        self.assertEqual(self.invited_guests.confirm_attending('bootcamp','josiah','nyarega').get('bootcamp_josiah')[-1],'attending', msg='Invalid message after confirm method')
        

    def test_confirm_not_attending(self):
        self.invited_guests.add_friend('bootcamp','josiah','nyarega',status='pending')
        self.assertEqual(self.invited_guests.confirm_not_attending('bootcamp','josiah','nyarega').get('bootcamp_josiah')[-1],'not_attending', msg='Invalid message after confirm method')
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()