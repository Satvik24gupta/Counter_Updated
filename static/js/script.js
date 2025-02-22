let counter_array= JSON.parse(localStorage.getItem('counter_array')) ||
[{
    "id": 1,
    "value":0
}]

document.addEventListener("DOMContentLoaded", ()=>{
    fetch('/get_counters', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
    })
    .then(response=> response.json())
    .then(data=> {
        counter_array = data;
        saveList();
        updateState(counter_array);
    })
})

let current_id=1;

function saveList(){
    localStorage.setItem('counter_array', JSON.stringify(counter_array));
}

function addCounter(){
    fetch('/add_counter')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        counter_array=data;
        saveList();
        updateState(counter_array);
    })
}

function increment(id) {
    current_id=id;
    fetch('/increment_counter', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id:id})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        counter_array=data;
        saveList();
        updateState(counter_array);
    }) 
}

function decrement(id) {
    current_id=id;
    fetch('/decrement_counter', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id:id})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        counter_array=data;
        saveList();
        updateState(counter_array);
    })
}
function reset(id) {
    current_id=id;
    fetch('/reset_counter', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id:id})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        counter_array=data;
        saveList();
        updateState(counter_array);
    })
}

function remove(id){
    var ans=confirm("Are you sure you want to delete this counter, This process can not be undone");
    if(!ans) return
    // for(let i=0;i<counter_array.length;i++){
    //     if(counter_array[i].id==id){
    //         counter_array.splice(i,1);
    //         break;
    //     }
    // }
    fetch('/delete_counter', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id:id})
    })
    .then(response => response.json())
    .then(data=>{
        console.log(data);
        counter_array=data;
        saveList();
        updateState(counter_array);
    })
}

function updateState(newState){
    let container=document.getElementById("container");
    container.innerText="";
    counter_array.forEach((item)=>{
        const counter=document.createElement('div')
        const name=document.createElement('input')
        name.setAttribute('placeholder', 'Enter Name')
        name.addEventListener(('click'), (e)=>{
            name.select();
            e.stopPropagation()
        })
        name.addEventListener(('blur'), (e)=>{
            item.name=e.target.value
            saveList();
            updateState(counter_array)
        })
        name.textContent=item.name
        name.value=item.name||"";
        const value = document.createElement('div');
        const controller = document.createElement('div');
        const increment = document.createElement('button');
        const decrement = document.createElement('button');
        const reset = document.createElement('button');
        const removeButton = document.createElement('button');
        value.classList.add("value")
        value.textContent=item.value;
        controller.classList.add("controller")
        increment.classList.add("increment");
        increment.textContent="+";
        decrement.classList.add("decrement");
        decrement.textContent="-";
        reset.classList.add("reset");
        reset.textContent="Reset";
        removeButton.classList.add("remove")
        removeButton.textContent="x";
        removeButton.setAttribute('onclick', `remove(${item.id})`)
        controller.appendChild(increment);
        controller.appendChild(decrement);
        controller.appendChild(reset);
        counter.classList.add("counter");
        counter.appendChild(name)
        counter.appendChild(removeButton)
        counter.appendChild(value);
        counter.appendChild(controller);
        container.appendChild(counter)
        increment.setAttribute('onclick', `increment(${item.id})`)
        decrement.setAttribute('onclick', `decrement(${item.id})`)
        reset.setAttribute('onclick', `reset(${item.id})`)
        counter.onclick=()=>{
            counter.classList.add("selected")
            current_id=item.id;
            saveList();
            updateState();
        }
        if(current_id==item.id){
            counter.classList.add("selected")
        }
    })
}

document.addEventListener('keydown', function(e) {
    if ((e.key === '+') || e.key==' ' || (e.key === 'Enter') || (e.key === 'ArrowRight') || (e.key === 'ArrowUp') || e.key === "=") {
        increment(current_id);
    }
})

document.addEventListener('keydown',(e)=>{
    if(e.key=='-' || (e.key === 'ArrowDown') || (e.key === 'ArrowLeft') || (e.key === "Backspace")){
        decrement(current_id);
    }
})

document.addEventListener('keydown', function(e) {
    if (e.code === 'Space' ||e.key==='ArrowDown') { // Check if the pressed key is the Spacebar
        e.preventDefault(); // Prevent the default action (scrolling)
    }
});

updateState(counter_array);


function resetAllName(){
    var ans=confirm("Are you sure you want to reset names of all counters?");
    if(!ans) return
    counter_array.forEach((item)=>{
        item.name=""
    })
    updateState(counter_array)
    saveList()
}

function resetAllValue(){
    var ans=confirm("Are you sure you want to reset values of all counters?");
    if(!ans) return
    // counter_array.forEach((item)=>{
    //     item.value="0"
    // })
    fetch('/reset_all_counter_value', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
    .then(response => response.json())
    .then(data=>{
        console.log(data);
        counter_array=data;
        saveList();
        updateState(counter_array);
    })
}

function deleteAll(){
    var ans=confirm("Are you sure you want to delete all counters?");
    if(!ans) return
    counter_array=[]
    saveList()
    updateState()
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}