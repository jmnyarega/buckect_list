from activities import Activities

class Invite(Activities):

    invited = {}
    def __init__(self,ATTENDING = 'attending',NOT_ATTENDING='not_attending',PENDING='pending'):
        self.ATTENDING      = ATTENDING
        self.NOT_ATTENDING  = NOT_ATTENDING
        self.PENDING        = PENDING

    def add_friend(self,title,first_name,second_name,status='pending'):
        self.invited[title+"_"+first_name] = [title,first_name,second_name,status]
        print(self.invited)
        return self.invited

    def delete_friend(self,title,first_name):
        del self.invited[title+"_"+first_name]
        return self.invited

    def get_activity_status(self,title):
        return super(Invite,self).__init__(title)

    def get_invited(self,title):
        count = 0
        for k,v in self.invited.items():
            if v[0] == title:
                count += 1
        return count

    def confirm_attending(self,title,first_name):
        self.invited[title+"_"+first_name] = [title,first_name,second_name,self.ATTENDING]
        return self.invited 


    def confirm_not_attending(self,title,first_name):
        self.invited[title+"_"+name] = [title,name,self.NOT_ATTENDING]
        return self.invited 

    def get_all(self,title):
        return self.invited
