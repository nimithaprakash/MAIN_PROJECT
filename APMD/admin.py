from flask import*
from database import*

app=Flask(__name__)

admin=Blueprint('admin',__name__)

@admin.route("/admin_home")
def admin_home():
    return render_template("admin_home.html")

@admin.route("/verify_teacher",methods=['post','get'])
def manage_test():
    data={}
    qry3= "select * from teacher"
    data['view']=select(qry3)
    
    
    if 'submit' in request.form:
        input=request.form['input']
        qry8="insert into test values(null,'%s','%s')"%(session['teacher'],input)
        insert(qry8)
                
        return """<script>alert('ADDED');window.location='verify_teacher'</script>"""

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
        
    if action=='reject':
        qry9="delete from teacher where teacher_id='%s'"%(id)
        delete(qry9)
        return """<script>alert('DELLTED');window.location='verify_teacher'</script>"""
    
    if action=='update':
        qry="select * from test where test_id='%s'"%(id)
        res=select(qry)
        if res:
            data['up']=res

        
    return render_template("verify_teacher.html",data=data)

@admin.route('/view_complaints',methods=['get','post'])
def view_complaints():
    data={}
    qry="select * from complaints"
    res=select(qry)
    data['view']=res
    return render_template('view_complaints.html',data=data)

@admin.route("/send_reply",methods=['get','post'])
def send_reply():
    id=request.args['id']
    if 'sendreply' in request.form:
        reply=request.form['reply']
        qry="update complaints set reply='%s' where complaint_id='%s'"%(reply,id)
        update(qry)
        return """<script>alert('reply send successfully');window.location="/view_complaints"</script>"""
        
    return render_template("send_reply.html")
        
        
    

