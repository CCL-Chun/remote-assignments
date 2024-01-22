const titleWelcome = document.querySelector('.welcome-message');
let titleText = titleWelcome.querySelector('h1');

titleWelcome.addEventListener('click', function(){
    if(titleText.textContent === 'Welcome Message'){
        titleText.textContent = 'Have a Good Time!';
    } else {
        titleText.textContent = 'Welcome Message'
    }
})

const bottomCta = document.querySelector('.bottom');
const contentBoxes = document.querySelector('#wait-for-click')

bottomCta.addEventListener('click', function(){
    if(contentBoxes.style.display === 'none'){
        contentBoxes.removeAttribute('style');
    } else {
        contentBoxes.style.display = 'none';
    }
})