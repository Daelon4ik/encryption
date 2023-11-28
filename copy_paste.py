import encryption
import pyperclip
import keyboard
from time import sleep as sl

def copy_ep():
    
    sl(0.5)
    paste = pyperclip.paste()
    check = True


    if paste[0:3] == 'ep:':
        print('encryption')
        pyperclip.copy(encryption.encryption(paste[3:]))

    else:
        for i in paste:
            if check:
                for x in '∶∴∵∷':
                    if i == x:
                        check = True
                        break
                    else:
                        check = False
            else:
                break
        if check:
            print('unencryption')
            pyperclip.copy(encryption.unencryption(paste))



def main():
    while True:
        keyboard.add_hotkey('ctrl + c', lambda: copy_ep())

        keyboard.wait()



if __name__ == '__main__':
    print('Dont have password')
    sl(3)