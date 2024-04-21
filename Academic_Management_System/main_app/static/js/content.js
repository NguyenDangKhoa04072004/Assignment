const content = document.querySelectorAll('.content-material')
content.forEach( item =>{
    item.addEventListener('click',()=>{
        console.log("click")
    })
})

const buttonDel = document.querySelector('#delSubject')
buttonDel.addEventListener('click',(event)=>{
     event.stopPropagation()
     console.log("Click ")
})