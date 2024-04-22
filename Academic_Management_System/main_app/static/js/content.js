// const content = document.querySelectorAll('.content-material')
// content.forEach( item =>{
//     item.addEventListener('click',()=>{
//         console.log("click")
//     })
// })

// const buttonDel = document.querySelector('#delSubject')
// buttonDel.addEventListener('click',(event)=>{
//      event.stopPropagation()
//      console.log("Click ")
// })
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getDatabase , ref , push , update , onValue , get, set, remove} from 
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
document.addEventListener('DOMContentLoaded', () => {
    const myAcordion = document.querySelectorAll('#accordionExample');
    myAcordion.forEach( item =>{
        const mydel = item.querySelector('#delSubject');
        mydel.addEventListener('click',(event)=>{
            event.stopPropagation()
            if (confirm("Bạn có chắc chắn xoá chủ đề này")) {
                 var currentURL = window.location.href;
                 var parts = currentURL.split('/');
                 var lastTwoParams = parts.slice(-2);
                 var course_id = lastTwoParams[0];
                 var class_id = lastTwoParams[1];
                 const content = ref(database, `Content/${course_id}/${class_id}`);
                 console.log(course_id);
                 console.log(class_id);
                 const subjects = document.querySelectorAll('#accordionExample');
                 for (const subject of subjects) {
                     const title = subject.querySelector('#My-Subject').textContent;
                     get(content).then(snapshot => {
                         let content_list = snapshot.val();  
                         for(let i  =0; i < content_list.length; i++){
                            if(content_list[i]['Subject'] === title){
                                content_list.splice(i, 1);
                                set(content, content_list);
                            }
                         }
                         if(content_list === null){
                            remove(content)
                         }
                         window.location.reload()
                     });
                 }
             }
        })
    })
})
//     mydel.forEach(button => {
//         button.addEventListener('click', () => {
//             alert("What the heck");
//             console.log('Click');
//             if (confirm("Bạn có chắc chắn xoá chủ đề này")) {
//                 var currentURL = window.location.href;
//                 var parts = currentURL.split('/');
//                 var lastTwoParams = parts.slice(-2);
//                 var course_id = lastTwoParams[0];
//                 var class_id = lastTwoParams[1];
//                 const content = ref(database, `Content/${course_id}/${class_id}`);
//                 console.log(course_id);
//                 console.log(class_id);
//                 const subjects = document.querySelectorAll('#accordionExample');
//                 for (const subject of subjects) {
//                     const title = subject.querySelector('#My-Subject').textContent;
//                     get(content).then(snapshot => {
//                         let content_list = snapshot.val();
//                         const index = content_list.findIndex(item => item['Subject'] === title);
//                         if (index !== -1) {
//                             content_list.splice(index, 1);
//                             set(content, content_list);
//                         }
//                     });
//                 }
//             }
//         });
//     });
// });

 