import random
import tkinter
bombfield = []
gameOver = False
score = 0
squares_to_clear = 0

def play_bombdodger():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()


def create_bombfield(bombfield):
    global squares_to_clear

    for row in range(0,10):
        rowList = []
        for column in range(0,10):
            if random.randint(1,100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squares_to_clear = int(squares_to_clear) + 1
        bombfield.append(rowList)
    printfield(bombfield)

def printfield(bombfield):
    for rowlist in bombfield:
        print(rowlist)




def layout_window(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, ColumnEntry in enumerate(rowList):
            if random.randint(1, 100) < 25:
                square = tkinter.Label(window, text = "    ", bg ="darkgreen")
            elif random.randint(1, 100) > 75:
                square = tkinter.Label(window, text = "    ", bg ="seagreen")
            else:
                square = tkinter.Label(window, text = "    ", bg = "green")
            square.grid(row = rowNumber, column = columnNumber)
            square.bind("<Button-1>", on_click)

def on_click(event):
    global score
    global gameOver
    global squares_to_clear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")

    if gameOver == False:
        if bombfield[row][column] == 1:
            gameOver = True
            square.config(bg = "red")
            print("Game Over! Du gick på en mina")
            print("Din poäng::", score)
        elif currentText == "    ":
            square.config(bg = "brown")
            totalBombs = 0

            if row < 9:
                if bombfield[row+1][column] == 1: # <>
                    totalBombs = totalBombs + 1

            if row > 0:
                if bombfield[row-1][column] == 1:
                    totalBombs = totalBombs + 1

            if column < 0:
                if bombfield[row][column-1] == 1:
                    totalBombs = totalBombs + 1


            if column < 9:
                if bombfield[row][column+1] == 1:
                    totalBombs = totalBombs + 1



            if row > 0 and column > 0:
                if bombfield[row-1][column-1] == 1:
                    totalBombs = totalBombs + 1

            if row < 9 and column > 0:
                if bombfield[row+1][column-1] == 1:
                    totalBombs = totalBombs + 1

            if row > 0 and column < 9:
                if bombfield[row-1][column+1] == 1:
                    totalBombs = totalBombs + 1

            if row < 9 and column < 9:
                if bombfield[row+1][column+1] == 1:
                    totalBombs = totalBombs + 1

            square.config(text = " " + str(totalBombs) + " ")
            score = score + 1

            if squares_to_clear == 0:
                gameOver = True
                print("Snyggt! Du gick inte på en enda mina!")
                print("Din poäng:", score)



play_bombdodger()