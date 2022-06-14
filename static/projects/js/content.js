console.log('Homes 3')

const oneee = document.getElementById('first23')
const twoee = document.getElementById('second23')
const threeee = document.getElementById('third23')
const fouree = document.getElementById('fourth23')
const fiveee = document.getElementById('fifth23')
const sixee = document.getElementById('sixth23')
const sevenee = document.getElementById('seventh23')
const eightee = document.getElementById('eighth23')
const nineee = document.getElementById('ninth23')
const tenee = document.getElementById('tenth23')

const form23 = document.querySelector('.rate-form23')
const confirmBox23 = document.getElementById('confirm-box23')
const csrf23 = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect23 = (size) => {
    const children = form23.children
    for (let i=0; i< children.length; i++){
        if(i<= size){
            children[i].classList.add('checked3')
        } else {
            children[i].classList.remove('checked3')
        }
    }
}


console.log(onee)
const handleSelect23 = (selection) => {
    switch(selection){
        case 'first23':{
            handleStarSelect23(1)
            return
        }
        case 'second23':{
            handleStarSelect23(2)
            return
        }
        case 'third23':{
            handleStarSelect23(3)
            return
        }
        case 'fourth23':{
            handleStarSelect23(4)
            return
        }
        case 'fifth23':{
            handleStarSelect23(5)
            return
        }
        case 'sixth23':{
            handleStarSelect23(6)
            return
        }
        case 'seventh23':{
            handleStarSelect23(7)
            return
        }
        case 'eighth23':{
            handleStarSelect23(8)
            return
        }
        case 'ninth23':{
            handleStarSelect23(9)
            return
        }
        case 'tenth23':{
            handleStarSelect23(10)
            return
        }
    }
}

const getNumericValue23 = (stringValue) =>{
    let numericValue;
    if (stringValue === 'first23'){
        numericValue = 1
    }
    else if (stringValue === 'second23'){
        numericValue = 2
    }
    else if (stringValue === 'third23'){
        numericValue = 3
    }
    else if (stringValue === 'fourth23'){
        numericValue = 4
    }

    else if (stringValue === 'fifth23'){
        numericValue = 5
    }
    else if (stringValue === 'sixth23'){
        numericValue = 6
    }
    else if (stringValue === 'seventh23'){
        numericValue = 7
    }
    else if (stringValue === 'eighth23'){
        numericValue = 8
    }
    else if (stringValue === 'ninth23'){
        numericValue = 9
    }
    else if (stringValue === 'tenth23'){
        numericValue = 10
    }
    else {
        numericValue = 0
    }
    return numericValue
}


if (oneee){
    const arr = [oneee, twoee, threeee, fouree, fiveee, sixee, sevenee, eightee, nineee, tenee]

arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    handleSelect23(event.target.id)
}))

arr.forEach(item=> item.addEventListener('click', (event)=>{
    const val = event.target.id
    console.log(val)
    let isSubmit = false
    form23.addEventListener('submit', e=>{
        e.preventDefault()
        if (isSubmit){
            return
        }
        isSubmit = true
        const id = e.target.id
        console.log(id)
        const val_num = getNumericValue23(val)

        $.ajax({
            type: 'POST',
            url: '/ratecontent/',
            data: {
                'csrf2middlewaretoken': csrf23[0].value,
                'el_id': id,
                'val': val_num,
            },
            success: function(response){
                console.log(response)
                confirmBox23.innerHTML = `<h6>Rated ${response.score}. Thanks for your content rating feedback <i class="fa-regular fa-face-grin"></i></h6>`

            },
            error: function(error){
                console.log(error)
                confirmBox23.innerHTML = `<h6> Sorry, something went wrong on the server</h6>`
            }
        })
    })
}))

}

