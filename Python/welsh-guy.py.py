import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import re
import time
import os

def split(number):
    #turns 1010 into ['1','0','1','0']
    return [char for char in number]


def unsplit(numList):
    #turns ['1','0','1','0'] into 1010
    return("".join(numList))


def unspace(binary):
    listy = split(binary)
    count = 0
    for i in listy:
        if listy[count] == " ":
            del listy[count]
        count += 1
    unspaced = unsplit(listy)
    return unspaced
        


def binarise(number):
    integer = int(number)
    ansList = []
    count = 0
    find = integer + 1
    while find > 1:
        find = find/2
        count += 1
        #count is the no of bits in register
    power = 2**(count-1)
    #power is the highest power used
    count2 = 0
    for i in range(0,count):
        if integer > power-1:
            ansList.append('1')
            integer = integer - power
        else:
            ansList.append('0')
        power = power/2
        
    #addds 0s at the front to make it a multiple of 4 so it looks neat

    if len(ansList)%4 == 0:
        x = 0
    else:
        x = 4-((len(ansList))%4)
    for j in range (0,x):
        ansList.insert(0,'0')
    


    #adds spaces every 4 bits to make it easier to read off
    bit = 0
    spaces = 0
    for position in ansList:
        if bit%4 == 0:
            if bit != 0:
                ansList.insert((bit+spaces),' ')
                spaces += 1
        bit +=1
        
    ans = unsplit(ansList)    
    return ans


def denarise(binary):
    myNum = unspace(binary)
    ans = 0
    n = len(myNum)-1
    
    start = 2**n
    #the start power
        
    numList = split(myNum)
    count = 0
    for i in numList:
        if numList[count] == '1':
            ans = ans + start
        start = start/2
        #start/2 is next power to the right
        count +=1
    return int(ans)

def hexabinarise(num):
    ans = 0
    numList = split(num)
    counter = 0
    binList = []
    for i in numList:
        if numList[counter] == 'A':
            binList.append(binarise(10))
        elif numList[counter] == 'B':
            binList.append(binarise(11))
        elif numList[counter] == 'C':
            binList.append(binarise(12))
        elif numList[counter] == 'D':
            binList.append(binarise(13))
        elif numList[counter] == 'E':
            binList.append(binarise(14))
        elif numList[counter] == 'F':
            binList.append(binarise(15))
        elif (numList[counter]).isalpha() == False:
            binList.append(binarise(numList[counter]))
        binList.append(" ")
        counter += 1
    ans = unsplit(binList)
    return ans

def binhexify(myNum):
    numList = split(myNum)
    if len(myNum)%4 == 0:
        upper = int(len(myNum)/4)
    else:
         x = 4-((len(myNum))%4)
         for j in range (0,x):                                                                                              
            numList.insert(0,'0')
         upper = int(len(numList)/4)
    anslist = []
    temp = []
    pos = 0
    for i in range (0,upper):
        temp = []
        temp.append(numList[pos])
        temp.append(numList[pos + 1])
        temp.append(numList[pos + 2])
        temp.append(numList[pos + 3])
        tempNum = unsplit(temp)
        den = denarise(tempNum)
        if den < 10:
            anslist.append(str(int(den)))
        elif den == 10:
            anslist.append('A')
        elif den == 11:
            anslist.append('B')
        elif den == 12:
            anslist.append('C')
        elif den == 13:
            anslist.append('D')
        elif den == 14:
            anslist.append('E')
        elif den == 15:
            anslist.append('F')
        pos +=4
    ans = unsplit(anslist)
    return ans



class sumScreen(tk.Tk):
    def __init__(self, title, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.customFont = tkFont.Font(family = "Gothic", size = 16)

        self.title(title)
        self.background1 = tk.PhotoImage(file = "flyBoi.gif")
        self.background_label = tk.Label(self, image = self.background1)
        self.background_label.place(x = 0, y=0, relwidth = 1, relheight = 1)

        self.geometry('{}x{}'.format(600, 500))
        self.rowconfigure(0, {'minsize':40})
        self.rowconfigure(1, {'minsize':40})
        self.rowconfigure(2, {'minsize':40})
        self.rowconfigure(3, {'minsize':40})
        self.rowconfigure(4, {'minsize':40})
        self.columnconfigure(0, {'minsize':200})
        self.columnconfigure(1, {'minsize':200})
        self.columnconfigure(2, {'minsize':200})

        self.message = "input"
        self.Label1 = tk.Label(self, text = self.message, font = self.customFont)
        self.Label1.grid(row = 1, column = 0, columnspan = 1, sticky = 'NSEW') 
        self.entry1 = tk.Entry(self, font = self.customFont)
        self.entry1.grid(row=1, column=1, columnspan=1, sticky='NSEW')
    
        

        self.message = "operation"
        self.menuLabel = tk.Label(self, text = self.message, font = self.customFont)
        self.menuLabel.grid(row = 3, column = 0, columnspan = 1, sticky = 'NSEW')

        

        
        self.variable = tk.StringVar()
        self.variable.set("(please select)")
        self.menuInput = tk.OptionMenu(self,self.variable,"binary to denary","denary to binary","binary to hexadecimal", "hexadecimal to binary", "denary to hexadecimal", "hexadecimal to denary")
        self.menuInput.grid(row = 3, column = 1, columnspan = 1, sticky = 'NSEW')
        
        self.calculateButton = tk.Button(self, text="calculate", font=self.customFont,fg="#EEE8AA", bg = "black", \
                                     command=lambda: self.calculate(self.entry1.get(), self.variable.get()))
        self.calculateButton.grid(row=5, column=1, columnspan=1, sticky='NSEW')

        
    def animate(self):
        frames = [PhotoImage(file = 'flyBoi.gif', format = 'gif -index % i' %(i)) for i in range(45)]
        def update(ind):

            frame = frames [ind]
            ind += 1
            if ind > 44:
                ind = 0
            label.configure(image = frame)
            self.after(100, update, ind)
        label = Label(self)
        label.pack()
        self.after(0, update, 0)
        self.mainloop()
        
    def calculate(self, value, operation):
        if operation == "binary to denary":
            if bool(re.search(r"^[w\ ].[0-1]$")) == True:
                self.answer(denarise(value))
            else:
                tk.messagebox.showerror("value error")
        if operation == "denary to binary":
            self.answer(binarise(value))
        if operation == "binary to hexadecimal":
            self.answer(binhexify(value))
        if operation == "hexadecimal to binary":
            self.answer(hexabinarise(value))
        if operation == "hexadecimal to denary":
            bina = unspace(unspace(hexabinarise(value)))
            self.answer(denarise(bina))
        if operation == "denary to hexadecimal":
            bina = unspace(unspace(binarise(value)))
            print (bina)
            self.answer(binhexify(bina))
        
        return
                   
    def answer(self,ans):
        h = 1
        
        if len(str(ans)) > 75:
            w = 75
            h = int(len(str(ans))/75)
        else:
            w = len(str(ans))
        self.T = tk.Text(self, height = h, width = w)
        self.S = tk.Scrollbar(self)
        self.T.grid(row=7, column=1, columnspan=1, sticky='NSEW')
        
        self.T.insert(tk.END, ans)
        
        
        return

def main():
    MainProg = sumScreen("Home")
    MainProg.mainloop()

if __name__ == '__main__':
    main()

