console.log('Homes ')

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')
const six = document.getElementById('sixth')
const seven = document.getElementById('seventh')
const eight = document.getElementById('eighth')
const nine = document.getElementById('ninth')
const ten = document.getElementById('tenth')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
    const children = form.children
    for (let i=0; i< children.length; i++){
        if(i<= size){
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}


console.log(one)
const handleSelect = (selection) => {
    switch(selection){
        case 'first':{
            handleStarSelect(1)
            return
        }
        case 'second':{
            handleStarSelect(2)
            return
        }
        case 'third':{
            handleStarSelect(3)
            return
        }
        case 'fourth':{
            handleStarSelect(4)
            return
        }
        case 'fifth':{
            handleStarSelect(5)
            return
        }
        case 'sixth':{
            handleStarSelect(6)
            return
        }
        case 'seventh':{
            handleStarSelect(7)
            return
        }
        case 'eighth':{
            handleStarSelect(8)
            return
        }
        case 'ninth':{
            handleStarSelect(9)
            return
        }
        case 'tenth':{
            handleStarSelect(10)
            return
        }
    }
}
if (one){
    const arr = [one, two, three, four, five, six, seven, eight, nine, ten]

arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    handleSelect(event.target.id)
}))

}

