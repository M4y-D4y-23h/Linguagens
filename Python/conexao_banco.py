import pyodbc

# Esse programa faz a conexão com o banco de dados e pode ser realizado os commits utilizando a variável cursor.
# Adaptado por: Kevin Ricardo

def conecta_ao_banco(driver='(Seu driver de acesso)', server=r'(caminho do servidor SQL na sua máquina)', database='(banco de dados que será usado)', username=(usuario, se houver), password=(senha, se houver), trusted_connection = 'yes'):

  string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};USERNAME={username};PASSWORD={password};TRUSTED_CONNECTION={trusted_connection};"
  conexao = pyodbc.connect(string_conexao)
  cursor = conexao.cursor()
  return conexao, cursor

conexao, cursor = conecta_ao_banco()
length = cursor.execute('select * from vendas').fetchall() # Exemplo de comando
conexao.close() # Encerrando conexão com o banco
