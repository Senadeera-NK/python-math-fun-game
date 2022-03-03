from tkinter import *
import random
from unittest import result


#constances
GAME_WIDTH = 500
GAME_HEIGHT = 500
SPACE_WIDTH = 25
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

math_operation_label = Label(window,text="{} = {}".format(randomResultDigitsGenerator(),result),font=('consalas',20),bg=BACKGROUND_COLOR,fg = TEXT_COLOR)
math_operation_label.pack()

canvas = Canvas(window,bg = BACKGROUND_COLOR, width = GAME_WIDTH, height = GAME_HEIGHT)
canvas.pack()

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