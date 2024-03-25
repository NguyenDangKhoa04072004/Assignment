const sideLinks = document.querySelectorAll('.sidebar .side-menu li a:not(.logout)');
var hash = CryptoJS.MD5('message');
var gravater = 'https://www.gravatar.com/avatar/' + hash + '?d=identicon'
var image = document.createElement('img')
image.src = gravater
document.querySelector('.content nav .profile').appendChild(image)
sideLinks.forEach(item => {
    const li = item.parentElement;
    var click ;
    item.addEventListener('click', () => {
        li.classList.add('active');  
    })
});
const menuBar = document.querySelector('.content nav .bx.bx-menu');
const RmenuBar = document.querySelector('.content nav .notif');
const sideBar = document.querySelector('.sidebar');
const RsideBar = document.querySelector('.Rsidebar')
window.addEventListener('DOMContentLoaded',() => {
    if(localStorage.getItem('sidebarState') == 'close'){
        sideBar.classList.add('close');
    }else{
        sideBar.classList.remove('close');
    }
    if(localStorage.getItem('theme') == 'dark'){
        document.body.classList.add('dark');
        document.querySelectorAll('th').forEach( item =>{
            item.style.border = '2px white solid'
            item.style.color = '#fbfbfb'
        })
        document.querySelectorAll('td').forEach( item =>{
            item.style.border = '2px white solid'
            item.style.color = '#fbfbfb'
        })
        document.querySelectorAll('.content nav #dropdown a').forEach( item =>{
            item.style.color = 'white'
            item.style.backgroundColor = 'black'
        })
        toggler.checked = true;
    }else{
        document.body.classList.remove('dark');
        document.querySelectorAll('.content nav #dropdown a').forEach( item =>{
            item.style.color = 'black'
            item.style.backgroundColor = 'white'
        })
    }
})
menuBar.addEventListener('click', () => {
    sideBar.classList.toggle('close');
    if(sideBar.classList.contains('close')){
        localStorage.setItem('sidebarState','close')
    }else{
        localStorage.setItem('sidebarState','open')
    }
});
RmenuBar.addEventListener('click', ()=>{
      RsideBar.classList.toggle('close');
})
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
        document.querySelectorAll('th').forEach( item =>{
            item.style.border = '2px white solid'
            item.style.color = '#fbfbfb'
        })
        document.querySelectorAll('td').forEach( item =>{
            item.style.border = '2px white solid'
            item.style.color = '#fbfbfb'
        })
        document.querySelectorAll('.content nav #dropdown a').forEach( item =>{
            item.style.color = 'white'
            item.style.backgroundColor = 'black'
        })
        localStorage.setItem('theme','dark')
    } else {
        document.body.classList.remove('dark');
        document.querySelectorAll('th').forEach( item =>{
            item.style.border = '2px black solid'
            item.style.color = 'black'
        })
        document.querySelectorAll('td').forEach( item =>{
            item.style.border = '2px black solid'
            item.style.color = 'black'
        })
        document.querySelectorAll('.content nav #dropdown a').forEach( item =>{
            item.style.color = 'black'
            item.style.backgroundColor = 'white'
        })
        localStorage.setItem('theme','light')
    }
});