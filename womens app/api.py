from flask import *
from database import *

import demjson

import uuid

api=Blueprint('api',__name__)



@api.route("/log")
def loginuser():
    data = {}

    uname = request.args['username']
    pwd = request.args['password']

    print(uname, pwd, "##########################################")
    q = "select * from login where username='%s' and password='%s'" % (
        uname, pwd)
    res = select(q)
    if res:

        data['status'] = 'success'
        data['data'] = res
    else:
        data['status'] = 'failed'

    return str(data)

@api.route("/customer_reg")
def register():
    data ={}
    
    fname =  request.args['fname']
    lname =  request.args['lname']
    phone =  request.args['phone']
    email =  request.args['email']
    longi=request.args['longitude']
    lat=request.args['latitude']
    username =  request.args['uname']
    password =  request.args['pswd']
    
    qry="insert into login values(null,'%s','%s','user')"%(username,password)
    lid=insert(qry)
    
    qry2="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s') "%(lid,fname,lname,phone,email,lat,longi)
    # insert(qry2)
    res = insert(qry2)
    
    if res:

        data['status'] = 'success'
        data['data'] = res
    else:
        data['status'] = 'failed'

    return str(data)

@api.route("/profile")
def viewprofile():
    data={}
    
    lid=request.args['lid']
    qry="select * from user where login_id='%s'"%(lid)
    res=select(qry)
    if res:

        data['status'] = 'success'
        data['data'] = res
    else:
        data['status'] = 'failed'

    return str(data)
    
    
    
@api.route("/notification")
def notification():
    data={}
    
    
    qry="select * from normal_notifications"
    res=select(qry)
    if res:

        data['status'] = 'success'
        data['data'] = res
    else:
        data['status'] = 'failed'

    return str(data)

@api.route("/contact")
def contact():
    data={}
    
    
    qry="select * from helpline_number"
    res=select(qry)
    print(res,"///////////////////////////////")
    if res:

        data['status'] = 'success'
        data['data'] = res
    else:
        data['status'] = 'failed'

    return str(data)

@api.route("/feedback")
def feedback():
    data={}
    
    
    qry="select * from feedback"
    res=select(qry)
    if res:

        data['status'] = 'success'
        data['data'] = res
    else:
        data['status'] = 'failed'

    return str(data)

@api.route("/emergency")
def emergency():
    data={}
    
    name =  request.args['name']
    number= request.args['number']
    relation=request.args['relation']
    lid=request.args['lid']
    s="select * from user where login_id ='%s'"%(lid)
    res=select(s)
    user_id=res[0]['user_id']
    
    qry="insert into emergency_contact values(null,'%s','%s','%s','%s')"%(user_id,name,number,relation)
    res=insert(qry)
    if res:

        data['status'] = 'success'
        data['data'] = res
    else:
        data['status'] = 'failed'

    return str(data)




    

@api.route('/getnumber')
def getnumber():
	data={}
	lid=request.args['lid']
	q="select * from emergency_contact where user_id=(SELECT user_id FROM user where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['numbers']=res[0]['number']
	else:
		data['status']="failed"
	data['method']="getnumber"
	return demjson.encode(data)






@api.route('/upload_image',methods=['get','post'])
def upload_image():
	data={}
	image=request.files['image']
	path="static/uploads/"+str(uuid.uuid4())+image.filename
	image.save(path)
	logid=request.form['logid']
	lati=request.form['lati']
	logi=request.form['logi']

	qry="SELECT `user`.*,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( wlatitude) ) * COS( RADIANS( wlongitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS( wlatitude ) ))) AS user_distance FROM `user` where user_id=(SELECT user_id FROM user where login_id='%s') HAVING user_distance  < 31.068 ORDER BY user_distance ASC "%(lati,logi,lati,logid)
	
	res=select(qry)
	print("////////////////",res)
 


	q= "INSERT into emergency_notification values(null,(SELECT user_id FROM user where login_id='%s'),'%s','%s',NOW(),'pending')"% (logid,lati,logi,)
	print(q)
	id=insert(q)
	q= "INSERT INTO  images values(null,'%s','%s',NOW())"% (path,id)
	print(q)
	id=insert(q)

	if id>0:
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	data['method'] = 'upload_image'

	return demjson.encode(data)


