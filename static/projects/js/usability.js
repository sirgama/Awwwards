console.log('Homes 2')

const one = document.getElementById('first2')
const two = document.getElementById('second2')
const three = document.getElementById('third2')
const four = document.getElementById('fourth2')
const five = document.getElementById('fifth2')
const six = document.getElementById('sixth2')
const seven = document.getElementById('seventh2')
const eight = document.getElementById('eighth2')
const nine = document.getElementById('ninth2')
const ten = document.getElementById('tenth2')

const form = document.querySelector('.rate-form2')
const confirmBox = document.getElementById('confirm-box2')
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
        case 'first2':{
            handleStarSelect(1)
            return
        }
        case 'second2':{
            handleStarSelect(2)
            return
        }
        case 'third2':{
            handleStarSelect(3)
            return
        }
        case 'fourth2':{
            handleStarSelect(4)
            return
        }
        case 'fifth2':{
            handleStarSelect(5)
            return
        }
        case 'sixth2':{
            handleStarSelect(6)
            return
        }
        case 'seventh2':{
            handleStarSelect(7)
            return
        }
        case 'eighth2':{
            handleStarSelect(8)
            return
        }
        case 'ninth2':{
            handleStarSelect(9)
            return
        }
        case 'tenth2':{
            handleStarSelect(10)
            return
        }
    }
}

const getNumericValue = (stringValue) =>{
    let numericValue;
    if (stringValue === 'first2'){
        numericValue = 1
    }
    else if (stringValue === 'second2'){
        numericValue = 2
    }
    else if (stringValue === 'third2'){
        numericValue = 3
    }
    else if (stringValue === 'fourth2'){
        numericValue = 4
    }

    else if (stringValue === 'fifth2'){
        numericValue = 5
    }
    else if (stringValue === 'sixth2'){
        numericValue = 6
    }
    else if (stringValue === 'seventh2'){
        numericValue = 7
    }
    else if (stringValue === 'eighth2'){
        numericValue = 8
    }
    else if (stringValue === 'ninth2'){
        numericValue = 9
    }
    else if (stringValue === 'tenth2'){
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
            url: '/rate2/',
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'el_id': id,
                'val': val_num,
            },
            success: function(response){
                console.log(response)
                confirmBox.innerHTML = `<h6>You have rated design with ${response.score}</h6>`

            },
            error: function(error){
                console.log(error)
                confirmBox.innerHTML = `<h6> Sorry, something went wrong on the server</h6>`
            }
        })
    })
}))

}

