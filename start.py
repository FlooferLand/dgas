from time import sleep
from importlib import import_module
from os import system as terminal

while True:
    main = import_module("main")
    if main.program() == 0:
        print("Waiting for a known program to be launched..")
        sleep(5)
