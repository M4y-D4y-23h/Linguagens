
// Essa é uma função em JavaScript que valida os CPF´s repassados à ela, foi feita em classe integrada à uma página HTML.
// Adaptado por: Kevin Ricardo

testaCPF = function(strCPF) {
  var soma;
  var resto;
  soma = 0;
if (strCPF == "00000000000") return false;
for (i=1; i<=9; i++) soma = soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
resto = (soma * 10) % 11;
  if ((resto == 10) || (resto == 11)) resto = 0;
  if (resto != parseInt(strCPF.substring(9, 10)) ) return false;
soma = 0;
  for (i=1; i<=10; i++) soma = soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);
  resto = (soma * 10) % 11;
  if ((resto == 10) || (resto == 11)) resto = 0;
  if (resto != parseInt(strCPF.substring(10, 11)) ) return false;
  return true;
}

document.addEventListener('DOMContentLoaded', function() {
  const button = document.querySelector('.button');
  const input = document.querySelector('.input')
  input.addEventListener('change', function() {
    const cpf = input.value
    if (testaCPF(cpf)) {
      alert('CPF válido')
    } else {
      alert('CPF inválido')
    }
  });
});
