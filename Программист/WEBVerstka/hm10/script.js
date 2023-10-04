const PopUpMenu = document.querySelector('.pop-up_menu');
const Burger = document.querySelector('.burger');

function toggleMenu() {
    PopUpMenu.classList.toggle('hidden');
}

Burger.addEventListener('click', toggleMenu);
