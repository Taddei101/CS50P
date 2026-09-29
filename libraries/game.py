import random


def set_number():
    while True:
        try:
            number = int(input("Level: "))
            
            return random.randint(1,number)
        
        except ValueError:
            pass 

def guess_number(number):
    
   while True:
        try:
            guess = int(input("Guess: "))

            if guess < number:
                print("Too small!")
                    
            elif guess > number:
                print("Too large!")

            else:
                print("Just right!")
                break

        except ValueError:
            pass

    


guess_number(set_number())