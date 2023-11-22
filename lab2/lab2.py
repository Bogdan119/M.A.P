#PYAUTOGUI
import pyautogui
import time
import keyboard

def cautare_google():
    if pyautogui.locateOnScreen(r"C:\Users\Bogdan\Desktop\map\lab2\poza5.png",confidence=0.7)!=None:
        camp_google =pyautogui.locateOnScreen(r"C:\Users\Bogdan\Desktop\map\lab2\poza5.png",confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(5)
        pyautogui.write("https://www.youtube.com/@kurzgesagt")
        pyautogui.press('enter')
        time.sleep(2)

response =pyautogui.confirm("Doriti sa incepeti rularea programului?","Confirmare")
if (response=="OK"):
      cautare_google()
else:
      pyautogui.alert("Ati ales anulare","Anulare")