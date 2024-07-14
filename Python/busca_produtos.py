# BIBLIOTECAS >>
from email.message import EmailMessage
from tabulate import tabulate
from datetime import datetime
from bs4 import BeautifulSoup
from time import sleep
import requests
import smtplib
import os

# Esse código tem a finalidade de poupar tempo e dinheiro fazendo a busca de produtos em diversos sites ao mesmo tempo
# Afim de retornar o produto mais barato e mais bem avaliado ao consumidor
# Feito por: Kevin Ricardo - 2023

# Códigos webscraping tendem a ser instáveis ao longo do tempo devido a modificações que ocorrem nos sites
# necessitando assim suporte e correções periodicamente pra evitar falhas na aplicação

# Declaração de variaveis globais
listaLinks,listaTitulos,listaPrecos,listaProdutos, listaLojas = [""]*99, [""]*99, [0.0]*99, [""]*99, [""]*99  #  variavel global
produto = str("")  #  variavel global
sites = ["https://www.zoom.com.br"]

#  começo do programa
email = str(input("Email que será enviado o relatorio:\t"))
#  Data atual
data_atual = datetime.now() #  retorno data atual

def pesquisaProduto():
    os.system("cls") #  limpar console
    # variaveis para armazenar busca
    pesquisaPrecos, pesquisaTitulos, pesquisaLinks, pesquisaLojas = [0.0]*24, [""]*24, [""]*24, [""]*24
    # Inicio do codigo
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    while True:
      print("\nDigite 0 para voltar")
      produto = str(input("\nColoque o produto que deseja:\t"))
      produto = produto.lower()
      if (produto == '0' or produto == ''):
        os.system("cls") # limpar console
        break
      try:
        for y in range( len(listaProdutos) ):
          if (listaProdutos[y] != ""):
            continue

          # Adiciona produto à lista
          if (listaProdutos[y] == ""):
            listaProdutos[y] = produto
            
          print("\nPesquisando..")
          sleep(1)
          os.system("cls")
          # Busca usando link e produto
          
          URL = 'https://www.zoom.com.br/search?q='
          site = requests.get(URL + produto, headers)
          soup = BeautifulSoup(site.content, 'html5lib')

          # Produtos achado pelo código html
          soup2 = soup.find_all('div', class_='Paper_Paper__4XALQ Paper_Paper__bordered__cl5Rh Card_Card__Zd8Ef Card_Card__clicable__ewI68 ProductCard_ProductCard__WWKKW')
          soup = soup.find_all('div', class_='Paper_Paper__4XALQ Paper_Paper__bordered__cl5Rh Card_Card__Zd8Ef Card_Card__clicable__ewI68 ProductCard_ProductCard__WWKKW')
          soup = soup+soup2
          # Pesquisa no código html pelas informações
          for x in range(0, len(soup)):
          # Pesquisa nas classes de cada div
            title = soup[x].find('h2', class_='Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ').get_text()
            link = soup[x].find('a', class_='ProductCard_ProductCard_Inner__gapsh')
            loja = soup[x].find('h3', class_='Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_MobileLabelSAtLarge__m0whD ProductCard_ProductCard_BestMerchant__JQo_V').get_text()
            preco = soup[x].find('p', class_='Text_Text__ARJdp Text_MobileHeadingS__HEz7L').get_text()
            # tirando caracteres da variavel 'preco'
            preco = preco.translate(str.maketrans('','','R$'))
            preco = preco.replace('.','')
            preco = preco.replace(',','.')
            preco = float(preco)

            # armazenando valores nas listas locais da função
            if (pesquisaTitulos[x] == ""):
              pesquisaTitulos[x] = title
            else:
              pesquisaTitulos[x] = title
              
            if (pesquisaLojas[x] == ""):
              pesquisaLojas[x] = loja
            else:
              pesquisaLojas[x] = loja
              
            if (pesquisaPrecos[x] == 0.0):
              pesquisaPrecos[x] = preco
            else:
              pesquisaPrecos[x] = preco
              
            if (pesquisaLinks[x] == ""):
              pesquisaLinks[x] = "https://www.zoom.com.br/"+link.get('href')
            else:
              pesquisaLinks[x] = "https://www.zoom.com.br/"+link.get('href')

            # Retornando menor preço
            if (x >= 1):
              if (preco > pesquisaPrecos[x-1]):
                
                preco = pesquisaPrecos[x-1]
                pesquisaPrecos[x] = preco
                
                title =  pesquisaTitulos[x-1]
                pesquisaTitulos[x] = title
                
                link =  pesquisaLinks[x-1]
                pesquisaLinks[x] = link
                
                loja = pesquisaLojas[x-1]
                pesquisaLojas[x] = loja
                
          print("|----------------------",
          "\n| >> Nome do produto:", title,
          "\n|----------------------\n",)
          print("|----------------------",
          "\n| >> Nome do produto:", preco,
          "\n|----------------------\n",)
          print("|----------------------",
          "\n| >> Loja com menor preço:", loja,
          "\n|----------------------\n",)
          print("|----------------------",
          "\n| >> Link:", pesquisaLinks[x],
          "\n|----------------------\n",)
                
          # armazenando valores nas listas globais do codigo
          for x in range(0, len(listaProdutos)):
            if (listaPrecos[x] == 0.0):
              for y in range(23, 24):
                listaLojas[x] = pesquisaLojas[y]
                listaPrecos[x] = pesquisaPrecos[y]
                listaTitulos[x] = pesquisaTitulos[y]
                listaLinks[x] = pesquisaLinks[y]
            else:
              continue
            break
          sleep(5)
          os.system("cls")
          break
      except:
        os.system("cls")
        print("Nenhum resultado encontrado")
        sleep(2)
        break

def envioEmail(): 
  # Buscando produtos para a mensagem
  tam_list = 0
  for x in range(0, len(listaPrecos)):
    if (listaPrecos[x] != 0.0):
      tam_list = tam_list+1
  for y in range(tam_list-1, tam_list):
      title1 = listaTitulos[y]
      loja1 = listaLojas[y]
      preco1 = listaPrecos[y]
      link1 = listaLinks[y]
    
  # Conteúdo da mensagem
  email_Content = f"""
  <html>
  <body>
  
  <h4> Sua consulta foi recebida! </h4>
  <p> Muito obrigado pela credibilidade </p>
  <h4> Produtos com menores preços e maior relevância: </h4>
  <p> - nome do produto: {title1}</p>
  <p> - Loja com menor preço: {loja1}</p>
  <p> - Produto com menor preço: R$ {preco1}</p>
  <p> - Link do produto: {link1}</p>
  
  <h4> Sites Pesquisados: </h4>
  <a href="https://www.zoom.com.br/"> Zoom Website</a><br>
  </body>
  </html>"""

  # Preparando mensagem
  msg = EmailMessage()
  msg['Subject'] = "Resultados Pesquisa Busca de Preços!"
  msg['From'] = "(Coloque o e-mail que fará o envio das mensagens)"
  msg['To'] = email
  password = '' # É imprescindivel uma senha de app dos e-mails que enviaram a mensagem
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(email_Content)

  # Envio da mensagem ao destinatário
  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

# começo do loop principal
codigo = bool(True)
while (codigo == True):
  os.system("cls")   #  limpar console"
  
# Tabela de opções principal
  print(f"Data: {data_atual.day}:{data_atual.month}:{data_atual.year}")
  print("Seu email:",email)
  print("Qual opção deseja?\n\n")
  print("|----------------------",
        "\n|0. >> Fechar o programa",
        "\n|----------------------\n",)
  
  print("|----------------------",
        "\n|1. >> Pesquisar Produto",
        "\n|----------------------\n",)
        
  print("|----------------------",
        "\n|2. >> Verificar Tabela",
        "\n|----------------------\n",)
  
  print("|----------------------",
        "\n|3. >> Checar resultados e enviar email",
        "\n|----------------------\n",)
  
  print("|----------------------",
        "\n|4. >> Sites",
        "\n|----------------------\n",)
  
  print("|----------------------",
        "\n|5. >> Email",
        "\n|----------------------\n",)
  
  print("|----------------------",
        "\n|6. >> Tutorial uso do programa",
        "\n|----------------------\n",)
  
  numeracao = str(input("\nEscolha uma numeração:\t"))
  if (numeracao == '0'):
      exit(0) # fechar o programa

  # Pesquisa de produtos
  if (numeracao == '1'):
    os.system("cls")   #  limpar console
    pesquisaProduto()
    # ...
    
    
  if (numeracao == '2'):
      os.system("cls") # limpar console
      print("carregando..")
      sleep(1)
      tabela = str("")  #  variável
      while (tabela != "0"):
        os.system("cls")  #  limpar console
        for y in range(0, len(listaProdutos)):
          print(y+1,">>",listaProdutos[y]) # Tabela
          
        print("\nDigite 0 para voltar\n")
        print("\nEscreva 'excluirlista' para limpar lista\n")
        tabela = str(input("\nPesquise um elemento da tabela:\t"))
        tabela = tabela.lower()
        if (tabela == "0"):
          os.system("cls")  #  limpar console
          break
        if (tabela == "excluirlista"):
          print("\n'sim' para exclusão")
          tabela = str(input("\nCerteza que deseja apagar toda a lista?\t"))
          if(tabela == "sim"):
            for x in range(0, len(listaProdutos)):
              listaProdutos[x] = ""
              listaPrecos[x] = 0.0
              listaLinks[x] = ""
              listaTitulos[x] = ""
            print("\nLista Excluida por completo!")
            os.system("cls")
            break
          else:
            os.system("cls")
            print("Nada foi modificado")
            sleep(1)
            break
        try:      
          for y in range(0, len(listaProdutos)):
              print(y+1,">>",listaProdutos[y])
          for x in range(0, len(listaProdutos)):
            os.system("cls")  #  limpar console
            if (listaProdutos[x] == tabela):
              os.system("cls")
              print("\nProduto: ",listaTitulos[x])
              print("\nLoja: ",listaLojas[x])
              print("Menor Preço: ",listaPrecos[x])
              print("Link do site: ",listaLinks[x])
              print("\nDigite 0 para voltar")
              print("\nDigite 1 para alterar nome do produto")
              print("\nDigite 2 para excluir o produto")
              opcao_prod = int(input("\nEscolha uma das numerações:\t"))
              if (opcao_prod == 0):
                break
              if (opcao_prod == 1):
                tabela = str(input("\nNovo nome:\t"))
                listaProdutos[x] = tabela
                break
              if (opcao_prod == 2):
                listaProdutos[x] = ""
                listaTitulos[x] = ""
                listaPrecos[x] = 0.0
                listaLinks = ""
                print("\nProduto excluido com sucesso!")
        except:
          os.system("cls")
          print("Deveria ter sido informado um valor numerico nas opcoes do produto")
          sleep(3)
          break
           
  if (numeracao == '3'):
    os.system("cls")
    tam_list = 0
    try:
      for x in range(0, len(listaTitulos)):
        if (listaTitulos[x] != ''):
          tam_list = tam_list+1
      for y in range(tam_list-1, tam_list):
        print("|----------------------",
        "\n| >> Nome do produto: ", listaTitulos[y],
        "\n|----------------------\n",)
        print("|----------------------",
        "\n| >> Menor preço: ", listaPrecos[y],
        "\n|----------------------\n",)
        print("|----------------------",
        "\n| >> Menor preço: ", listaLojas[y],
        "\n|----------------------\n",)
        print("|----------------------",
        "\n| >> Site do produto: ", listaLinks[y],
        "\n|----------------------\n",)
      envioEmail()
      print("Email enviado com sucesso!")
      sleep(6)
    except:
      print("Nenhum resultado encontrado ou email invalido")
      sleep(2)
      # Erro comum: variáveis sem valor
  
  if (numeracao == '4'):
    os.system("cls") # limpar console
    for x in range(0, len(sites)):
      print("\nSites verificados:\n-",sites[x])
    sleep(3) # Tempo do resultado recente
  
  if (numeracao == '5'):
    opcao = ''
    os.system("cls") # limpar console
    while (opcao >= '1' or opcao <= '2'):
      print("Seu email:\t",email)
      print("\n0. >> Digite 0 para voltar")
      print("\n1. >> Troca do email")
      print("\n2. >> Reenvio do produto ao email")
      opcao = str(input("\nEscolha uma das opções:\t"))
      if (opcao == '0'):
        os.system("cls")
        break
      if (opcao == '1'):
        os.system("cls")  #  limpar console
        email = str(input("\nColoque seu email:\t"))
        os.system("cls")
      if (opcao == '2'):
        os.system("cls")  #  limpar console
        print("\nCaso não esteja recebendo verifique a aba de spam")
        print("\nAguarde..")
        try:
          envioEmail()
          sleep(4)
          print("\nEmail enviado com sucesso!")
          sleep(1)
          os.system("cls")
        except:
          print("\nEmail invalido")
          sleep(2)
        os.system("cls")
      else:
        os.system("cls")
        break
  if (numeracao == '6'):
    os.system("cls")
    print("\nOlá, seja bem vindo(a)")
    print("\nDuração do tutorial: 2 minutos")
    sleep(4)
    os.system("cls")
    print("\nVou ensinar um pouco sobre o uso do programa")
    sleep(4)
    os.system("cls")
    print("\nEm breve, será colocado um video mais explicativo")
    sleep(4)
    os.system("cls")
    print("\nBom.. vamos a primeira parte:")
    sleep(4)
    # loop da tabela
    for y in range(0, 10):
      print(y+1,">>",listaProdutos[y])  
    sleep(4)
    print("\nEstá é uma mini tabela, um exemplo da tabela da numeração '2'")
    sleep(4)
    print("\nNesta tabela são colocados valores de buscas")
    sleep(4)
    print("\nPor exemplo: titulo do produto, preço, link, etc..")
    sleep(4)
    print("\nE essa informações são guardadas em listas")
    sleep(4)
    print("\nMeio complexo né?")
    sleep(4)
    os.system("cls")
    print("\nA tabela apresentada tem seus dados")
    sleep(4)
    print("\nPrincipalmente das pesquisas dos produtos")
    sleep(4)
    print("\nEssa busca pode ser feita na numeração '1'")
    sleep(4)
    print("\nColocando assim o produto que tem interesse em poupar ;)")
    sleep(4)
    os.system("cls")
    print("\nA busca na numeração '1' retorna dos produtos, nome, preço, etc.")
    sleep(4)
    print("\nEm seguida eles são organizados em listas")
    sleep(4)
    print("\nE essas listas organizadas por loops na tabela")
    sleep(4)
    print("\nEspero que tenha ficado mais claro, companheiro(a)")
    sleep(4)
    os.system("cls")
    print("\nPara que seja enviado o email")
    sleep(4)
    print("\nSão necessárias 2 condições de uso do programa")
    sleep(4)
    print("\nUm email valido inserido por você usuário")
    sleep(4)
    print("\nE também pelo menos uma pesquisa feita com sucesso")
    sleep(4)
    print("\ncaso contrario as variaveis retornam vazias e dá erro")
    sleep(4)
    os.system("cls")
    print("\nOs sites que são feitos as buscas")
    sleep(4)
    print("\nSão de fonte confiável e pode ser verificado aqui:")
    sleep(4)
    print("\nhttps://www.reclameaqui.com.br/empresa/zoom-com-br/")
    sleep(4)
    print("\nTendo algumas pessoas que tiveram transtornos")
    sleep(4)
    print("\nAi então o site entrou em contato, solucionaram o problema")
    sleep(4)
    print("\nE grande parte escolheu voltar a fazer negócios no site")
    sleep(4)
    os.system("cls")
