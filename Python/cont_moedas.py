import os
from time import sleep

# Esse programa tem a finalidade de otimizar a contagem do valor de moedas somente pela quantidade de cada uma
# Feito por: Kevin Ricardo

resultado = 0
print("Coloque a quantidade de moedas na seguinte ordem: 1 centavos (espaço) 5 centavos (espaço) 10 centavos (espaço) 50 centavos (espaço) 1 real")
print("Exemplo: 1 1 1 1 1")
print("Sem escrever os '(espaços)'")
print("Ou enter para encerrar o programa\n")
while True:
  def moedas(resultado):
    try:
      moedas = [float(x) for x in input("Quantidades: ").split()]
      if moedas == []:
        resultado = []
      if len(moedas) > 4:
        for x in range(4, len(moedas)-1):
          moedas.pop()
      if moedas != None:
        if len(moedas) > 0:
          moedas_1cent = 0.01 * moedas[0]
          resultado += moedas_1cent
          if len(moedas) > 1:
            moedas_5cent = 0.05 * moedas[1]
            resultado += moedas_5cent
            if len(moedas) > 2:
              moedas_10cent = 0.10 * moedas[2]
              resultado += moedas_10cent
              if len(moedas) > 3:
                moedas_50cent = 0.50 * moedas[3]
                resultado += moedas_50cent
                if  len(moedas) > 4:
                  moedas_1real = 1 * moedas[4]
                  resultado += moedas_1real
      return resultado
    except:
      os.system("cls")
      print("Dado_inválido")
      sleep(1.5)
      return resultado
  resultado = moedas(resultado)
  if resultado == []:
    os.system('cls')
    break
  print("valor retornado:",format(resultado,'.2f'),"\n")
