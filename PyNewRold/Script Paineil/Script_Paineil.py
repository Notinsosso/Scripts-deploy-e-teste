import os
import time
import pyautogui
import subprocess
import pygetwindow as gw
import winsound

# Configurações
Timeout = 5000  # tempo de timeout em ms
Address = "10.0.1.103"  # endereço para onde vai pingar
AA = "senha"  # login
BB = "123"  # senha
frequency = 3000  # Set Frequency To 2500 Hertz
duration = 5000  # Set Duration To 1000 ms == 1 second

# Funções de automação
def open_ASA():
    subprocess.Popen(["C:\\Sistemas\\SZNasa\\SZNasa13042023.exe"]) #Abre o SZN
    time.sleep(2.5)
    win = gw.getWindowsWithTitle('Entrando no Sistema')[0]
    win.activate()

def close_ASA():
    subprocess.Popen(["taskkill", "/f", "/im", "SZNAsa13042023.exe"])

def check_asa():
   win = gw.getWindowsWithTitle('Painel de Chamada - Szn Informática')
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
    
    if RTT == 0:  # Se o ping for bem sucedido
        if check_asa():
            continue
           
        open_ASA()
        

        pyautogui.write(AA)
        pyautogui.press("tab")
        time.sleep(0.9) 
        pyautogui.write(BB)
        time.sleep(0.9)
        pyautogui.press("enter")
        time.sleep(2.5)
        pyautogui.click(147, 66)
        time.sleep(2.5)
        pyautogui.click(1848, 579)
        time.sleep(2.5)
        winsound.Beep(frequency, duration)

    
    else:  # Se o ping falhar
        close_ASA()

    time.sleep(3)  # Aguarda 3 segundos antes da próxima iteração
