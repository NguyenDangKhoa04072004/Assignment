import pyrebase
from requests.exceptions import HTTPError
import json
config = {
  'apiKey': "AIzaSyCU44Hm0uhjR3EP98CcLGuJey3WAvo9bAo",
  'authDomain': "academic-management-syst-41163.firebaseapp.com",
  'databaseURL': "https://academic-management-syst-41163-default-rtdb.firebaseio.com",
  'projectId': "academic-management-syst-41163",
  'storageBucket': "academic-management-syst-41163.appspot.com",
  'messagingSenderId': "605353132079",
  'appId': "1:605353132079:web:349702e48dbd25ad9346da",
  'measurementId': "G-MLMFJ9PD68"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
class Auth():  
    def SignIn(email,password):
        try:
            User = auth.sign_in_with_email_and_password(email,password)
            id = db.child('Auth').child(User['localId'])['ID']
            return db.child('User').child(id).get().val()
        except HTTPError as e:
            return json.loads(e.strerror)['error']['message']
class User():
    def create(type, id, email, password):
        try:
            User = auth.create_user_with_email_and_password(email,password)
            db.child('Auth').child(User['localId']).set(User)
            db.child('Auth').child(User['localId']).update({'ID':id})
            db.child('User').child(id).set({
                'UID':User['localId'],
                'Type':type,
                'ID':id,
                'Email':email,
                'Password':password
            })
        except HTTPError as e:
            return json.loads(e.strerror)['error']['message']
    def remove(self,id):
        try:
            User = db.child('User').child(id).get().val()
            uid = User['UID']
            idToken = db.child('Auth').child(uid).get().val()['idToken']
            auth.delete_user_account(idToken)
            db.child('Auth').child(User['UID']).remove()
            db.child('User').child(id).remove()
        except:
            email = db.child('User').child(id).child('Email').get().val()
            password = db.child('User').child(id).child('Password').get().val()
            user = auth.sign_in_with_email_and_password(email,password)
            db.child('Auth').child(user['localId']).update(user)
            db.child('Auth').child(user['localId']).update({'ID':id})
            self.remove(self,id)
class Student():
    def all():
        students = db.child('Student').get().each()
        list = [student.val() for student in students]
        return list
    def create(id,name,email,major,date,year,password):
        if db.child('Student').child(id).get().val() == None:
            if db.child('User').get().each() != None:
                User_List = [{user.val()['Email'] for user in db.child('User').get().each()}]
                check = True
                if User_List != None:
                    for user in User_List:
                        if user == email:
                            check = False
                    if check:
                        if len(str(password)) >= 6:
                            User.create('Student',id,email,password)
                            db.child('Student').child(id).set({
                                'ID':id,
                                'Name':name,
                                'Email':email,
                                'Major':major,
                                'Date':date,
                                'Year':year,
                            })
                        else:
                            return "Mật khẩu quá yếu yêu cầu mật khẩu phải có từ 6 ký tự trở lên"
                    else:
                        return "Email này đã tồn tại"
            else:
                if len(str(password)) >= 6:
                    User.create('Student',id,email,password)
                    db.child('Student').child(id).set({
                        'ID':id,
                        'Name':name,
                        'Email':email,
                        'Major':major,
                        'Date':date,
                        'Year':year,
                    })

        else:
            return "Mã số sinh viên này đã tồn tại" 
    def remove(id):
        List = db.child('Student').child(id).child('Course_List').get().val()
        for Course in List:
            Class.delStudent(id,Course,List[Course])
        db.child('Student').child(id).remove()
        User.remove(User,id)
    def enroll(student,course):
        if db.child('Score').child(student).get().val() == None:
            db.child('Score').child(student).set({
                'Course':{str(course):0}
            })
        else:
            if db.child('Score').child(student).child('Course').get().val() != course:
                db.child('Score').child(student).child('Course').update({
                    str(course):0.0
                })
    def unenroll(student,course):
        if db.child('Score').child(student).child('Course').child(course).get().val() != None:
            db.child('Score').child(student).child('Course').child(course).remove()
    def get_course_list(id):
        course_list = db.child('Student').child(id).child('Course_List').get().each()
        for item in course_list:
            print(f"{item} , {course_list[item].get().val()}")
class Teacher():
    def all():
        teachers = db.child('Teacher').get().each()
        list = [teacher.val() for teacher in teachers]
        return list
    def create(id,name,email,level,field,password):
        User.create('Teacher',id,email,password)
        db.child('Teacher').child(id).set({
            'ID':id,
            'Name':name,
            'Email':email,
            'Level':level,
            'Field':field,
            'Password':password
        })
    def remove(id):
        db.child('Teacher').child(id).remove()
        User.remove(id)
    def grading(student,course,grade):
        if db.child('Score').child(student).child('Course').child(course).get().val() != None:
            db.child('Score').child(student).child('Course').update({course:grade})
class Course():
    def all():
        Courses = db.child('Course').get().each()
        list = [course.val() for course in Courses]
        return list 
    def create(id,name,credits,type,requirements):
        db.child('Course').child(id).set({
            'ID':id,
            'Name':name,
            'Credits':credits,
            'Type':type,
            'Requirements':requirements
        })
    def remove(id):
        db.child('Course').child(id).remove()
class Class():
    def create(id,classroom,course,teacher,time):
        if db.child('Class').child(course).child(id).get().val() == None:
            db.child('Class').child(course).child(id).set({
                'Count':0,
                'ID':id,
                'Classroom':classroom,
                'Teacher':teacher,
                'Time':time
            })
        if db.child('Teacher').child(teacher).child(course).get().val() == None:
            db.child('Teacher').child(teacher).child(course).set({
                'Count':1,
                'Class_List':{0:id}
            })
        else:
            count = int(db.child('Teacher').child(teacher).child(course).child('Count').get().val())
            db.child('Teacher').child(teacher).child(course).child('Class_List').update({count:id})
            newCount = int(count)+1
            db.child('Teacher').child(teacher).child(course).update({'Count':newCount})
    def addStudent(student,course,Class,):
        if db.child('Class').child(course).child(Class).child('Student_List').get().val() == None:
            db.child('Class').child(course).child(Class).update({
                'Count':1,
                'Student_List':{0:student}
            })
        else:
            count = db.child('Class').child(course).child(Class).child('Count').get().val()
            db.child('Class').child(course).child(Class).child('Student_List').update({count:student})
            newCount = int(count)+1
            db.child('Class').child(course).child(Class).update({'Count':newCount})
        db.child('Student').child(student).child('Course_List').update({course:Class})
    def delStudent(student,course,Class):
        Student_List = db.child('Class').child(course).child(Class).child('Student_List').get().val()
        if  Student_List != None:
            i = 0
            for std in Student_List:
                if std == student: 
                    db.child('Class').child(course).child(Class).child('Student_List').child(i).remove()
                    count = db.child('Class').child(course).child(Class).child('Count').get().val()
                    newCount = int(count)-1
                    db.child('Class').child(course).child(Class).update({'Count':newCount})
                    break
                else:
                    i=i+1
        if db.child('Student').child(student).child('Course_List').child(course).get().val() != None:
            db.child('Student').child(student).child('Course_List').child(course).remove()
    def remove(course,id):
        if db.child('Class').child(course).child(id).get().val() != None:
            teacher = db.child('Class').child(course).child(id).child('Teacher').get().val()
            Student_List = db.child('Class').child(course).child(id).child('Student_List').get().val()
            if  Student_List != None:
                for student in Student_List:
                    db.child('Student').child(student).child('Course_List').child(course).remove()
            db.child('Class').child(course).child(id).remove()
            count = db.child('Teacher').child(teacher).child(course).child('Count').get().val()
            class_list = db.child('Teacher').child(teacher).child(course).child('Class_List').get().val()
            if class_list != None:
                i = 0
                for item in class_list:
                    if item == id:
                         db.child('Teacher').child(teacher).child(course).child('Class_List').child(i).remove()
                         newCount = int(count)-1
                         if newCount == 0:
                            db.child('Teacher').child(teacher).child(course).remove()
                         else:
                            db.child('Teacher').child(teacher).child(course).update({'Count':newCount})
                    else:
                        i = i+1
# print(Student.create(2211620,'Nguyễn Đăng Khoa','dagkoa@gmail.com','Computer Science','01/01/2004',2022,'123456'))
#Teacher.create('OS121','Nguyen Duy Phuong','duyphuong@gmail.com','Banchelor','Infomation System','123456')
# Class.create('L01',{'Buiding':'H1','Room':201,'Base':2},'CO1007','OS121',{
#         'Day':"Monday" , 
#         'Start':{'Hour':2, 'Minute':0},
#         'End' : {'Hour':3, 'Minute':50}
#     })
# Class.create('L02',{'Buiding':'H1','Room':401,'Base':2},'CO2008','OS121',{
#         'Day':"Tuesday" , 
#         'Start':{'Hour':7, 'Minute':0},
#         'End' : {'Hour':8, 'Minute':50}
#     })
#Course.create("CO2008","Hệ điều hành",4,'Ngành','Kiến trúc máy tính')
# Class.addStudent(2211612,"Data Structure and Algorithm",'L01')
# Class.addStudent(2211612,"Operating System",'L01')
# Class.addStudent(2211621,"Operating System",'L01')
# Class.addStudent(2211622,"Operating System",'L01')
# Class.addStudent(2211623,"Operating System",'L01')
# Class.addStudent(2211624,"Operating System",'L01')
# Class.addStudent(2211625,"Operating System",'L01')
# Class.remove('Operating System','L01')
#Class.delStudent(2211618,"Operating System",'L01')
# Class.addStudent("Nguyen Thi Ngoc Xuyen","Operating System",'L01')
#Class.delStudent("Nguyen Thi Ngoc Xuyen","Operating System",'L01')
#print(Student.all())
# Student.remove(2211612)
#print(db.child('Class').child('Operating System').child('L01').child('Student_List').get().val())
#Class.addStudent(2211620,'CO2008','L02')
#print(Student.get_course_list(2211620))