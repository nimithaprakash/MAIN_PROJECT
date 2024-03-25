from flask import*

from database import*

from public import public

from teacher import teacher

from admin import admin

app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(teacher)
app.register_blueprint(admin)
app.secret_key='gy'
app.run(debug=True,port=5008)