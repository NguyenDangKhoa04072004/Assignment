Để chạy được cần tải python3, pip3 
Tải django bằng lệnh : pip3 install django==5.0.1
Để chạy server ảo: cd Academic_Management_System -> chạy lệnh  python3 manage.py runserver
Folder templates chứa các file html 
Folder static chia ra thành css , images, js để chứa các file tương ứng
* Để load các file css,js, images cần thêm vào đầu trang {% load static %} với mỗi đường dẫn dùng {% static 'Đường dẫn tới file css, js tương ứng' %}  vd:  {% static 'css/style.css' %}
