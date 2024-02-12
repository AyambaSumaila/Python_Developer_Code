my_score=0
print("Guess the animal!")

my_guess=input("Which bear lives at the North Pole? >:")
    
    
def check_guess(guess, answer):
    
    
    global my_score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 4:
        
    
        if guess.lower() == answer.lower():
            print("Correct answer!")
            my_score += 3 - attempt
            
            still_guessing= False
        else:
            if attempt < 3:
                my_guess=input("Sorry wrong answer. Try again.")
            attempt +=1
    if attempt == 4:
        print("The correct answer is " + answer)
my_score=0 

    
    
    return my_score

check_guess(my_guess, "polar bear")

my_guess2=input("Which is the fastest land animal?>:")

check_guess(my_guess2, "Cheetah")
my_guess3=input("Which is the largest animal?>:")

check_guess(my_guess3, "blue whale")

my_guess4=input("Which one of these is a fish?\n a) whale \nb) Dolphin \nc) Shark \n d) Squid type A, B, C or D:")

check_guess(guess, "C")

guess=input("Mice are mammals. True or False?")
check_guess(guess, "True")




print("Your score is " + str(my_score))






"""
print("Do want to play again?(yes/no)")
response=input("Enter an option:>")

if response == "yes":    
    
    my_guess=input("Which bear lives at the North Pole? >:")
if response == "no":
         print("Thank for your time")
         
else:
    print("Incorrect option")
        
        
check_guess(my_guess, "polar bear")

         
"""

