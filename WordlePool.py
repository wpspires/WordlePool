import tkinter as tk
from attr import validate
from click import get_current_context
from pyparsing import White

lines = []

def main():
    with open("C:\\Users\\Guy\\Desktop\\WordleAnswers.txt") as f:
        global lines

        lines = f.readlines()

        window = tk.Tk()
        window.title("WordlePool")
        window.geometry("400x200")
    
        input1 = CustomEntry(window)
        input2 = CustomEntry(window)
        input3 = CustomEntry(window)
        input4 = CustomEntry(window)
        input5 = CustomEntry(window)

        input1.grid(column=0, row=0)
        input1.focus_set()
        input2.grid(column=1, row=0)
        input3.grid(column=2, row=0)
        input4.grid(column=3, row=0)
        input5.grid(column=4, row=0)

        window.mainloop()

        #for line in lines:
            #print(line)

def change_color_of_input(event):
    return False    

def does_not_contain(line, chars) -> bool:
    for c in chars:
        if c in line:
            return False
    return True

def contains(line, chars) -> bool:
    for c in chars:
        if c not in line:
            return False
    return True

def green(index, letter) -> list[str]:
    global lines
    lines =  [x for x in lines if x[index-1] == letter]

def yellow(index, letter) -> list[str]:
    global lines
    lines =  [x for x in lines if x[index-1] != letter and contains(x, letter)]

def black(chars) -> list[str]:
    global lines
    lines =  [x for x in lines if does_not_contain(x, chars)]

def move_focus(self, val, d):
    if len(val) == self.width and d != 0:
        self.entry.tk_focusNext().focus()
        return False
    return True

class CustomEntry(tk.Frame):

    def __init__(self, parent, txt=None): 
        tk.Frame.__init__(self, parent)
        self.width = 1

        vcmd = (self.register(self.move_focus), '%P', '%d')
        self.entry = tk.Entry(self, 
            width = 1,
            font= ('Verdana', 20),
            bg = 'white',
            justify ='center',
            validate = 'key',
            vcmd = vcmd)
        self.entry.pack()

    def move_focus(self, val, d):
        if len(val) == self.width and d != 0:
            self.entry.insert(0, val)
            self.entry.tk_focusNext().focus()
            return False
        return True

main()