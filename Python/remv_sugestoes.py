import pyautogui

# automatização especializada em remover sugestões indesejadas no google drive
# Após inicializar o programa não use o teclado
# Feito por: Kevin Ricardo

numeracao = 0
pyautogui.PAUSE = 5 # Tempo de espera entre cada comando do pyautogui
pyautogui.press('winleft')
pyautogui.write('chrome', interval=0.10)
pyautogui.press('right')
for x in range(2):
  pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('https://drive.google.com/drive/u/0/home', interval=0.10) 
pyautogui.press('enter')
pyautogui.write("", interval=0.10) # (Coloque o email de acesso à sua conta entre as aspas duplas)
pyautogui.press('enter') # botão avançar
pyautogui.write("", interval=0.10) # (Coloque a senha de acesso à sua conta entre as aspas simples)
pyautogui.press('enter') # botão avançar
while True:
  pyautogui.PAUSE = 3 # Tempo de espera entre cada comando
  pyautogui.press('a')
  pyautogui.press('left')
  pyautogui.press('a')
  pyautogui.press('end')
  pyautogui.press('enter')
  numeracao += 1
