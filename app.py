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
    # clicar e digitar produto
    # clicar e digitar a quantidade
    # clicar e digitar o preco
    # clicar en registrar