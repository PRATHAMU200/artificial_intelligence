import pyautogui
import os

#save_path=pyautogui.prompt('Enter Path')
#name= pyautogui.prompt("enter name of file .png")

def screenshot():  
    screenshot = pyautogui.screenshot()
    save_path=pyautogui.prompt('Enter Path')
    name= pyautogui.prompt("enter name of file .png")
    nam=os.path.join(save_path,name+".png")
    screenshot.save(nam)
   
























