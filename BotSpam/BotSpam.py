import AppKit #solo per mac os 
import time
import pyperclip
import pyautogui

#mettere tastiera americana 

screenWidth, screenHeight = pyautogui.size()
print((screenWidth, screenHeight))
#per mac
"""
time.sleep(5)
f = open("spam","r")
for word in f:
    print(word)
    pyautogui.typewrite(word)
""" 
time.sleep(5)
f = open("spam","r")

for char in f:
    print(char)
    pyperclip.copy(char)
    pyautogui.hotkey('command','v',interval = 0.2)
    pyautogui.typewrite("\n")
#"""
"""
ciao_
sono un bot
sto spammando 
non so cosa scrivere 
àèi'
proviamolo subito 
adios
"""


