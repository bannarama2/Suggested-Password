#import libraries
import random as r

"""
Random password generator (like that used by google when it suggests passwords that would be strong). It will need random
to give a random feel to the generation of the password. Because it would be least expected. It will have 4 lists. Then a random
number will be given and depending on the number that we get from 0-3 it will tell us which list to use. Then we need another
random number that will tell us which index to use from the list that we previously generated. It will need a for loop to keep
running for around 8 characters minimum in length. Could also be done using a while loop. While current iteration is less than 
or equal to the decided character length. Do generation. Else exit.
"""

#declare lists and variables
Numbers = [0,1,2,3,4,5,6,7,8,9]
Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capitalLetters = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Symbols = ["!","@","#","$","%","^","&","*","_","-","=","+","<",">","?","/",".","`","~",";",":"]

passwordLength = input("How long do you want your password to be? ")

currIteration = 0
maxIteration = int(passwordLength) - 1

finalPassword = ""

#iterates through the while loop and adds one to the iteration counter every time
while currIteration <= maxIteration:
    #chooses a random integer from the range 0-3
    listChoice = r.randint(0,3)

    #checks if the integer chosen is 0 if it is 0, then it will get a random value from the list of numbers
    if listChoice == 0:
        numChoice = r.choice(Numbers)
        print(numChoice)
        finalPassword += str(numChoice)

    #checks if the integer chosen is 1 if it is 1, then it will get a random value from the list of small case letters
    elif listChoice == 1:
        letterChoice = r.choice(Letters)
        print(letterChoice)
        finalPassword += letterChoice

    #checks if the integer chosen is 2 if it is 2, then it will get a random value from the list of capital letters
    elif listChoice == 2:
        capLetterChoice = r.choice(capitalLetters)
        print(capLetterChoice)
        finalPassword += capLetterChoice

    #checks if the integer chosen is 3 if it is 3, then it will get a random value from the list of symbol characters
    elif listChoice == 3:
        symbolChoice = r.choice(Symbols)
        print(symbolChoice)
        finalPassword += symbolChoice

    currIteration += 1

print()
print(f"Your password is {finalPassword}")