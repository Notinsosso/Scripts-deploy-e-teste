import os
import time
import pyautogui
import subprocess
import pygetwindow as gw

# Configurações
Timeout = 5000  # tempo de timeout em ms
Address = "10.0.0.3"  # endereço para onde vai pingar
AA = "senha"  # login
BB = "123"  # senha


# Funções de automação
def open_SZN():
    subprocess.Popen(["C:\\Sistemas\\SZNasa\\SZNasa13042023.exe"]) #Abre o SZN
    time.sleep(2.5)
    win = gw.getWindowsWithTitle('Entrando no Sistema')[0] # Pega o nome da janela de login
    win.activate() # Força a janela de login do SZN ir pra frente

def close_SZN():
    subprocess.Popen(["taskkill", "/f", "/im", "SZNAsa13042023.exe"]) # Apenas mata o processo

#Função para checar se existe um painel já aberto e se existir, ele puxa pra frente 
def check_SZN():
   win = gw.getWindowsWithTitle('Painel de Chamada - Szn Informática') # Pega o nome da janela do painel e joga na variável
   if win:
        win[0].activate()
        return True 
   else:
        return False

# Loop principal
while True:
    # Realiza o ping para o endereço especificado
    RTT = subprocess.run(["ping", "-n", "1", "-w", str(Timeout), Address], capture_output=True)
    RTT = RTT.returncode
    
    if RTT == 0:  # Se o ping for bem sucedido, ele vai dar 0 como resposta, então ele continua o código se a condição for atendida
        if check_SZN(): # Aqui ele checa se existe um painel já aberto
            continue # Se teve resposta do servidor e o SZN está aberto no painel, então ele continuará a iteração ignorando o resto do código (Não abrirá o SZN novamente e continuará verificando se esta pingando)
        #Caso o ping retornou e não tem nenhum SZN aberto, ele irá abrir com o código abaixo
           
        open_SZN()
        

        pyautogui.write(AA) # Cola o usuário definido na variável AA
        pyautogui.press("tab") # Vai para o campo abaixo
        time.sleep(0.9) 
        pyautogui.write(BB) # Cola a senha definida na váriavel BB
        time.sleep(0.9)
        pyautogui.press("enter") # Usa o botão Enter para logar
        time.sleep(2.5)
        pyautogui.click(147, 66) # Clica no primeiro ícone
        time.sleep(2.5)
        pyautogui.click(1848, 579) # Clica na opção painel
        time.sleep(2.5)

    
    else:  # Se a resposta do RTT for diferente de 0, então o endereço não respondeu o ping, ele irá fechar o ASA
        close_SZN()

    time.sleep(3)  # Aguarda 3 segundos antes da próxima iteração
