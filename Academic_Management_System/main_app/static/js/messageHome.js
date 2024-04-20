import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getDatabase , ref , push , update , onValue , get, set} from 
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
document.addEventListener('DOMContentLoaded',()=>{
  const Path = ref(database,`Message/General`)
  console.log(Path)
  const sectionGeneral = document.querySelector('#special')
  console.log(sectionGeneral)
  onValue(Path, function(snapshot){
    if(snapshot.exists()){
      console.log("New Data")
      let array = snapshot.val()
    for(let i = array.length -1 ; i >= 0  ; i-- ){
         let mess = array[i]
         let div = document.createElement('div')
         div.classList.add("special__grid")
         div.innerHTML = 
         `
         <div>
            <h3>${mess['Title']}</h3>
         </div>
         <div class="sender">
            Bởi ${mess['Name']} - ngày ${mess['Date']['Day']} tháng ${mess['Date']['Month']} năm ${mess['Date']['Year']}
         </div >
          ${mess['Content']}
          `
          sectionGeneral.appendChild(div)
    }
    }else{
      console.log('No Data')
       sectionGeneral.innerHTML += `<h3 style="text-align: center;"> Hiện tại không có thông báo nào</h3>`
    }
  })
})