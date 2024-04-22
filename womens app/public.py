from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['post','get'])
def login():
    if 'login' in request.form:
        uname=request.form['username']
        password=request.form['password']
        
        qry="select * from  login where username='%s' and password='%s'"%(uname,password)
        res=select(qry)
        session['lid']=res[0]['login_id']
 
        
        print(res)
        if res:
                    
            if res[0]['usertype']=='admin':
                return redirect(url_for('admin.adminhome'))
            elif res[0]['usertype']=='user':
                qry="select * from user where login_id='%s'"%(session['lid'])
                res2=select(qry)
                session['user']=res2[0]['user_id']
        
                return redirect(url_for('user.userhome'))
            

    return render_template('login.html')

@public.route('/register',methods=["post","get"])
def register():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        qry="insert into login values(null,'%s','%s','user')"%(username,password)
        lid=insert(qry)
        qry2="insert into user values(null,'%s','%s','%s','%s','%s') "%(lid,fname,lname,phone,email)
        insert(qry2)
        return'''<script>alert("successfully submitted");window.location="/login"</script>'''
    return render_template('register.html')

@public.route('/contact us')
def contactus():
    return render_template('contactus.html')

@public.route('/sendfeedback',methods=['post','get'])
def feedback():
    if 'submit' in request.form:
        description=request.form['description']
        qry="insert into feedback values(null,'%s',curdate())"%(description)
        insert(qry)

    return render_template("sendfeedback.html")



