function mostrarMenu() {
    document.getElementById("mostrarMenu").classList.toggle("mostrarMenu");
}

function menuClinica() {
    document.getElementById("menuClinica").classList.toggle("mostrarMenu");
}

window.onclick = (event) => {
    let menu = document.getElementsByClassName("cabecalho__menu");
    if (event.target == menu) {
        menu.style.display = none;
    }
}