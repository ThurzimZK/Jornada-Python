# Passo a Passo do projeto 
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 0.5
# pyautogui.click -> clicar em algm lugar da tela
# pyautogui.write -> escreve um texto
# pyautogui.press -> pressiona 1 tecla do teclado
# pyautogui.hotkey('ctrl', 'v') -> combinação de teclas

#abrir o navegador (chrome)
pyautogui.press('win')
time.sleep(1.5)
pyautogui.write('chrome')
time.sleep(1.5)
pyautogui.press('enter')

# fazer uma pausa maior em um lugar especifico
time.sleep(2.5)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(1.5)

# Passo 2: Fazer login
#pyautogui.click(x=770, y=368, clicks=2 ou button='left') quantos cliques e qual botão
pyautogui.click(x=770, y=368)
pyautogui.write('jornadapython@gmail.com')

#escrever a senha
pyautogui.press('tab')
pyautogui.write('senha123')
# pyautogui.press('enter') ou clicar no botão de logar
pyautogui.click(x=794, y=525)
time.sleep(1.5)

# Passo 3: Importar a base de dados
# pandas
import pandas as pd
tabela = pd.read_csv('produtos.csv')
print(tabela)

# Passo 4: Cadastrar 1 produto
#paracada linha da minha tabela
for linha in tabela.index:
    #clicar no primeiro campo
    pyautogui.click(x=724, y=256)

    #codigo do produto
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    #tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    #categoria
    #str() string -> texto
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    #preco
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    #obs
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    #enviar
    pyautogui.press('enter')
    pyautogui.scroll(5000)
# Passo 5: Repetir o processo de cadastro até acabar