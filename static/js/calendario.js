const daysTag = document.querySelector('.dias');
const currentDate = document.querySelector('#data-atual');
const prevNextIcon = document.querySelectorAll('.icons span');

// Recebendo nova data, mês e ano atual
let date = new Date();
currYear = date.getFullYear();
currMonth = date.getMonth();

const months = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'];

const renderCalendar = () => {
    let firstDayofMonth = new Date(currYear, currMonth, 1).getDay(),
    //Recebendo o primeiro dia do mês
    lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(),
    // Recebendo a última data do mês
    lastDayofMonth = new Date(currYear, currMonth, lastDateofMonth).getDay(),
    // Recebendo o último dia do mês
    lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate();
    // Recebendo a última data do mês anterior

    let liTag = '';

    for(let i = firstDayofMonth; i > 0; i--) {
        // Criando li com últimos dias do mês anterior
        liTag += `<li class='inactive'>${lastDateofLastMonth - i + 1}</li>`;
    }

    for (let i = 1; i <= lastDateofMonth; i++) {
        // Criando li para todos os dias do mês atual
        // Adicionando classe ativa a li dia, mês e ano atuais
        let isToday = i === date.getDate() && currMonth === new Date().getMonth() 
                            && currYear === new Date().getFullYear() ? 'active' : '';
        liTag += `<li class='${isToday}'>${i}</li>`;
    }

    for (let i = lastDayofMonth; i < 6; i++) {
        // Criando li do próximo mês, primeiros dias
        liTag += `<li class='inactive'>${i - lastDayofMonth + 1}</li>`;
    }

    currentDate.innerHTML = `${months[currMonth]} ${currYear}`; // Passando mês e ano atual como texto de currentDate

    daysTag.innerHTML = liTag;
}

renderCalendar();

prevNextIcon.forEach(icons => { // Buscando icones prev e next
    icons.addEventListener('click', () => { // Adicionando evento de click nos icones
        // se o ícone clicado for o ícone anterior, diminua o mês atual caso contrário, incrementa 1
        currMonth = icons.id === 'prev' ? currMonth - 1 : currMonth + 1;

        if(currMonth < 0 || currMonth > 11) { // Se o mês atual for menor que 0 ou maior que 11
            // criando uma nova data do ano e mês atual e passando como valor de data
            date = new Date(currYear, currMonth, new Date().getDate());
            currYear = date.getFullYear(); // Atualizando o ano atual com o nova data do ano
            currMonth = date.getMonth(); // Atualizando o mês atual com o novo mês
        } else {
            date = new Date(); // Passa o valor de data para a data atual
        }
        renderCalendar(); // Chamando a função renderCalendar
    });
});