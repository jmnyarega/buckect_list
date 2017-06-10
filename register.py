class User(object):
    users    = {}
    def __init__(self):
        pass

    def check_if_user_exists(self):
        pass
    
    def login(self,username):
        # print(self.users)
        # del self.users['joss']
        return self.users.get(username)

    def save(self,username,password):
        self.users[username] = password

    def get_all_users(self):
        return self.users


    def del_user(self,username):
        del self.users[username]  
        return self.users

    def logout(self,username):
        del self.users[username] 
        return self.users
