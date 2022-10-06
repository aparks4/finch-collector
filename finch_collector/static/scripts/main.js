console.log("js file connected")
const addBtns = document.getElementsByClassName('add-to-album-btn');
const dropdowns = document.getElementsByClassName('dropdown');

for (let i = 0; i < addBtns.length; i++) {
    addBtns[i].addEventListener('click', function() {
        console.log('button clicked');
        dropdowns[i].style.visibility = "visible";
    })
}






