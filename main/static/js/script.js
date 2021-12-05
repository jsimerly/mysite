function dropDown() {
    document.getElementById('account-dropdown').classList.toggle('show')
}

function selectBet() {
    // document.write(5)
    // document.classList.toggle('bet-selected')
    document.getElementsByClassName('.totalSpread')[0].classList.toggle('bet-selected')
}

window.onclick = function(event){
    if (!event.target.matches('.account-btn')) {
        var dropdowns = document.getElementsByClassName('dropdown-content');
        var i;
        
        for (i=0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')){
                openDropdown.classList.remove('show')
            }
        }
    }
}