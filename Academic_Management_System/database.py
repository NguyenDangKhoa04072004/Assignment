import pyrebase
import json
import requests
from requests.exceptions import HTTPError
config = {
  'apiKey': "AIzaSyADvmTCZB5tJLLgTTuNBHyQKbEtYEilb_g",
  'authDomain': "academic-management-project.firebaseapp.com",
  'databaseURL': "https://academic-management-project-default-rtdb.firebaseio.com",
  'projectId': "academic-management-project",
  'storageBucket': "academic-management-project.appspot.com",
  'messagingSenderId': "934007202157",
  'appId': "1:934007202157:web:e4183561a6cc5ea7633a64",
  'measurementId': "G-1PW5ZVVDZ2"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


class User():
  def create_user(email,password):
    try:
      User = auth.create_user_with_email_and_password(email,password)
      db.child('User').child(User['localId']).set({
         'Email':email,
         "Password":password,
      })
      return User
    except HTTPError as e:
      return json.loads(e.strerror)['error']['message']
  def delete_user(email,password):
    User = auth.sign_in_with_email_and_password(email,password)
    auth.delete_user_account(User['idToken'])
    db.child('User').child(User['localId']).remove()
    return None
  def reset_password(email):
    auth.send_password_reset_email(email)
class Student():
  def create_student(id,name,sex,email,major,date,faculty,year,password):
    try:
      user = User.create_user(email,password)
      db.child('User').child(user['localId']).update({
        'ID':id,
        'Type':'Student'
      })
      db.child('Student').child(id).set({
        'ID':id,
        'Name':name,
        'Sex':sex,
        'Email':email,
        'Major':major,
        'Date':date,
        'Faculty':faculty,
        'Year':year
      })
    except HTTPError as e:
      return json.loads(e.strerror)['error']['message']
  def delete_student(id):
    pass
class Teacher():
  pass
class Course():
  pass
class GPA():
  pass
class Class():
  pass
class Schedule():
  pass
class Resource():
  pass

print(db.child('User').order_by_value().get())