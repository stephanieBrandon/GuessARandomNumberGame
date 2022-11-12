import random

def create_random_num():
    min_num = (int(input("Please enter your minimum number...")))
    max_num = (int(input("Please enter your maximum number...")))

    randomNum = random.randint(min_num,max_num)
    return randomNum

def win_stats():
    global winScore
    global games_played
    global games_lost
    print(f"You have won {winScore} games and played a total of {games_played} games with your win percentage  currently being %{winScore/games_played:.2f}")
    resetScore = input("Would you like to reset the record of your games won/lost?")
    if resetScore == 'y':
        winScore = 0
        games_lost = 0
        games_played = 0

#Creating while loop
winScore = 0
games_played = 0
games_lost =0

while(True):
    random_num =create_random_num()
    number_guess = int(input("Please guess the number in your specified range: "))
    if random_num == number_guess:
        print("You guessed correct!!!!")
        winScore+=1
    else:
        print("Sorry, your guess is wrong.")
        games_lost +=1
    games_played+=1
    win_stats()
    play_again = input("Would you like to play again?")
    if play_again == "n":
        print("Thanks for playing")
        break


    