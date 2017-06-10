
class  Activities(object):

    activities = {}
    def __init__(self,CANCELED = 'canceled',PENDING = 'pending',DONE = 'done'):
        self.CANCELED = CANCELED
        self.PENDING  = PENDING
        self.DONE     = DONE

    def add_activity(self,title,description,date,status,user):       
        self.activities[title]   =  [description,date,status,user]
        return self.activities

    def get_all_activities(self):
        return self.activities

    def delete_activity(self,title):
        del self.activities[title]

    def update_activity(self,title,description,date,status,user):
        self.activities[title]  =    [description,date,status,user]

    def set_canceled(self,title):
        self.activities[title][2] = self.CANCELED
        return self.activities

    def set_pending(self,title):
        self.activities[title][2] = self.PENDING
        return self.activities

    def set_done(self,title):
        self.activities[title][2] = self.DONE
        return self.activities

    def get_status(self,title):
        return self.activities[title][2]

    def get_activity_details(self,title):
        return self.activities[title]
