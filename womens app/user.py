from flask import *
from database import *
user=Blueprint('user',__name__)

@user.route('/userhome')
def userhome():
    return render_template('userhome.html')

@user.route('/viewprofile')
def viewprofile():
    data={}
    qry="select * from user where user_id='%s'"%(session['user'])
    data['user']=select(qry)

    
    return render_template('viewprofile.html',data=data)

@user.route('/us_normal_notification')
def normalnotification():
    data={}
    qry="select * from normal_notifications"
    data['normal_notification']=select(qry)

    return render_template("normaltablenotification.html",data=data)


