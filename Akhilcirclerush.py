
import subprocess #importing subprocess module to control new processes
import serial     #we install pySerial and import serial to handle the serial communication
import pyautogui  #importing pyautogui module which allows us to control the keyboard and mouse
import time       #importing time module which provides time related functions


subprocess.call([r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                '-new-tab', 'https://www.chrome-games.com/play-color-switch-online']) #calling another subprocess which is a color splash game playable on our browser by passing its path 
print("Loading..")
time.sleep(5)    # python time sleep function actually stops the execution of current thread for 5 seconds
print("lets play the circle rush ")
print("colured bubble must only pass through the same colour else game over")
communication= serial.Serial('COM3', 9600, timeout=0.01) #opening our serial port by passing the port number baudrate and timeout 


while 1 : #infinite loop when game is running
        Incoming_data_from_Serial_Communication=communication.readline() #readline function is used to read serial data
        if Incoming_data_from_Serial_Communication : #checking that if the data is present is true i.e if data is seent using serial it willl execute next statement
         buttonIsPressed=int(Incoming_data_from_Serial_Communication.decode('utf-8')) # getting the bytes from the serail data unicode 
         if buttonIsPressed==1:  #checking whether the button is pressed and exucutes below statements if true
           pyautogui.press('space') #used to move to colour up 
           print("coloured bubble will go up each time when button on the board is pressed") 
