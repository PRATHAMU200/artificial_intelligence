import pyautogui


def security():
    z=0
    while z==0:
        username=pyautogui.prompt('Enter Username')  # returns string or None
        password=pyautogui.password('Enter password')  # returns string or None
        if username == "root" and password == "root":
            z=1
        
        else:
            pyautogui.alert("Wrong password !!!!")
        
    pyautogui.alert('Succesfull Login', "Jarvis Login page")

    


# Method signatures:
#   alert(text='', title='', button='OK')
#   confirm(text='', title='', buttons=['OK', 'Cancel'])
#   prompt(text='', title='' , default='')
#   password(text='', title='', default='', mask='*')
