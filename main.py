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
  noOfNumbers =int(500/50)
  numbers = []
  noOfshowingNumbers = random.randint(1,(noOfNumbers - 1))
  showingNumbers = []
  notShowingNumbers = []
  operations = ['+','=']
   
  for i in range(noOfNumbers):
    number = random.randint(0,result)
    numbers.append(number)
    result -= number
  
  #numbers that are showing adding to 'showingNumbers' list
  j = 0
  while(j < noOfshowingNumbers):
    #randomly picking an index number between 0 and 9
    x = random.randint(0,(noOfNumbers-1))
    #getting the value of that random index from numbers list
    randomNumber = numbers[x]
    #adding that value to showingNumbers list if it isn't already exists
    if (randomNumber not in showingNumbers):
      showingNumbers.append(randomNumber)
      j += 1
  
  #numbers that aren't showing adding to notShowing numbers list
  noOfNotShowingNumbers = noOfNumbers - noOfshowingNumbers
  for i in range(noOfNotShowingNumbers+1):
    #getting numbers from noumbers list
    randomNumber2 = numbers[i]
    #if that number not already exists in showingNumbers list adding it to notShowingNumbers list
    if (randomNumber2 not in showingNumbers):
      notShowingNumbers.append(randomNumber2)
    elif (randomNumber2 == 0):
      notShowingNumbers.append(0)
  
  print('no of not showing numbers: ', noOfNumbers - noOfshowingNumbers)
  print('not showing numbers: ',notShowingNumbers)
  print("no of showing number: ",noOfshowingNumbers)
  print(showingNumbers)
  return numbers


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

math_operation_label = Label(window,text="{} = {}".format(mathOperation(result),result),font=('consalas',20),bg=BACKGROUND_COLOR,fg = TEXT_COLOR)
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