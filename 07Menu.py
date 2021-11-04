import sys
import os

def clear():
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

def options():
    print (' ------------------------------------------------ ')
    print ('|                                                |')
    print ('|    07Menu                                      |') 
    print ('|    Name : Celestine Sutanto                    |')
    print ('|    Version : 01                                |')
    print ('|                                                |')
    print (' ------------------------------------------------ ')
    print ('')
    print ('1. Hello World')
    print ('2. Goodbye World')
    print ('3. Goodbye Person')
    print ('4. Good Teacher')
    print ('5. forLoop')
    print ('6. whileLoop')
    print ('7. string Loop')
    print ('8. Convert to ascii')
    print ('9. Encode a string')
    print ('x. To Exit')

def helloworld():
    print ('')
    print ('----Start of Output ---------------------------')
    print ('')
    print ('Hello World')
    print ('')
    print ('----End of Output -----------------------------')

def goodbyeworld():
    print ('')
    print ('----Start of Output ---------------------------')
    print ('')
    print ('Hello World')
    x = input('------> Program paused - press enter to continue')
    print('Goodbye World')
    print ('')
    print ('----End of Output -----------------------------')

def goodbyeperson():
    print ('')
    print ('----Start of Output ---------------------------')
    print ('')
    print ('Hello World')
    x = input('What is your name ? ')
    print('Goodbye ' + x)
    print ('')
    print ('----End of Output -----------------------------')

def goodteacher():
    print ('')
    print ('----Start of Output ---------------------------')
    print ('')
    x = input('Teacher\'s name (try Mr Horan) ')
    if x == "Mr Horan":
        print ('You are lucky, he is a great teacher.')
    else:
        print (x + ' is an ok teacher')
    print ('')
    print ('----End of Output -----------------------------')

def forloop():
    print ('')
    print ('----Start of Output ---------------------------')
    print ('')
    for x in range(1, 500):
        print (x)
    print ('')
    print ('----End of Output -----------------------------')

def whileloop():
    print ('')
    print ('----Start of Output ---------------------------')
    print ('')
    subject = input ('What is the name of this subject ')
    while subject != 'IST':
        print ('Not Correct - try again')
        subject = input ('What is the name of this subject ')
        continue
    else:
        print ('')
        print ('')
        print (' Congratulations!!')
        print ('')
        print ('')
        print ('')
    print ('----End of Output -----------------------------')

while True:
    options()
    menu = input ('Enter an option ')
    valid = ["1", "2", "3", "4", "5", "6", "x"]

    if menu in valid:
        if menu == '1':
            helloworld()
            clear()
        elif menu == '2':
            goodbyeworld()
            clear()
        elif menu == '3':
            goodbyeperson()
            clear()
        elif menu == '4':
            goodteacher()
            clear()
        elif menu == '5':
            forloop()
            clear()
        elif menu == '6':
            whileloop()
            clear()
        elif menu == 'x':
            print ('')
            print ('----Start of Output ---------------------------')
            print ('')
            print ('')
            print ('----End of Output -----------------------------')
            print ('')
            print ('')
            print ('')
            input ('Press Enter to continue')
            print ('')
            sys.exit()
    else:
        print ('----Start of Output ---------------------------')
        print ('')
        print ('invalid option')
        print ('')
        print ('----End of Output -----------------------------')
        
    print ('')
    print ('')
    print ('')
    input ('Press Enter to continue')

