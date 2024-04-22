import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getDatabase , ref , push , update , onValue , get, set, off} from 
"https://www.gstatic.com/firebasejs/10.11.0/firebase-database.js";
const firebaseConfig = {
  apiKey: "AIzaSyCU44Hm0uhjR3EP98CcLGuJey3WAvo9bAo",
  authDomain: "academic-management-syst-41163.firebaseapp.com",
  databaseURL: "https://academic-management-syst-41163-default-rtdb.firebaseio.com",
  projectId: "academic-management-syst-41163",
  storageBucket: "academic-management-syst-41163.appspot.com",
  messagingSenderId: "605353132079",
  appId: "1:605353132079:web:349702e48dbd25ad9346da",
  measurementId: "G-MLMFJ9PD68"
};
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
const MenuSideBar = document.querySelector('#MenuSideBar')
const counter = document.querySelector('.count')
fetch("/check_id")
  .then(response =>{
      if(!response.ok){
         console.log("Failed")
      }else{
        console.log('Successful')
      }
      return response.json()
  })
  .then(data =>{
      console.log(`Message/${data['Type']}/${data['ID']}`)
      const message = ref(database,`Message/${data['Type']}/${data['ID']}`);
      onValue(message, function(snapshot){
        if(snapshot.exists()){
          console.log("New Data")
          MenuSideBar.innerHTML = ""
          let array = snapshot.val()
        for(let i = array.length -1 ; i >= 0  ; i-- ){
          let mess = array[i]
          console.log(mess)
          addMessage(mess['Name'],mess['Title'],mess['Content'],mess['Date'])
  
        }
        }else{
           MenuSideBar.innerHTML = ""
           MenuSideBar.innerHTML += `<h3 style="text-align: center;"> Hiện tại không có thông báo nào</h3>`
        }
    
      })
    // window.location.reload()
    const submitButton = document.querySelectorAll('#notiInfo')
    submitButton.forEach( item => {
      const button = item.querySelector('button');
      const id = item.querySelector('th');
        button.addEventListener('click',()=>{
        const textArea = item.querySelector('textarea');
        let inputText = textArea.value
        let formatText = textToHTML(inputText)
        console.log('CLICK')
        console.log(textArea)
        console.log(inputText)
        console.log(formatText)
        console.log(id.innerHTML)
        console.log("Success")
        let student_id = id.innerHTML.toString()
        const Path = ref(database,`Message/Student/${student_id}`)
         get(Path).then( (snapshot) =>{
          let array = snapshot.val()
          const currentDate = new Date();
          if(array == null){
            set(Path,[{
              'Content':formatText,
              'Date':{
                  'Day':currentDate.getDay(),
                  'Month':currentDate.getMonth()+1,
                  'Year':currentDate.getFullYear(),
                  'Hour':currentDate.getHours(),
                  'Minute':currentDate.getMinutes(),
                  'Second':currentDate.getSeconds(),
              },
              'Name':`${data['Name']}`
            }])
          }else{
            array = Object.values(array)
            array.push({
              'Content':formatText,
              'Date':{
                  'Day':currentDate.getDay(),
                  'Month':currentDate.getMonth()+1,
                  'Year':currentDate.getFullYear(),
                  'Hour':currentDate.getHours(),
                  'Minute':currentDate.getMinutes(),
                  'Second':currentDate.getSeconds(),
              },
              'Name':`${data['Name']}`
            })
            set(Path,array)
          }
        })
       textArea.value = ""
     })
    })
    const submitAllButton = document.querySelector('#submitAll')
    submitAllButton.addEventListener('click',()=>{
      console.log("Click")
      const textAreaAll = document.querySelector('#textAll')
      let inputText = textAreaAll.value
      console.log(inputText)
      let formatText = textToHTML(inputText)
      let student_list = document.querySelectorAll('#id_student')
      for(let i =0; i < student_list.length;i++){
        let id = student_list[i].innerHTML.toString()
        const Path = ref(database,`Message/Student/${id}`)
       get(Path).then( (snapshot) =>{
        let array = snapshot.val()
        const currentDate = new Date();
        if(array == null){
          set(Path,[{
            'Content':formatText,
            'Date':{
                'Day':currentDate.getDay(),
                'Month':currentDate.getMonth()+1,
                'Year':currentDate.getFullYear(),
                'Hour':currentDate.getHours(),
                'Minute':currentDate.getMinutes(),
                'Second':currentDate.getSeconds(),
            },
            'Name':`${data['Name']}`
          }])
        }else{
          array = Object.values(array)
          array.push({
            'Content':formatText,
            'Date':{
                'Day':currentDate.getDay(),
                'Month':currentDate.getMonth()+1,
                'Year':currentDate.getFullYear(),
                'Hour':currentDate.getHours(),
                'Minute':currentDate.getMinutes(),
                'Second':currentDate.getSeconds(),
            },
            'Name':`${data['Name']}`
          })
          set(Path,array)
        }
      })
      }
      textAreaAll.value = ""
  })
}) 

  // button.addEventListener('click',()=>{
  //   console.log('Click')
  //   let inputText = textArea.value;
  //   let formatText = textToHTML(inputText);
  //   get(message).then( (snapshot) =>{
  //     let array = snapshot.val()
  //     if(array == null){
  //       set(message,[{
  //         'Content':formatText,
  //         'Title': "New Message",
  //         'Name':"Nguyễn Đăng Khoa"
  //       }])
  //     }else{
  //       array = Object.values(array)
  //       array.push({
  //         'Content':formatText,
  //         'Title': "New Message",
  //         'Name':"Nguyễn Đăng Khoa"
  //       })
  //       set(message,array)
  //     }
  //   })
  // })
function textToHTML(text) {
    // Loại bỏ các ký tự đặc biệt như &, <, >
    text = text.replace(/&/g, "&amp;");
    text = text.replace(/</g, "&lt;");
    text = text.replace(/>/g, "&gt;");
    // Thêm thẻ <p> cho mỗi dòng văn bản
    text = text.split("\n").map(line => "<p>" + line + "</p>").join("");
    return text;
  }



function addMessage(name,title,content,date){
  let newLi = document.createElement('li')
  let newListItem = 
  `
  <li>
  <div class="submenu-item ">
      <div><img src="static/images/profileImage.png" alt=""></div>
      <div>
          <div class="messageInfo">
              <div style = "width: 150px; text-align: center;" ><h6>${name}</h6></div>
              <div>${content.substring(0,10)+" ....."}</div>
          </div>
      </div>
      <div class="datetime">
          <div style="font-size: 10px;">${(date['Day'].toString().length) < 2 ? `0${date['Day']}` : date['Day']}/${(date['Month'].toString().length) < 2 ? `0${date['Month']}` : date['Month']}/${date['Year']}</div>
          <div><i class='bx bx-caret-right'></i></div>
      </div>
    </div>
   <!--End Main Menu-->
  
   <!--Sub Menu-->
    <ul class="menu-items submenu">
      <div class="menu-title">
              <div class="title-message">
                  <i class='bx bx-caret-left' ></i>
                  <div><img src="static/images/profileImage.png" alt="" style="
                  border: 0.5px solid rgba(0, 0, 0, 0.243);
                  justify-self: flex-start;
                  margin-left: 10px;
                  width: 50px;
                  height: 50px;
                  object-fit: cover;
                  border-radius: 50%;"></div>
              </div>
              <div><h5>${name}</h5></div>
              <div style="font-size:15px;">${date['Hour']}:${(date['Minute'].toString().length) < 2 ? `0${date['Minute']}` : date['Minute']}:${date['Second']}</div>
              </div>
      </div>
      <div style="font-size: 17px; border: solid rgba(0, 0, 0, 0.243) 1px ; height: 100%; width:350px; padding: 10px; border-radius: 12px;">
            <p>${content}</p>
      </div>
    </ul>
  </li>
  `
newLi.innerHTML+=newListItem
MenuSideBar.appendChild(newLi)
const menu = document.querySelector(".menu-content");
const menuItems = document.querySelectorAll(".submenu-item");
const subMenuTitles = document.querySelectorAll(".submenu .menu-title");
menuItems.forEach((item, index) => {
  item.addEventListener("click", () => {
    console.log("Click ")
    menu.classList.add("submenu-active");
    item.classList.add("show-submenu");
    menuItems.forEach((item2, index2) => {
      if (index !== index2) {
        item2.classList.remove("show-submenu");
      }
    });
  });
});

subMenuTitles.forEach((title) => {
  title.addEventListener("click", () => {
    menu.classList.remove("submenu-active");
  });
});
}


