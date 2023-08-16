import pyautogui # Importando o pyautogui
import time # Controlar o tempo que está acontecendo
import pandas as pd

pyautogui.PAUSE = 0.6 # tempo de espera de cada ação que o python executar

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# Entrar com link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Fazer o login utilizando email e senha sem precisar usar teclado ou mouse
pyautogui.click(x=703, y=483) # Posição do campo para inserir o email desejado
pyautogui.write("pythonpowerup@gmail.com")
pyautogui.press("tab") # passa para o próximo campo 
pyautogui.write("python2023") 
pyautogui.click(x=971, y=680) # Posição para clicar no botão de 'logar'
time.sleep(2)

# Ver os produtos que estão na tabela do arquivo
tabela = pd.read_csv("produtos.csv")
print(tabela)

# cadastrar o produto no site
for linha in tabela.index:
    print(linha)
    pyautogui.click(x=748, y=337)

    # pegar da tabela o valor do campo que a gente quer preencher 
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo 
    pyautogui.write(str(codigo))

    pyautogui.press("tab") 
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab") 
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab") 
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab") 
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab") 
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab") 
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    # dar scroll até o começo da página
    pyautogui.scroll(5000)







