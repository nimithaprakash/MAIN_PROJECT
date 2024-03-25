from flask import*
from database import*


teacher=Blueprint('teacher',__name__)

@teacher.route("/teacher_home")
def teacher_home():
    return render_template("teacher_home.html")


  
@teacher.route("/manage_test",methods=['post','get'])
def manage_test():
    data={}
    qry3= "select * from test inner join teacher using (Teacher_id)"
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
        
    if action=='delete':
        qry9="delete from test where test_id='%s'"%(id)
        delete(qry9)
        return """<script>alert('DELLTED');window.location='verify_teacher'</script>"""
    
    if action=='update':
        qry="select * from test where test_id='%s'"%(id)
        res=select(qry)
        if res:
            data['up']=res

        
    return render_template("verify_teacher.html",data=data)



@teacher.route("/update_test",methods=['get','post'])
def update_test():
    id=request.args['id']
    if 'update' in request.form:
        input=request.form['input']
        qry="update test set Test_name='%s' where Test_id='%s'"%(input,id)
        update(qry)
        return """<script>alert('updated');window.location='manage_test'</script>"""
    return render_template("update_test.html")

@teacher.route("/add_test",methods=['get','post'])
def add_test():
    id=request.args['id']
    if 'add' in request.form:
        input=request.form['input']
        qry="insert into test values(null,'%s','%s')"%(session['teacher'],input)
        insert(qry)
        return """<script>alert('added');window.location='manage_test'</script>"""
        
    return render_template("add_test.html")

  
  
@teacher.route("/teacher_send_comp",methods=['get','post'])
def teacher_send_comp():
    data={}
    qry="select * from complaints"
    res=select(qry)
    data['u']=res
    print(data['u'])
    if 'complaints' in request.form:
        title=request.form['title']
        des=request.form['description']
        qry="insert into complaints values(null,'%s','%s','%s','pending',curdate())"%(session['teacher'],title,des)
        insert(qry)
    return render_template("teacher_send_comp.html",data=data)

@teacher.route("/manage_qstn",methods=['post','get'])
def manage_qstn():
    id=request.args['id']
    data={}
    qry="select * from questions"
    res=select(qry)
    if res:
        data['view']=res
    if 'submit' in request.form:
        input=request.form['input']
        qry8="insert into questions values(null,'%s','%s')"%(id,input)
        insert(qry8)

    return render_template("manage_qstn.html",data=data)

# @teacher.route("/view_qstns",methods=['get','post'])
# def view_qstns():
#     data={}
#     qry3= "select * from questions inner join test using (Test_id)"
#     data['view']=select(qry3)
        
#     if 'action' in request.args:
#         action=request.args['action']
#         id=request.args['id']
#     else:
#         action=None
        
#     if action=='delete':
#         qry9="delete from test where Question_id='%s'"%(id)
#         delete(qry9)
          
#     return render_template("view_qstns.html",data=data)



# @teacher.route("/update_test",methods=['get','post'])
# def update_test():
#     id=request.args['id']
#     if 'update' in request.form:
#         input=request.form['input']
#         qry="update test set Test_name='%s' where Test_id='%s'"%(input,id)
#         update(qry)
#         return """<script>alert('updated');window.location='view_test'</script>"""
#     return render_template("update_test.html")

# @teacher.route("/add_qstn",methods=['get','post'])
# def add_test():
#     id=request.args['id']
#     if 'add' in request.form:
#         input=request.form['input']
#         qry="insert into test values(null,'%s','%s')"%(session['teacher'],input)
#         insert(qry)
#         return """<script>alert('added');window.location='view_test'</script>"""
        
#     return render_template("add_test.html")
