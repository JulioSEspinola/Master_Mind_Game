from random import randrange
from graphics import *
colors = ['pink','orange','yellow','red','green','blue']

def createBoard():
    win = GraphWin("Master Mind", 400, 600)
    win.setBackground('red3')
    win.setCoords(0, 0, 40, 64)

    for j in range(4):
        for i in range(8):
            circle = Circle(Point(5*j + 3, 5*i + 17), 2)
            circle.setFill('gray')
            circle.draw(win)

    line1 = Line(Point(0, 14), Point(40,14))
    line1.setWidth(2)
    line1.draw(win)

    line2 = Line(Point(25,13), Point(25,55))
    line2.setWidth(2)
    line2.draw(win)

    line3 = Line(Point(25,13),Point(25,0))
    line3.setWidth(2)
    line3.draw(win)

    line4 = Line(Point(0,55),Point(40,55))
    line4.setWidth(2)
    line4.draw(win)

    #Circles
    for j in range(4):
        for i in range(8):
            circ = Circle(Point(3*j + 28, 5*i + 17),1)
            circ.setFill('gray')
            circ.draw(win)

    #Diplay the color of the circles
    for j in range(3):
        for i in range(2):
            circ = Circle(Point(8*j + 5, 7*i + 3), 2.5)
            circ.setFill(colors[2*j+i])
            circ.draw(win)

    text = Text(Point(20,62),'MASTER MIND')
    text.draw(win)

    #Entry Box text
    text1 = Text(Point(32,11),' Enter four colors')
    text1.draw(win)

    #Input box
    inputText = Entry(Point(32,8),8)
    inputText.setFill('white')
    inputText.draw(win)

    return win, inputText
    
#Get a random sequence of the four choosed colors
def getSecret():
    secret = []
    for i in range(4):
        secret.append(colors[randrange(6)][0])        
    return secret

def copyCode(code):
    copy = []
    for i in range(len(code)):
        copy.append(code[i])

    return copy
       
#Get the guess from the user
def getGuess(window, entry):
    guess = []
    window.getMouse()
    inGuess = entry.getText()
    entry.setText('')
    for i in range (len(inGuess)):
        guess.append(inGuess[i])
    print(guess)
    return guess
#Check if the guess is similar to the reandom guess
def checkGuess(secret, guess):
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            secret[i] = 'BK'
            guess[i] = 'BK'
            
    for i in range(len(secret)):
        if secret[i] != 'BK':
            for j in range(len(guess)):
                if secret[i] == guess[j]:
                    secret[i]= 'WT'
                    guess[j] =  'WT'
                    
    return secret.count('BK'), secret.count('WT')
#Outputs the the similarities from the guess and the random guess
def outputResults(black,white, guess, turn, window):
    for i in range(len(guess)):
        for j in range(len(colors)):
            if guess[i] == colors[j][0]:
                circle = Circle(Point(5*i + 3,5*(turn-1) + 17), 2)
                circle.setFill(colors[j])
                circle.draw(window)
    bwList = []

    for i in range(black):
        bwList.append('black')

    for i in range(white):
        bwList.append('white')
    print(bwList)
    for i in range(len(bwList)):
        circ = Circle(Point(3*i + 28, 5*(turn-1) + 17),1)
        circ.setFill(bwList[i])
        circ.draw(window)

#end of the game 
def endGame(window,text, secret):
    text = Text(Point(20,60), text)
    text.draw(window)

    for i in range(len(secret)):
        for j in range(len(colors)):
            if secret[i] == colors[j][0]:
                circle = Circle(Point(2.5*i + 29, 5), 1)
                circle.setFill(colors[j])
                circle.draw(window)
            
#Run the program 
def main():
    secret = getSecret()
    black = 0
    turn = 1
    window, entry = createBoard()
    
    while(turn <= 8 and black != 4):
        guess = getGuess(window, entry)
        tempSecret = copyCode(secret)
        tempGuess = copyCode(guess)
        black, white = checkGuess(tempSecret, tempGuess)
        print(guess)
        outputResults(black, white, guess,turn, window)
        turn = turn + 1     
    if (black == 4):
        endGame(window, "You WIN!", secret)

    else:
        endGame(window,"You Lose!", secret)
        
main()
    
