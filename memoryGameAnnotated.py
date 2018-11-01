#Declaring variables
easyMode = False#Starts off with no mode being selected
hardMode = False#Starts off with no mode being selected

#Importing Modules
import random#importing this module to allow for shuffle
import time

#Defining Functions

#loading list from external file
def addWords():
    tenWordList = []
    tenWordsFile = open('Words.txt', 'r')
    for line in tenWordsFile:
        line = line.replace('\n', '')
        tenWordList.append(line);
    tenWordsFile.close;
    return tenWordList;

def addextendedwords():
    seventeenWordList = [];
    seventeenWordsFile = open('WordsExt.txt', 'r');
    for line in seventeenWordsFile:
        line = line.replace('\n', '');
        seventeenWordList.append(line);
    seventeenWordsFile.close;
    return seventeenWordList;

def createEasyGrid(tenWordList):
    for x in range (0, 9, 3):
        tableRow = ((tenWordList[x])+' | '+(tenWordList[x+1])+' | '+(tenWordList[x+2]))
        print (tableRow)

def createHardGrid():
    for i in range(0,16,4):
        hardTableRow = (seventeenWordList[i])+' | '+(seventeenWordList[i+1])+' | '+(seventeenWordList[i+2])+' | '+(seventeenWordList[i+3])
        print(hardTableRow)

def timeFirstGrid():
    time.sleep(30)

#Main Program
print ('Hi there, you are here as you believe that you have a talent at being observant')
modeChosen = input('Press - for easy mode\n\nPress + for hard mode')
if modeChosen == '-':
    easyMode = True
    print('You have 30 seconds to guess the missing word as well as the substitute word, good luck')
else:
    if modeChosen == '+':
        hardMode = True
        seventeenWordList = addextendedwords()
        random.shuffle(seventeenWordList)
        print('You have 45 seconds to look at the slightly larger grid and guess the missin and substitue word, good luck')
    else:
        print('That is not a valid mode wait a few seconds and the prgoram will close')
        time.sleep(3)
        exit()


tenWordList = addWords()            #Defining it just before it is called

if easyMode == True:                #Generates numbers for the first grid
    tenWordList = addWords()
    random.shuffle(tenWordList)

if easyMode == True:                #Creates the grid for easy mode
    createEasyGrid(tenWordList)
    print('you have 30 seconds to memorise these words')

    #Replacing first grid with second grid
    replacementWordOne = (tenWordList[9])
    random.shuffle(tenWordList)
    time.sleep(30)
    for w in range(60):
        print('')

    createEasyGrid(tenWordList)

    #Allow the user to guess the missing word
    guessedWordOne = input('Guess the missing word (please enter the answer in CAPITALS)')
    if guessedWordOne == (tenWordList[9]):
        print('You are correct!')
    else:
        guessedWordOne = input('WRONG!, you have 2 more chances to guess the missing word')
        if guessedWordOne == (tenWordList[9]):
            print('Well done! That is the missing word!')
        else:
            guessedWordOne = input('WRONG AGAIN!, this is your last chance...')
            if guessedWordOne == (tenWordList[9]):
                print('Finally!')
            else:
                print('You are a failure...')
                time.sleep(3)
                exit()

    #Allow the user to guess the substitute word
    guessedWordTwo = input('Guess the substitute word (please enter the answer in CAPITALS): ')
    if guessedWordTwo == replacementWordOne:
        print('You are correct!\nCongratulations, you have won!')
    else:
        guessedWordTwo = input('WRONG!, you have 2 more chances to guess the substitute word: ')
        if guessedWordTwo == replacementWordOne:
            print('Well done! That is the substitute word!\nCongratulations, you have won!')

        else:
            guessedWordTwo = input('WRONG AGAIN!, this is your last chance... : ')
            if guessedWordTwo == replacementWordOne:
                print('Finally!\nCongratulations, you have won!')
            else:
                print('So close yet so far...')
                time.sleep(3)
                exit()

#Creating the hard modes' first grid
if hardMode == True:
    createHardGrid()
  
#Replacing word from first hard grid
    replacementWordTwo = (seventeenWordList[16])
    random.shuffle(seventeenWordList)
    time.sleep(45)
    for w in range(60):
        print('')
        
    createHardGrid()
    #allowing the user to guess a removed word from the grid
    guessedWordThree = input ('What word has been removed?(answer in capitals)')
    if guessedWordThree == seventeenWordList[16]:
        print ('correct')
    else:
        guessedWordThree = input ('you have two more chances, try again')    #gives three guesses before forcibly closing program
        if guessedWordThree == seventeenWordList[16]:
            print ('correct')
        else:
            guessedWordThree = input ('your final chance, try again')
            if guessedWordThree == seventeenWordList[16]:
                print ('correct, at least you got it eventually')
            else:
                input('you have failed. i was right it seems, you did not have what it takes. press enter to close the program')
                exit()

    #allows user to guess a word added in the second grid
    guessedWordFour = input ('And what is the newly added word?(also in capitals)')
    if guessedWordFour == replacementWordTwo:
        print ('Ah! well done! well done indeed!')
        print('You have beaten the Hard mode! You are triumphant!\nYou will now leave for my next challenger')
        time.sleep(3)
        exit()
    else:
        guessedWordFour = input ('try again fool, that is incorrect')
        if guessedWordFour == replacementWordTwo:
            print ('at least you are not completely terrible')
        else:
            guessedWordFour = input ('that is incorrect, i will give you one more chance, since i enjoy your pain')  #gives another three chances before closing
            if guessedWordFour == replacementWordTwo:
                print ('you do not have my praise. a real player wins on their first try')
            else:
                print ('blood stains the ground beneath your corpse')
                input ('you have failed, as i expected. please show yourself out, with the enter key: ')
                exit()

                
