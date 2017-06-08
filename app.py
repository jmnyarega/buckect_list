from flask import Flask,render_template,request,session
from register import User
from activities import Activities
from invited import Invite

U =  User()
activity = Activities()
invited_friends = Invite()

app = Flask(__name__)
app.config['SECRET_KEY'] = "123456abcde"



@app.route('/',methods = ['GET','POST'])
def index():
    '''
            This function render a login page and authenticates the user when the form is submitted
    '''
    if request.method == 'GET':
        return render_template("index.html",name="name")
    elif request.method == 'POST':
        print(U.get_all_users())
        if U.get_all_users().get(request.form['username']):
            if U.get_all_users().get(request.form['username']) == request.form['password']:
                session['user'] = request.form['username']
                data = activity.get_all_activities()      
                return render_template('activities.html',data = data)
            else:
                return  render_template("index.html",name="invalid login")
        return  render_template("index.html",name="invalid login")


@app.route('/registration',methods=['GET','POST'])
def register():
    '''
    This form render a registration form and add a new user once the form has been submitted

    '''
    if request.method == 'GET':
        return render_template("register.html",name="")
    elif    request.method == 'POST':
        U.save(request.form['username'],request.form['password']) 
        return render_template('register.html',name="")



@app.route('/new_activity',methods=['GET','POST'])
def new_activity():
    if request.method == 'GET':
        return render_template('new_activity.html')
    elif request.method == 'POST':
        activity.add_activity(request.form['title'],request.form['description'],request.form['date2'],'pending',session['user'])        
        data = activity.get_all_activities()      
        return render_template('activities.html',data = data)
        

@app.route('/activity_list')
def list_activities():
        data = activity.get_all_activities()      
        return render_template('activities.html',data = data)


@app.route('/activity_delete<title>')
def delete_activity(title):
    activity.delete_activity(title)
    #get all names on this title
    invited_friends.delete_friends_by_title(title)
    # invited_friends.
    data = activity.get_all_activities()    
    return render_template('activities.html',data = data)


@app.route('/invited/<title>')
def get_invited_friends(title):
    data = invited_friends.get_all(title);
    return render_template('invited.html',title=title,data=data)

@app.route('/invite_friend/<titles>',methods = ['POST','GET'])
def invite_friend(titles):
    if request.method == 'GET':
        return render_template('new_friend.html',title=titles)
    elif request.method == 'POST':
        invited_friends.add_friend(request.form['title'],request.form['first_name'],request.form['second_name'],request.form['status'])
        data = invited_friends.get_all(titles);
        return render_template('invited.html',title=titles,data=data)  


@app.route('/delete_friend/<name>,<title>')
def delete_friend(name,title):
    invited_friends.delete_friend(title,name)
    data = invited_friends.get_all(title);      
    return render_template('invited.html',title=title,data = data)    

@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('index.html')  

@app.route('/status/<title>')
def activity_status(title):
    return "jos "+str(invited_friends.get_activity_status(title))


if __name__ == '__main__':
    app.run(debug=True)
