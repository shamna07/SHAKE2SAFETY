from flask import *
from public import public
from database import database
from admin import admin
from user import user
from api import api

app=Flask(__name__)


app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(api,url_prefix='/api')

app.secret_key='228788732'  


app.run(debug=True,host='0.0.0.0')

