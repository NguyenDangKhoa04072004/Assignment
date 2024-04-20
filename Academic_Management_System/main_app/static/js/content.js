const content = document.querySelectorAll('.content-material')
content.forEach( item =>{
    item.addEventListener('click',()=>{
        console.log("click")
    })
})