#Quiz game
import random

def cont(ques,ans):
    rand = random.randint(0,4)
    print("Question : ")
    print(ques[rand])
    ans1 = str(input("Please Enter Answer : "))
    if(ans1 == ans[rand]):
        print("Answer is Correct")
    else:
        print("Answer is not correct")
    

#Function for displaying the menu
def menu():
    print(" ______________________________")
    print("|          Quiz Game           |")
    print("|______________________________|")
    print("|  0. Exit                     |")
    print("|  1. Continue                 |")
    print("|______________________________|")

#Project function to call menu function and decide which function to call
def project(ques,ans):
    #Running infinite loop so that user can use options multiple times
    while(True):
        print()
        print()
        #Calling the menu function from which user can choose
        menu()
        #Taking the input of user choice
        ch = int(input("Please Enter Your Choice : "))
        #If the user chooses 0 then we will exit the program
        if(ch == 0):
            print("Thank you for using")
            break
        #If the user selects 1 then continuing 
        elif(ch == 1):
            cont(ques,ans)
        else:
            print("Wrong Input!")

ques = ["How many emairates are there in UAE?" ,"What is the capital of UAE?", "Largest city of UAE?", "National dish of emirates?", "dialing code of UAE"]
ans = ["7", "abu dhabi", "al ain", "kabsa", "+971"]
project(ques,ans)



