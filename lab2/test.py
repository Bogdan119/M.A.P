#PYAUTOGUI
import pyautogui
import time
import keyboard
    

     #dinorunner.com
def dino():
    pyautogui.moveTo(750,530)
    time.sleep(5)
    pyautogui.click(750,530)
    while keyboard.is_pressed('space')!=True :
         if pyautogui.pixelMatchesColor(780, 540, (83, 83, 83), tolerance=10 )==True:  
             pyautogui.click(780,540)


response =pyautogui.confirm("Doriti sa in cepeti rularea programului?","Confirmare")
if (response=="OK"):
    dino()
else:
      pyautogui.alert("Ati ales anulare","Anulare")