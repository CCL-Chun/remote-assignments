# Practice HTML DOM and Event Handling
## Request 1: Click to Change Text
  - When user clicks on "Welcome Message" block, change text to "Have a Good Time!"
```
const titleWelcome = document.querySelector('.welcome-message'); // <section class="welcome-message">
let titleText = titleWelcome.querySelector('h1'); // <h1> under <section class="welcome-message">

titleWelcome.addEventListener('click', function(){ // listen to the action on <section class="welcome-message">
    if(titleText.textContent === 'Welcome Message'){
        titleText.textContent = 'Have a Good Time!';
    } else {
        titleText.textContent = 'Welcome Message'
    }
})

```
## Request 2: Click to Show More Content Boxes
  - When user clicks the Call-to-Action button, show those hidden content boxes
```
const bottomCta = document.querySelector('.bottom'); // <div class="bottom">
const contentBoxes = document.querySelector('#wait-for-click') //<section class="content" id="wait-for-click" style="display: none;">

bottomCta.addEventListener('click', function(){ // listen to the action on <div class="bottom">
    if(contentBoxes.style.display === 'none'){ // style="display: none;" as default
        contentBoxes.removeAttribute('style'); // just remove the attribute to show it
    } else {
        contentBoxes.style.display = 'none'; // add the attribute as 'none' to hide it after another click
    }
})
```
