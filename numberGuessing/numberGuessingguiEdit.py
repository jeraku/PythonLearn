import random
import sys
# from numpy import diff

# MAX_TRIES= 10

def generateRandom(difficulty_level):
    if difficulty_level ==1: 
        number, max_tries = random.randint(1,50), 5
    elif difficulty_level ==2: 
        number,  max_tries = random.randint(1,100),7
    elif difficulty_level ==3: 
        number, max_tries = random.randint(1,1000),10
    else:
        print("default difficulty level")
    return number, max_tries

def welcome():
    print("Welcome to number guessing game")

def getUserInput():
    userInput = int(input("enter your guess number:"))
    return userInput

def checkEqual(userInput, randomNumer):
    status= False
    if userInput> randomNumer:
        print("input is higher")
    elif userInput < randomNumer:
        print("input is lower")
    elif userInput == randomNumer:
        print("you have won")
        status = True
    return status

def get_difficulty_level():
    print(""" 
Difficulty Levels: 
    1. Easy  1-50
    2. Medium 1-100
    3. Hard 1- 1000
""")
    difficultyLevel =  int(input("Enter your Difficulty Level: "))
    return difficultyLevel

def retry_fun():
    user_wish = input("Do you want to retry the game ? Yes/No: ")
    if user_wish == "yes":
        number_guessing_game()
    else:
        print("thanks for playing the game, we will connect later.")

def play(randomNumer, max_tries):
    status = False
    attempt=0
    while not status:
        if attempt > max_tries:
            print("you have lost the game")
            break
        attempt = attempt+1
        userInput = getUserInput()
        status= checkEqual(userInput, randomNumer)
        if status == True: 
            user_name = input("As you have won the game, enter your name")
            save_leaderboard(user_name, attempt)

def save_leaderboard(name, attempts):
    # print(f"save leader board name is {name} and attempt is {attempts}")
    with open("leader.txt", "a") as file:
        print(attempts)
        score = 1000 - ((attempts-1) * 100)
        print(f"save leader board name is {name} and attempt is {attempts} and score is {score}")
        file.write(f"{name} || {score} \n")
        print("leader board")
        
def list_leaderboard():
    with open(".//numberguessing//leader.txt", "r") as f:
    # with open("leader.txt", "r") as f:

        content = f.readlines()
        # score sorting - TASK
        print("\n--- Leaderboard ---")
        sorted_result=[]
        result={}
        for person in content:
            name, score = person.split("||")
            result[int(score)] = name
        result_sort = sorted(result.keys(),reverse = True)
        for i in (range(len(result_sort))):
            print(f"{i+1} winner Name is {result[result_sort[i]]} and the Score is {result_sort[i]}")
            sorted_result.append([result[result_sort[i]], result_sort[i]])
        print(sorted_result)
        
def number_guessing_game():
    welcome()
    # max_tries = 10
    difficulty_level = get_difficulty_level()  
    rand, max_tries = generateRandom(difficulty_level)
    print("2222222222222222   " + str(rand) )
    play(rand, max_tries)
    retry_fun()

if(__name__=="__main__"):
    if len(sys.argv)> 1 and sys.argv[1]=="list":
        list_leaderboard()
    else:
        number_guessing_game()

# TASK
# sort the rank in leader board
# fit the GUI code with my code
