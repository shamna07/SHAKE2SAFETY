from flask import *
from database import *

admin=Blueprint('admin',__name__)


@admin.route('/adminhome')
def adminhome():
    
    return render_template("adminhome.html")

@admin.route('/viewuser')
def viewuser():
    data={}
    qry="select * from user"
    data['user']=select(qry)

    
    return render_template('viewuser.html',data=data)

@admin.route('/newstip', methods=["post","get"])
def newstip():
    if 'submit' in request.form:
        title=request.form['title']
        description=request.form['description']
        date=request.form['date']
        qry="insert into news_tips values(null,'%s','%s','%s')"%(title,description,date)
        insert(qry)
    return render_template("newstip.html")

@admin.route('/normalnotification', methods=["post","get"])
def normalnotification():
    if 'submit' in request.form:
        title=request.form['title']
        description=request.form['description']
        date=request.form['date']
        qry="insert into normal_notifications values(null,'%s','%s','%s')"%(title,description,date)
        insert(qry)
    return render_template("normalnotification.html")

@admin.route('/emergencynotification')
def emergencynotification():
    data={}
    qry= "SELECT * FROM `emergency_notification` INNER JOIN `user` USING (user_id)"
    data['emergenecy_notification']=select(qry)
    
    return render_template("emergencynotification.html",data=data)


@admin.route('/viewemergencyimages',methods=["post","get"])
def viewemergencyimages():
    id=request.args['id']
    data={}
    qry= "SELECT * FROM images WHERE emergency_id=5"
    data['emergenecy_notification']=select(qry)
    return render_template('view_emergency_images.html',data=data)


@admin.route('/complaints')
def complaints():
    data={}
    qry="select * from complaints"
    data['complaints']=select(qry)

    return render_template("complaints.html",data=data)

@admin.route('/admin_reply',methods=['post','get'])
def ad_comp_reply():
    id=request.args['id']
    if 'submit' in request.form:
        reply=request.form['reply']
        qry=" update complaints set reply='%s' where complaint_id='%s'"%(reply,id)
        update(qry)
    return render_template('ad_comp_reply.html')

@admin.route('/feedback')
def feedback():
    data={}
    qry="select * from feedback"
    data['feedback']=select(qry)

    return render_template("feedback.html",data=data)

@admin.route('/helplinenumber', methods=["post","get"])
def helpline():
    data={}
    qrt="select * from helpline_number"
    res=select(qrt)
    data['view']=res
    if 'submit' in request.form:
        name=request.form['name']
        contactnumber=request.form['contactnumber']
        qry="insert into helpline_number values(null,'%s','%s')"%(name,contactnumber)
        insert(qry)
    return render_template("helplinenumber.html",data=data)