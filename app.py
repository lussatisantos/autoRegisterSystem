import pyautogui
from time import sleep

# clicar e digitar meu usuario
pyautogui.click(1295,542, duration=2)
pyautogui.write('lussatisantos')

# clicar e digitar minha senha
pyautogui.click(1296,568, duration=2)
pyautogui.write('#netconnect123')

# clicar en entrar
pyautogui.click(1190,595, duration=2)

# extrair cada produto
with open('Produt.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

    # clicar e digitar produto
        pyautogui.click(1047,530, duration=2)
        pyautogui.write(produto)

    # clicar e digitar a quantidade
        pyautogui.click(1034,554, duration=2)
        pyautogui.write(quantidade)

    # clicar e digitar o preco
        pyautogui.click(1034,580, duration=2)
        pyautogui.write(preco)
    # clicar en registrar
        pyautogui.click(907,734, duration=1)
        sleep(1)