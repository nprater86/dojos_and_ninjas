let dojoNameVal = document.getElementById('dojoName');

function checkDojoName(event){
    if (!dojoNameVal.value){
        event.preventDefault();
        alert('Please enter a Dojo Name!')
    }
}

let dojoSelect = document.getElementById('dojoSelect');
let first_name = document.getElementById('first_name');
let last_name = document.getElementById('last_name');
let age = document.getElementById('age');

function checkNinjaVals(event){
    if (dojoSelect.value == 'default'){
        event.preventDefault;
        alert('Please select a Dojo!');
    } else if (!first_name.value){
        event.preventDefault;
        alert('Please enter first name!');
    } else if (!last_name.value){
        event.preventDefault;
        alert('Please enter last name!');
    } else if (!age.value){
        event.preventDefault;
        alert('Please enter age!');
    }
}