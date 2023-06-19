#generate 4 colour random code
#make user guess code
#compare guess to code
#tie game together

import random

COLOURS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for i in range(CODE_LENGTH):
        color = random.choice(COLOURS)
        code.append(color)
    return code

def guess_code():
    while True:
        guess = input("Guess:").upper().split(" ") #turns all input into list

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colours. ")
            continue #brings you to back of top of loop

        for colour in COLOURS: #checks all guesses are in color list
            if colour not in COLOURS:
                print(f"Invalid colour: {colour}. Try again")
                break
        else:
            break #breaks out of while loop

    return guess

def check_code(guess, real_code): 
    #looks through every single
    #detrmine how many colours are in correct position
    #deteremine how many colours are not in correct position

    colour_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for colour in real_code: 
        if colour not in colour_count:
            colour_count[colour] = 0
        colour_count[colour] += 1

    #arguments in correct position
    for guess_colour, real_colour in zip(guess, real_code): #arguments are combined into tuples
        if guess_colour == real_colour:
            correct_pos += 1
            colour_count[guess_colour] += 1 #geting rid of colour from colour_count


    #for incorrect colours
    for guess_colour, real_colour in zip(guess, real_code): #arguments are combined into tuples
        if guess_colour in  colour_count and colour_count[guess_colour] > 0:
            incorrect_pos += 1
            colour_count[guess_colour] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code ...")
    print("The valid colours are", *COLOURS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries! ")
            break
        print(f"Correct Position: {correct_pos} | Incorrect Position: {incorrect_pos}")
    
    else:
        print("You ran out of tries, the code was", *code)


if __name__ == "__main__": #makes sure that its directly running python file
    game()





