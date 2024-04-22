import pyrebase
from requests.exceptions import HTTPError
import json
from datetime import datetime
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


def Major():
  return db.child('Major').get().val()

class User():
  def Login(email,password):
    try:
      user = auth.sign_in_with_email_and_password(email,password)
      type = db.child('User').child(user['localId']).child('Type').get().val()
      if type == None:
        return {
                'Success':False,
                'Message':"Email hoặc mật khẩu không đúng"
               }
      id = db.child('User').child(user['localId']).child('ID').get().val()
      return {
              'ID':id, 
              'Type':type,
              'Success':True,
              'Message':None
             }
    except:
      return {
              'Success':False,
              'Message':"Email hoặc mật khẩu không đúng"
             }
  def AdminLogin(email,password):
    try:
      user = auth.sign_in_with_email_and_password(email,password)
      type = db.child('User').child(user['localId']).child('Type').get().val()
      if type == 'Student' or type =='Teacher':
         return "Email hoặc mật khẩu không đúng"
      else:
         return None
    except:
      return "Email hoặc mật khẩu không đúng"
  def create(type, id , email,password):
    if len(str(password)) < 6:
      return {'success':False, 'message':"Mật khẩu phải có ít nhất 6 ký tự"}
    try:
      user = auth.create_user_with_email_and_password(email,password)
      db.child('User').child(user['localId']).set(user)
      db.child('User').child(user['localId']).update({
        'Type':type,
        'ID':id,
        'Password':password
      })
      return {'success':True, 'User_ID':user['localId']}
    except:
      return {'success':False, 'message':"Email này đã tồn tại"}
  def remove(user_id):
    email = db.child('User').child(user_id).child('email').get().val()
    password = db.child('User').child(user_id).child('Password').get().val()
    user = auth.sign_in_with_email_and_password(email,password)
    auth.delete_user_account(user['idToken'])
    db.child('User').child(user_id).remove()



class Student():
  def all():
    students = db.child('Student').get().each()
    if students != None:
      return  [student.val() for student in students] 
    else:
      return None
  
  def get_student(student_id):
    return db.child('Student').child(student_id).get().val()
  
  def create(student_id,name,email,major,date,year,password):
    if db.child('Student').child(student_id).get().val() != None:
      return "Mã số sinh viên này đã tồn tại"
    Success = User.create('Student',student_id,email,password)
    if Success['success']:
      db.child('Student').child(student_id).set({
          'ID' : student_id,
          'Name' : name,
          'Credits' : 0,
          'Email': email, 
          'Date' : date,
          'Count':0,
          'Major' : major,
          'Year' : year,
          'GPA' : 0.0,
          'UID' : Success['User_ID']
      })
      return None
    else:
      return Success['message']
    
  def update(student_id,new_name,new_email,new_major,new_date,new_year):
    user_id = db.child('Student').child(student_id).child('UID').get().val()
    db.child('Student').child(student_id).update({
          'Name' : new_name,
          'Email': new_email, 
          'Date' : new_date,
          'Major' : new_major,
          'Year' : new_year,
    })
    db.child('User').child(user_id).update({'email':new_email})
    
  def remove(student_id):
   user_id = db.child('Student').child(student_id).child('UID').get().val()
   class_list = db.child('Student').child(student_id).child('Class_list').get().val()
   if class_list != None:
      for item in class_list:
         student_list = db.child('Class').child(item['Course']).child(item['Class']).child('Student_list').get().val()
         if student_list != None:
            for student in student_list:
               if student == str(student_id):
                  student_list.remove(student)
                  db.child('Class').child(item['Course']).child(item['Class']).update({
                     'Student_list':student_list,
                     'Count':len(student_list)
                  })
                  break
   User.remove(user_id)
   db.child('Student').child(student_id).remove()
   db.child('Grade').child(student_id).remove()
  def register_course(student_id, course_id, class_id):
     course = db.child('Student').child(student_id).child('Class_list').child(course_id).get().val()
     student = db.child('Class').child(course_id).child(class_id).child('Student_list').child(student_id).get().val()
     if course == None and student == None:
        if db.child('Student').child(student_id).child('Class_list').get().val() == None:
           db.child('Student').child(student_id).update({
              'Class_list':[{'Course':course_id, 'Class':class_id}]
           })
        else:
           class_list = db.child('Student').child(student_id).child('Class_list').get().val()
           class_list.append({'Course':course_id, 'Class':class_id})
           db.child('Student').child(student_id).update({
              'Class_list':class_list
           })
        if db.child('Class').child(course_id).child(class_id).child('Student_list').get().val() == None:
           db.child('Class').child(course_id).child(class_id).update({
              'Student_list':[student_id],
              'Count':1
           })
        else:
           student_list = db.child('Class').child(course_id).child(class_id).child('Student_list').get().val()
           student_list.append(student_id)
           db.child('Class').child(course_id).child(class_id).update({
              'Student_list':student_list,
              'Count':len(student_list)
           })
        Grade.create(student_id,course_id)
        return True
     else:
        return False
  def get_course(student_id):
     class_list = db.child('Student').child(student_id).child('Class_list').get().val()
     if class_list == None:
        return None
     else:
       list = []
       for item in class_list:
          list.append({
             'Class':db.child('Class').child(item['Course']).child(item['Class']).get().val(),
             'Course': db.child('Course').child(item['Course']).get().val()         
             })
       return list
  def get_timetable(student_id):
     class_list = db.child('Student').child(student_id).child('Class_list').get().each()
     if class_list == None:
        return None
     else:    
        list = []
        Credits = 0
        for item in class_list:
          list.append({
             'Course': db.child('Course').child(item.val()['Course']).get().val(),
             'Class':db.child('Class').child(item.val()['Course']).child(item.val()['Class']).get().val()
          })
        Credits+= int(db.child('Course').child(item.val()['Course']).get().val()['Credits'])
     return {'List':list, 'Credits':Credits}
  def delete_course(student_id , course_id, class_id):
     class_list = db.child('Student').child(student_id).child('Class_list').get().val()
     student_list = db.child('Class').child(course_id).child(class_id).child('Student_list').get().val()
     if student_list == None:
        return None
     for item in class_list:
        if item['Course'] == course_id and item['Class'] == class_id:
           class_list.remove(item)
           break
     for student in student_list:
        if student == student_id:
           student_list.remove(student)
           break
     db.child('Student').child(student_id).update({
        'Class_list':class_list,
     })
     db.child('Class').child(course_id).child(class_id).update({
        'Student_list':student_list
     })
     db.child('Class').child(course_id).child(class_id).update({
        'Count':len(student_list)
     })   
     Grade.remove(student_id,course_id)    
  def get_result(student_id):
     class_list = db.child('Student').child(student_id).child('Class_list').get().val()
     list = []
     if class_list != None:
      for item in class_list:
        list.append({
            'Course':db.child('Course').child(item['Course']).get().val(),
            'Grade':db.child('Grade').child(student_id).child(item['Course']).get().val()
        })  
      return list  
class Teacher():
  def all():
    teachers = db.child('Teacher').get().each()
    if teachers != None:
      return [teacher.val() for teacher in teachers]
    else:
       return None
  
  def get_teacher(teacher_id):
    return db.child('Teacher').child(teacher_id).get().val()
  
  def create(teacher_id, name,email, level,field,password):
    if db.child('Student').child(teacher_id).get().val() != None:
        return "Mã số giảng viên này đã tồn tại"
    Success = User.create('Teacher',teacher_id,email,password)
    if Success['success']:
      db.child('Teacher').child(teacher_id).set({
          'ID' : teacher_id,
          'Name' : name,
          'Email': email, 
          'Level':level,
          'Field':field,
          'UID' : Success['User_ID']
      })
      return None
    else:
      return Success['message']
    
  def update(teacher_id,new_name,new_email, new_level,new_field):
        user_id = db.child('Teacher').child(teacher_id).child('UID').get().val()
        db.child('Teacher').child(teacher_id).update({
                    'Name' : new_name,
                    'Email' : new_email,
                    'Level' : new_level,
                    'Field' : new_field,
        })
        db.child('User').child(user_id).update({'email':new_email})

  def remove(teacher_id):
    user_id = db.child('Teacher').child(teacher_id).child('UID').get().val()
    course_list = db.child('Teacher').child(teacher_id).child('Course_List').get().each()
    if course_list != None:
       for item in course_list:
          class_list = db.child('Teacher').child(teacher_id).child('Course_List').child(item.key()).get().val()
          if class_list != None:
             for clss in class_list:
                db.child('Class').child(item.key()).child(clss).remove()
    User.remove(user_id)
    db.child('Teacher').child(teacher_id).remove()

  def get_schedule(teacher_id):
     course_list = db.child('Teacher').child(teacher_id).child('Course_List').get().each()
     if course_list != None:
        list = []
        for item in course_list:
           list.append({
               'Course':db.child('Course').child(item.key()).get().val(),
               'Class':[db.child('Class').child(item.key()).child(clas).get().val() for clas in item.val()]
           })
        return list
  def scoring(student_id, course_id, Excercise, Assignment, Midterm, FinalTerm):
     FinalGrade = float((0 if  Excercise =='CB' else int(Excercise))*10/100 + (0 if  Assignment =='CB' else int(Assignment))*20/100 +(0 if  Midterm =='CB' else int(Midterm))*20/100+(0 if  FinalTerm =='CB' else int(FinalTerm))*50/100)
     db.child('Grade').child(student_id).child(course_id).update({
        'Excercise_Grade':Excercise,
        'Assignment_Grade':Assignment,
        'MidTerm_Grade':Midterm,
        'FinalTerm_Grade':FinalTerm,
        'Final_Grade': round(FinalGrade,1)
     })
     Grade.gpa(student_id)


class Course():
    def all():
        courses = db.child('Course').get().each()
        if courses == None:
            return None
        else: 
            return  [course.val() for course in courses]
        
    def create(course_id, name , credits, type):
        course = db.child('Course').child(course_id).get().val()
        if course == None:
            db.child('Course').child(course_id).set({
                'ID':course_id,
                'Name':name,
                'Credits':credits,
                'Type':type
            })
        else:
            return "Khoá học này đã tồn tại"
        
    def update(course_id, new_name, new_credits, new_type):
            db.child('Course').child(course_id).update({
                'ID':course_id,
                'Name':new_name,
                'Credits':new_credits,
                'Type':new_type
            })

    def remove(course_id):
        db.child('Course').child(course_id).remove()
        
    def getCourse(course_id):
        return db.child('Course').child(course_id).get().val()


class Class():
    def all(course_id):
        clss = db.child('Class').child(course_id).get().each()
        if clss != None:
            return [clas.val() for clas in clss]
        else:
            return None
    def create(class_id, classroom, course_id, teacher_id, maxsize, time):
        name = db.child('Teacher').child(teacher_id).child('Name').get().val()
        if name == None:
            return "Giáo viên này không tồn tại"
        if db.child('Class').child(course_id).child(class_id).get().val() == None:
            db.child('Class').child(course_id).child(class_id).set({
                'ID':class_id,
                'Classroom':classroom,
                'Course':course_id,
                'Teacher':{'ID':teacher_id, 'Name':name},
                'Count' : 0,
                'Maxsize' : maxsize,
                'Time':time,
            })
            course_list = db.child('Teacher').child(teacher_id).child('Course_List').child(course_id).get().val()
            if course_list == None:
                db.child('Teacher').child(teacher_id).child('Course_List').update({
                    course_id:[class_id]
                })
            else:
                course_list.append(class_id)
                db.child('Teacher').child(teacher_id).child('Course_List').update({
                     course_id:course_list
                })
        else:
            return "Lớp này đã tồn tại"
        
    def remove(course_id, class_id):
        teacher_id  = db.child('Class').child(course_id).child(class_id).child('Teacher').child('ID').get().val()
        class_list = db.child('Teacher').child(teacher_id).child('Course_List').child(course_id).get().val()
        student_class_list = db.child('Class').child(course_id).child(class_id).child('Student_list').get().val()
        if class_list != None:
            for item in class_list:
               if item == class_id:
                  class_list.remove(item)
                  break
        if student_class_list != None:
           for student in student_class_list:
              class_student_list = db.child('Student').child(student).child('Class_list').get().val()
              if class_student_list != None:
                 for item in class_student_list:
                    if item['Course'] == course_id and item['Class'] == class_id:
                       class_student_list.remove(item)
                       db.child('Student').child(student).update({
                          'Class_list':class_student_list
                       })
                       break
        db.child('Teacher').child(teacher_id).child('Course_List').update({
            'Course_List':class_list
        })
        db.child('Class').child(course_id).child(class_id).remove()
    def get_class(course_id, class_id):
        return db.child('Class').child(course_id).child(class_id).get().val()
    def update(course_id, class_id, classroom, teacher_id, maxsize, time):
       name = db.child('Teacher').child(teacher_id).child('Name').get().val()
       db.child('Class').child(course_id).child(class_id).update({
          'Classroom':classroom,
          'Teacher':{'ID':teacher_id, 'Name':name},
          'Count' : 0,
          'Maxsize' : maxsize,
          'Time':time,
       })
    def get_studentList(course_id, class_id):
       list = []
       student_list =  db.child('Class').child(course_id).child(class_id).child().child('Student_list').get().val()
       if student_list == None:
          return None
       for student in student_list:
          list.append({
             'Student':db.child('Student').child(student).get().val(),
             'Grade':db.child('Grade').child(student).child(course_id).get().val()
          })
       return list
       

class Grade():
   def create(student_id, course_id):
      grade = db.child('Grade').child(student_id).child(course_id).get().val()
      if grade == None:
         db.child('Grade').child(student_id).child(course_id).set({
            'Excercise_Grade':'CB',
            'Assignment_Grade':'CB',
            'MidTerm_Grade':'CB',
            'FinalTerm_Grade':'CB',
            'Final_Grade':'CB'
         })
   def remove(student_id, course_id):
       grade = db.child('Grade').child(student_id).child(course_id).get().val()
       if grade != None:
          db.child('Grade').child(student_id).child(course_id).remove()
   def gpa(student_id):
      Result = db.child('Grade').child(student_id).get().each()
      if Result != None:
         Credits = 0
         Fail = 0
         Gpa = 0.0
         for item in Result:
            if item.val()['Final_Grade'] >= 4.0 and item.val()['Final_Grade'] != 'CB':
               Credits +=int(db.child('Course').child(item.key()).child('Credits').get().val())
               Gpa += float(item.val()['Final_Grade']) * float(db.child('Course').child(item.key()).child('Credits').get().val())
            else:
               Credits +=int(db.child('Course').child(item.key()).child('Credits').get().val())
               Fail+=int(db.child('Course').child(item.key()).child('Credits').get().val())
               Gpa += float(item.val()['Final_Grade']) * float(db.child('Course').child(item.key()).child('Credits').get().val())
         db.child('Student').child(student_id).update({
            'Credits':Credits-Fail,
            'GPA':round((Gpa/Credits),1)
         })


class Content():
   def addSubject(course_id,class_id,subject):
      content_list =  db.child('Content').child(course_id).child(class_id).get().val()
      if content_list == None:
         db.child('Content').child(course_id).update({
            class_id:[{
               'Subject':subject,
               'Content':"NULL"
            }]
         })
      else:
         content_list.append({
               'Subject':subject,
               'Content':"NULL"
            })
         db.child('Content').child(course_id).update({
            class_id:content_list
         })
   def getSubject(course_id,class_id):
      return db.child('Subject').child(course_id).child(class_id).get().val()
   def upload(course_id,class_id,subject,title,upload_file):
      content_list = db.child('Content').child(course_id).child(class_id).get().val()
      if content_list != None:
         for item in content_list:
            if item['Subject'] == subject:
               Contents = item['Content']
               if Contents == "NULL":
                  item['Content'] = [{'Title':title, 'URL':f"{course_id}/{class_id}/{upload_file.name}"}]
               else:
                  Contents.append({'Title':title, 'URL':f"{course_id}/{class_id}/{upload_file.name}"})
               break
      db.child('Content').child(course_id).update({
          class_id:content_list
      })         
      storage.child(f"{course_id}/{class_id}/{upload_file.name}").put(upload_file)
   def load(course_id,class_id):
      list = []
      i = 0
      content_list = db.child('Content').child(course_id).child(class_id).get().val()
      if content_list != None:
         for item in  content_list:
            if item['Content'] == 'NULL':
               list.append({
                  'Index':i,
                  'Subject':item['Subject'],
                  'Content':None
               })
            else: 
               ContentList = []
               index = 0
               for it in item['Content']:
                  ContentList.append({
                     'Title':it['Title'],
                     'Index':index,
                     'URL':storage.child(it['URL']).get_url(None)
                  })
                  index+=1
               list.append({
                  'Index':i,
                  'Subject':item['Subject'],
                  'Content':ContentList
               })
            i+=1
         return list
   def delContent(course_id,class_id,subject,index):
      contents = db.child('Content').child(course_id).child(class_id).get().val()
      for content in contents:
         if content['Subject'] == subject:
            i = 0
            for item in content['Content']:
               if i == index:
                  content['Content'] = 'NULL'
                  storage.delete(item['URL'],None)
                  break
               else:
                  i+=1
            break
      db.child('Content').child(course_id).update({
         class_id:contents
      })
class Message():
   def all():
      return db.child('Message').child('General').get().val()
