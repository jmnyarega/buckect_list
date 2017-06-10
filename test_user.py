from app import app
from register import User
from invited import Invite
from activities import Activities
import unittest

class LoginRegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        self.U = User()

    # test if flask setup is correct
    def test_index(self):
        
        response = self.tester.get("/",content_type="html/text")
        self.assertEqual(response.status_code,200)
   
    # test login
    def test_login_page(self):
        response = self.tester.get("/",content_type="html/text")
        self.assertTrue(b"Alternative Login" in response.data)

    # test registration
    def test_registration_page(self):
        response = self.tester.get("/registration",content_type="html/text")
        self.assertTrue(b"Registration Area" in response.data)            
    
    #Ensure login page with correct credentials
    def test_correct_login_credentials(self):
        self.U.save('josiah','1234')
        response =self.tester.post('/',data=dict(username='josiah',password='1234',follow_redirects= True))
        self.assertTrue(b"Activities" in response.data)  

    #Ensure login page with incorrect credentials
    def test_incorrect_login_credentials(self):
        # logout 
        self.U.save('john','1234')        
        response = self.tester.post('/',data=dict(username='username',password='password',follow_redirects= True))
        self.assertTrue(b"Bucket List App - Login" in response.data,msg="Logged in with invalid credentials")

    #Ensure logout page with correct credentials
    def test_logout(self):

        # login first
        self.U.save('john','1234')
        response_login = self.tester.post('/',data=dict(username='john',password='1234',follow_redirects= True))

        # logout out now
        response_logout = self.tester.get("/logout",content_type="html/text")
        self.assertEqual(None, self.U.get_all_users().get('john'))
         
    #ensure main page requires login

    def test_login_required(self):
    
        response_activities = self.tester.get("/",content_type="html/text")       
        self.assertEqual(b"Bucket List App - Login" in response_activities.data ,True, msg="Invalid access to this page.")


    #Create a test to ensure that a user is logged in to logout 


    #ensure that activties recieves data

    def tearDown(self):
        pass


        
if __name__ == '__main__':
    unittest.main()
