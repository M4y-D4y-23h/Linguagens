import keyboard as kb
import os

# Esse programa tem a finalidade de ser um exemplo da troca de senha pelo CMD com os seguintes comandos: net user [usuario] [nova senha].
# Pois o mesmo oculta o cursor na entrada da nova senha.
# Por: Kevin Ricardo.

def senha_oculta(codenome):
  print("Repita seu codenome sigilosamente: (em seguida aperte enter)")
  usuario = input(kb.record(until='enter'))
  os.system('cls')
  print("Senha correta") if usuario == codenome else print("Senha incorreta") # Operador ternário

codenome = input("Seu codename: ")
senha_oculta(codenome)
