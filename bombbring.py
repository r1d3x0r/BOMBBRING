from time import sleep
import pyautogui
banner = """
\033[0;36m
██████╗  ██████╗ ███╗   ███╗██████╗ ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
██████╔╝██║   ██║██╔████╔██║██████╔╝██████╔╝██████╔╝██║██╔██╗ ██║██║  ███╗
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██╗██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝██████╔╝██║  ██║██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

Author		: r1d3x0r
Tool Name	: BOMBBRING
Version		: 1.0  
"""
print(banner)
numberofbombingtexts = int(input("Number Of Bombing Text: "))
bombingtext = input("Enter Your Bombing Text: ")
counter = 1
print ("=====25%")
sleep(1)
print ("==========50%")
sleep(1)
print ("===============75%")
sleep(1)
print ("======================92%")
sleep(1)
print ("===============================100%")
sleep(1)
while counter <= numberofbombingtexts:
 pyautogui.typewrite(bombingtext)
 pyautogui.typewrite("\n")
 sleep(2)
 counter = counter + 1
print("Attack Complete")
