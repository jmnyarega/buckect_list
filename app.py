from flask import Flask, redirect, render_template, request, session

from activities import Activities
from invited import Invite
from register import User

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
        return render_template("index.html")
    elif request.method == 'POST':
        print(U.get_all_users())
        if U.get_all_users().get(request.form['username']):
            if U.get_all_users().get(request.form['username']) == request.form['password']:
                session['user'] = request.form['username']
                data = activity.get_all_activities()      
                return render_template('activities.html',data = data)
            else:
                return  render_template("index.html",name="Password or username is wrong, try again.")
        return  render_template("index.html",name="Password or username is wrong, try again.")


@app.route('/registration',methods=['GET','POST'])
def register():
    '''
    This form render a registration form and add a new user once the form has been submitted

    '''
    if request.method == 'GET':
        return render_template("register.html")
    elif    request.method == 'POST':
        U.save(request.form['username'],request.form['password']) 
        if request.form['password'] != request.form['C_password']:
            return render_template('register.html',error="Your passwords do not match, try again. ")
        else:
            return render_template('register.html',name="You have been succesfully registered, you can now login ")



@app.route('/new_activity',methods=['GET','POST'])
def new_activity():
    try:
        if request.method == 'GET':
            return render_template('new_activity.html')
        elif request.method == 'POST':
            activity.add_activity(request.form['title'],request.form['description'],request.form['date2'],'pending',session['user'])        
            message = 'Added Successfully.'    
            return render_template('new_activity.html',message = message)
    except Exception as e:
        return redirect('/')

        

@app.route('/activity_list')
def list_activities():

    try:
        data = activity.get_all_activities()      
        return render_template('activities.html',data = data)
    except Exception as e:
        return redirect('/')


@app.route('/activity_delete<title>')
def delete_activity(title):
    activity.delete_activity(title)
    #get all names on this title
    invited_friends.delete_friends_by_title(title)
    # invited_friends.
    data = activity.get_all_activities()    
    return render_template('activities.html',data = data)


@app.route('/activity/mark_done/<title>')
def mark_done(title):
    try:
        activity.set_done(title)
        return redirect('activity_list')
    except Exception as e:
        return redirect('activity_list')


@app.route('/activity/mark_pending/<title>')
def mark_set_pending(title):
    try:
        activity.set_pending(title)
        return redirect('activity_list')
    except Exception as e:
        return redirect('activity_list')



@app.route('/invited/<title>')
def get_invited_friends(title):
    data = invited_friends.get_all(title);
    status = activity.get_status(title)
    print(activity.get_status(title))
    print(status)
    return render_template('invited.html',title=title,status = status,data=data)

@app.route('/invite_friend/<titles>',methods = ['POST','GET'])
def invite_friend(titles):
    if request.method == 'GET':
        return render_template('new_friend.html',title=titles)
    elif request.method == 'POST':
        invited_friends.add_friend(request.form['title'],request.form['first_name'],request.form['second_name'],request.form['status'])
        message = "Added Sucessfully."
        return render_template('new_friend.html',title=titles,message=message)  


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
