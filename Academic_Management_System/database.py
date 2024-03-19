import pyrebase
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
class Student():
  def create_student(id, name):
    pass
