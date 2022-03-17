from operator import index
from tkinter import *
import random

#()=rows
tableDigitsList = [(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"",""),(1,"",23,33,"",31,"","","",11,34,"",12,67,78,"",90,98,"","")]

#constances
GAME_WIDTH = 500
GAME_HEIGHT = 500
SPACE_WIDTH = 50
BACKGROUND_COLOR = 'black'
LINE_COLOR = TEXT_COLOR = 'white'
CURRENT_GUESSBOX_LINE_COLOR = 'blue'
USER_GUESSES_COLOR = 'yellow'

#functions
def mathOperation(result):
  mathPieces = []
  operations = ['+','=']

  for number in mathPieces:
    return number + operations[0]

def randomResultDigitsGenerator():
  pass

def roundsOver():
  pass

#window starts........
window = Tk()
window.title('Math Fun Game')
window.resizable(False, False)

score = 0
result = random.randint(0,1000)
no_columns = int(GAME_WIDTH/SPACE_WIDTH)
no_rows = int(GAME_HEIGHT/SPACE_WIDTH)

math_operation_label = Label(window,text="{} = {}".format(randomResultDigitsGenerator(),result),font=('consalas',20),bg=BACKGROUND_COLOR,fg = TEXT_COLOR)
math_operation_label.pack()


frame = Frame(window,bg = BACKGROUND_COLOR, width = GAME_WIDTH, height = GAME_HEIGHT)
frame.pack()

#create the list for showing tableDigits
for i in range(no_rows): #Rows
    for j in range(no_columns): #Columns
        label = Label(frame, text="123",borderwidth=2,relief="groove",bg=BACKGROUND_COLOR,fg="white",width=int(SPACE_WIDTH/10),height=int(SPACE_WIDTH/20))
        # label.place(relx=.5, rely=.5)
        label.grid(row=i,column=j, sticky=NSEW)
        


score_label = Label(window, text='score:{}'.format(score),font=('consalas',40))
score_label.pack()

#adjusting the window to center of the screen
window.update()
window_height = window.winfo_height()
window_width = window.winfo_width()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window.mainloop()