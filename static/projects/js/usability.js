console.log('Homes 2')

const onee = document.getElementById('first2')
const twoe = document.getElementById('second2')
const threee = document.getElementById('third2')
const foure = document.getElementById('fourth2')
const fivee = document.getElementById('fifth2')
const sixe = document.getElementById('sixth2')
const sevene = document.getElementById('seventh2')
const eighte = document.getElementById('eighth2')
const ninee = document.getElementById('ninth2')
const tene = document.getElementById('tenth2')

const form2 = document.querySelector('.rate-form2')
const confirmBox2 = document.getElementById('confirm-box2')
const csrf2 = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect2 = (size) => {
    const children = form2.children
    for (let i=0; i< children.length; i++){
        if(i<= size){
            children[i].classList.add('checked2')
        } else {
            children[i].classList.remove('checked2')
        }
    }
}


console.log(onee)
const handleSelect2 = (selection) => {
    switch(selection){
        case 'first2':{
            handleStarSelect2(1)
            return
        }
        case 'second2':{
            handleStarSelect2(2)
            return
        }
        case 'third2':{
            handleStarSelect2(3)
            return
        }
        case 'fourth2':{
            handleStarSelect2(4)
            return
        }
        case 'fifth2':{
            handleStarSelect2(5)
            return
        }
        case 'sixth2':{
            handleStarSelect2(6)
            return
        }
        case 'seventh2':{
            handleStarSelect2(7)
            return
        }
        case 'eighth2':{
            handleStarSelect2(8)
            return
        }
        case 'ninth2':{
            handleStarSelect2(9)
            return
        }
        case 'tenth2':{
            handleStarSelect2(10)
            return
        }
    }
}

const getNumericValue2 = (stringValue) =>{
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


if (onee){
    const arr = [onee, twoe, threee, foure, fivee, sixe, sevene, eighte, ninee, tene]

arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    handleSelect2(event.target.id)
}))

arr.forEach(item=> item.addEventListener('click', (event)=>{
    const val = event.target.id
    console.log(val)
    let isSubmit = false
    form2.addEventListener('submit', e=>{
        e.preventDefault()
        if (isSubmit){
            return
        }
        isSubmit = true
        const id = e.target.id
        console.log(id)
        const val_num = getNumericValue2(val)

        $.ajax({
            type: 'POST',
            url: '/rateusability/',
            data: {
                'csrf2middlewaretoken': csrf2[0].value,
                'el_id': id,
                'val': val_num,
            },
            success: function(response){
                console.log(response)
                confirmBox2.innerHTML = `<h6>Thank you for rating ${response.score} on usability <i class="fa-regular fa-face-smile-wink"></i></h6>`

            },
            error: function(error){
                console.log(error)
                confirmBox2.innerHTML = `<h6> Sorry, something went wrong on the server</h6>`
            }
        })
    })
}))

}

