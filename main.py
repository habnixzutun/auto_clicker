import time
import threading
import os


modules = [("click", "from click import clear", "pip3 install click"),
           ("keyboard", "import keyboard", "pip3 install keyboard"),
           ("pyautogui", "import pyautogui", "pip3 install pyautogui")]

for name, imp, ins in modules:
    try:
        exec(imp)
    except ModuleNotFoundError:
        print(f"[+] Installing {name} ({ins})")
        os.system(ins)
        try:
            exec(imp)
        except ModuleNotFoundError:
            print(f"[!] There was a problem installing and/or importing the {name} module. "
                  f"Please check your internet connection")
            print(f"[+] Press enter to close the program")
            input()
            os._exit(-1)
        print()

clear()

class Thread(threading.Thread):
    def __init__(self, mode, key):
        threading.Thread.__init__(self)
        self.mode = mode
        self.key = key

    def mode1(self):
        time.sleep(6.1)
        while not keyboard.is_pressed(self.key):
            pyautogui.leftClick()

    def mode2(self):
        time.sleep(.1)
        while True:
            if keyboard.is_pressed(self.key):
                pyautogui.leftClick()

    def run(self):
        if self.mode == 1:
            self.mode1()
        if self.mode == 2:
            self.mode2()


def while_not_pressed():
    key = input("Enter exit key:\t")[0]
    print(f"Your exit key is {key}")

    while True:
        try:
            thread_count = int(input("Enter thread count:\t"))
            print(f"Your key is {key}")
            break
        except ValueError:
            pass

    print()
    for i in range(thread_count):
        print(f"Thread Nr.{i + 1}/{thread_count} started")
        t1 = Thread(1, key)
        t1.start()
    time.sleep(1)
    print()

    for i in range(5, 0, -1):
        print(f"Autoclicker starts in {i}s...")
        time.sleep(1)
    print("Autoclicker starts")


def while_pressed():
    key = input("Enter key:\t")[0]
    print(f"Your key is {key}")

    while True:
        try:
            thread_count = int(input("Enter thread count:\t"))
            print(f"Your key is {key}")
            break
        except ValueError:
            pass

    print()
    for i in range(thread_count):
        print(f"Thread Nr.{i+1}/{thread_count} started")
        t1 = Thread(2, key)
        t1.start()
    print()

    print("Autoclicker starts...")


if __name__ == '__main__':
    while True:
        try:
            mode = int(input("while not pressed =\t1\n"
                             "while pressed =\t\t2\n"
                             "Option:\t"))
            if mode not in range(1, 3):
                print()
                continue
            print()
            break
        except ValueError:
            pass
    if mode == 1:
        while_not_pressed()
    if mode == 2:
        while_pressed()
