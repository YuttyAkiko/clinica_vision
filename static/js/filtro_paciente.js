function changePlaceholder() {
    var select = document.getElementById("tipo_select");
    var input = document.getElementById("tipo_input");

    if (select.value === "nome") {
        input.placeholder = "Digite o nome";
    } else if (select.value === "cpf") {
        input.placeholder = "Digite o CPF";
    }
}
