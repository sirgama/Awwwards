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

console.log(one)

const arr = [one, two, three, four, five, six, seven, eight, nine, ten]

arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    console.log(event.target)
}))