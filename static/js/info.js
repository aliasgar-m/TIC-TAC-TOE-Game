// HTML variables
const returnDiv = document.querySelector('.return');

//functions
const handleReturn = (e) => {
    history.back()
}

//event listeners
returnDiv.addEventListener('click', handleReturn);