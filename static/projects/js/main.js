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

const getNumericValue = (stringValue) =>{
    let numericValue;
    if (stringValue === 'first'){
        numericValue = 1
    }
    else if (stringValue === 'second'){
        numericValue = 2
    }
    else if (stringValue === 'third'){
        numericValue = 3
    }
    else if (stringValue === 'fourth'){
        numericValue = 4
    }

    else if (stringValue === 'fifth'){
        numericValue = 5
    }
    else if (stringValue === 'sixth'){
        numericValue = 6
    }
    else if (stringValue === 'seventh'){
        numericValue = 7
    }
    else if (stringValue === 'eighth'){
        numericValue = 8
    }
    else if (stringValue === 'ninth'){
        numericValue = 9
    }
    else if (stringValue === 'tenth'){
        numericValue = 10
    }
    else {
        numericValue = 0
    }
    return numericValue
}


if (one){
    const arr = [one, two, three, four, five, six, seven, eight, nine, ten]

arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    handleSelect(event.target.id)
}))

arr.forEach(item=> item.addEventListener('click', (event)=>{
    const val = event.target.id
    console.log(val)
    let isSubmit = false
    form.addEventListener('submit', e=>{
        e.preventDefault()
        if (isSubmit){
            return
        }
        isSubmit = true
        const id = e.target.id
        console.log(id)
        const val_num = getNumericValue(val)

        $.ajax({
            type: 'POST',
            url: '/rate/',
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'el_id': id,
                'val': val_num,
            },
            success: function(response){
                console.log(response)
                confirmBox.innerHTML = `<h6>Thanks for your feedback <i class="fa-regular fa-face-laugh-beam"></i>. You have rated ${response.score} on design.</h6>`

            },
            error: function(error){
                console.log(error)
                confirmBox.innerHTML = `<h6> Sorry, something went wrong on the server</h6>`
            }
        })
    })
}))

}

