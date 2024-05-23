
const janelaCancelar = document.getElementById("janela_cancelar");
const janelaConfirmado = document.getElementById("janela_confirmado");

//função que ao clicar no botao vermelho aparece o alert de confirmação
function btnCancelar() {
    janelaCancelar.style.display = "block";
}
//função que ao clicar no botao vermelho o alert fecha
function btnRetornar() {
    janelaCancelar.style.display = "none";
}
// função que ao clicar em confirmar fecha janela
function confirmarCancelamento() {
    janelaCancelar.style.display = "none";
    janelaConfirmado.style.display = "block";
}
// função que ao clicar fora da janela fecha o alert
window.onclick = function (event) {
    if (event.target == janelaCancelar) {
        janelaCancelar.style.display = "none";
    }

    if (event.target == janelaConfirmado) {
        janelaConfirmado.style.display = "none";
    }
}