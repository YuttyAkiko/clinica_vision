setTimeout(function () {
  window.location.href = "{% url 'paciente:geral-list' pk=request.user.paciente.pk %}";
}, 3000);  // Redireciona após 3 segundos (3000 milissegundos)