import pywhatkit
import pyautogui
import time

import flask
from tkinter import *

root = Tk()



def myclick():

     number = inp1.get()
     text=inp2.get()
     time_hr=inp3.get()
     time_min=inp4.get()
     n=inp5.get()
     label2 = Label(root, text='message wil be sent at ' + time_hr + ':' + time_min+'n number of times')
     label2.grid(row=8, column=5)

     pywhatkit.sendwhatmsg('+' + str(number),text,int(time_hr),int(time_min))

     for i in range(int(n)-1):
          time.sleep(2)
          pyautogui.typewrite(text)
          pyautogui.press('enter')



label = Label(root, text='MESSAGE BASHER',font=('Bold',25),bg='Green',borderwidth=10)
mybutton = Button(root, text='Submit', command=myclick, fg='blue',borderwidth=15,font=('Aerial'))
label.grid(row=0, column=5)
# for entering number
num = Label(root, text='ENTER THE PHONE NUMBER')
num.grid(row=2, column=4)
# input for number
inp1 = Entry(root, width=50, fg='white', bg='black', borderwidth=10)
inp1.grid(row=2, column=5)

# for entering message
msg = Label(root, text='ENTER THE MESSAGE')
msg.grid(row=3, column=4)
# INPUT FOR MESSAGE
inp2 = Entry(root, width=50, fg='white', bg='blue', borderwidth=10)
inp2.grid(row=3, column=5)

th = Label(root, text='ENTER Time(HOURS)')
th.grid(row=4, column=4)

inp3 = Entry(root, width=50, fg='white', bg='green', borderwidth=10)
inp3.grid(row=4, column=5)

tm = Label(root, text='ENTER Time(MINS)')
tm.grid(row=5, column=4)

inp4 = Entry(root, width=50, fg='white', bg='red', borderwidth=10)
inp4.grid(row=5, column=5)

repeat = Label(root, text='ENTER the number of times')
repeat.grid(row=6, column=4)
inp5 = Entry(root, width=50, fg='black', bg='yellow', borderwidth=10)
inp5.grid(row=6, column=5)


mybutton.grid(row=7, column=5)

root.mainloop()
