document.addEventListener('DOMContentLoaded', function () {
    /* Função para o smooth do scrool */
    const links = document.querySelectorAll('nav a');
    const offset = 100; // Ajuste o valor conforme necessário

    links.forEach(link => {
        link.addEventListener('click', function (event) {
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                event.preventDefault();
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - offset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});

window.addEventListener('scroll', function () {
    var arrowUp = document.getElementById('arrow-up');
    if (window.scrollY > 400) { // Exibir a seta após rolar 400px
        arrowUp.classList.add('visible');
        arrowUp.classList.remove('hidden');
    } else {
        arrowUp.classList.add('hidden');
        arrowUp.classList.remove('visible');
    }
});