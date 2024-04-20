const sideLinks = document.querySelectorAll('.sidebar .side-menu li ');
fetch("/check_id")
.then(respone =>{
    return respone.json()
})
.then(data =>{
    const name = data['Name']
    var hash = CryptoJS.MD5(name);
    var gravater = 'https://www.gravatar.com/avatar/' + hash + '?d=identicon'
    var image = document.createElement('img')
    image.src = gravater
    document.querySelector('.content nav .profile').appendChild(image)
})

sideLinks.forEach( item =>{
     item.addEventListener('click', () =>{
         const li = item.parentElement
         sideLinks.forEach( i =>{
             i.parentElement.classList.remove('active')
         })
         li.classList.add('active')
     })
})

const menuBar = document.querySelector('.content nav .bx.bx-menu');
const RmenuBar = document.querySelector('.content nav .notif');
const sideBar = document.querySelector('.sidebar');
window.addEventListener('DOMContentLoaded',() => {
    sideBar.style.display = "none"
    if(localStorage.getItem('sidebarState') == 'close'){
        sideBar.classList.add('close');
    }else{
        sideBar.classList.remove('close');
    }
    if(localStorage.getItem('theme') == 'dark'){
        document.body.classList.add('dark');
        document.querySelectorAll('.data-header').forEach( item =>{
            item.style.border = '2px var(--dark) solid'
            item.style.color = 'var(--dark)'
        })
        document.querySelectorAll('.data-recording').forEach( item =>{
            item.style.border = '2px var(--dark) solid'
            item.style.color = 'var(--dark)'
        })
        document.querySelectorAll('.content nav #dropdown .dropdown-item').forEach( item =>{
            item.style.color = 'var(--dark)'
            item.style.backgroundColor = 'var(--light)'
            document.querySelector('#logout').style.color ='red'
        })
        toggler.checked = true;
    }else{
        document.body.classList.remove('dark');
        document.querySelectorAll('.content nav #dropdown .dropdown-item').forEach( item =>{
            item.style.color = 'var(--dark)'
            item.style.backgroundColor = 'var(--light)'
            document.querySelector('#logout').style.color ='red'
        })
    }
    window.addEventListener('load', () =>{
        sideBar.style.display = ""
    })
})
menuBar.addEventListener('click', () => {
    sideBar.classList.toggle('close');
    if(sideBar.classList.contains('close')){
        localStorage.setItem('sidebarState','close')
    }else{
        localStorage.setItem('sidebarState','open')
    }
});
const searchBtn = document.querySelector('.content nav form .form-input button');
const searchBtnIcon = document.querySelector('.content nav form .form-input button .bx');
const searchForm = document.querySelector('.content nav form');



// window.addEventListener('resize', () => {
//     if (window.innerWidth < 768) {
//         sideBar.classList.add('close');
//     } else {
//         sideBar.classList.remove('close');
//     }
// });

const toggler = document.getElementById('theme-toggle');

toggler.addEventListener('change', function () {
    if (this.checked) {
        document.body.classList.add('dark');
        document.querySelectorAll('.data-header').forEach( item =>{
            item.style.border = '2px var(--dark) solid'
            item.style.color = 'var(--dark)'
        })
        document.querySelectorAll('.data-recording').forEach( item =>{
            item.style.border = '2px var(--dark) solid'
            item.style.color = 'var(--dark)'
        })
        document.querySelectorAll('.content nav #dropdown a:not(#logout)').forEach( item =>{
            item.style.color = 'var(--dark)'
            item.style.backgroundColor = 'var(--light)'
        })
        localStorage.setItem('theme','dark')
    } else {
        document.body.classList.remove('dark');
        document.querySelectorAll('.data-header').forEach( item =>{
            item.style.border = '2px var(--dark) solid'
            item.style.color = 'var(--dark)'
        })
        document.querySelectorAll('.data-recording').forEach( item =>{
            item.style.border = '2px var(--dark) solid'
            item.style.color = 'var(--dark)'
        })
        document.querySelectorAll('.content nav #dropdown a:not(#logout)').forEach( item =>{
            item.style.color = 'var(--dark)'
            item.style.backgroundColor = 'var(--light)'
        })
        localStorage.setItem('theme','light')
    }
});