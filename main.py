import encryption
from colorama import Fore, Back
from os import system
import getpass
from time import sleep as s
import copy_paste as cp
import password as ps


def open_file(file):

    with open(file, 'r', encoding='UTF-8') as files:
        or_text = files.read()
    return or_text


def save_file(text):

    with open('text.txt', 'w', encoding='UTF-8') as files:
        files.write(text)


def read_file(file):

    with open(file, 'r', encoding='UTF-8') as files:
        ret = encryption.unencryption(files.read())

    return ret


def unblock():
    system('cls')
    attempts = 0
    password = ''
    while password != ps.passw:
        password = getpass.getpass(f"{Fore.BLUE}Password -> ")
        attempts += 1
        system('cls')
        if attempts == 3:
            while True:
                print(f'{Back.RED}{Fore.BLACK}!!! Too many password attempts !!!\n'*15)
                s(99999999)


    system('cls')
    direct_file = input(f"{Fore.MAGENTA}-> {Fore.RESET}")
    unfiles = read_file(direct_file)
    save_file(unfiles)


def block(link):
    text = open_file(link)

    done_text = encryption.encryption(text)

    save_file(done_text)



def main():

    direct_file = input(f"{Fore.CYAN}-> {Fore.RESET}")

    if direct_file == 'unblock':
        unblock()

    elif direct_file == 'copy_paste':

        password = ''
        while password != ps.passw:
            password = getpass.getpass(f"{Fore.BLUE}Password -> ")

        system('cls')
        print(f'{Fore.LIGHTWHITE_EX}-=- Copy-Paste mode -=-')
        cp.main()

    else:
        block(direct_file)


if __name__ == "__main__":
    main()