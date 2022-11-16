# 2. (List of List) Write a program that allows 3 players to guess the total of 3 dice values. 
# The program first gets the player’s names, and randomly selects one player to guess first. 
# This is followed by the next player in order of the input of names. 
# The first person to guess the value wins. 
# The program then prompts whether the players wish to play again. 
# If the players do not wish to play, the the game ends. 
# Display the names of players with the most correct guesses.

# function get name

#function to randomly choose player and prompt to ask value
#show result
#if all wrong repeat until first person get it right
#prompt if user wants to play again if no game end
 
#show users with the most correct guesses 
#randit returns random int from rangeofnumbers in ()
#choice returns item in a list,tuple

from random import randint,choice

#dice no = how many num of dices to play
def diceValue(diceNo): 
    total = 0
    #loop through the range of dice no eg 3 [0,1,2]
    for i in range(diceNo):
        total += randint(1,6)
    return total



#only need to select 1 player to start first
def getPlayer(numOfPlayer):
    playerList = []
    playerOrder = []
    playerDetail = []
    for p in range(numOfPlayer):
        playerName = input('Enter player name: ')
        playerList.append(playerName)
    
    first_player = choice(playerList)
    print(f'Random choose {first_player} to start first')

    #remove first player from list
    playerList.remove(first_player)
    #append first player to the order list 
    playerOrder.append(first_player)
    # add the remaining players in player list to playerorder
    playerOrder = playerOrder + playerList
    # loop through player order and create into a list with score 0 and append to player details
    #player details with have the order of player info
    for player in playerOrder:
        playerDetail.append([player,0])
    # print(playerList)
    # print(first_player)
    # print(playerOrder)
    # print(playerDetail)
    #return a list of player details
    return(playerDetail)


#get player guess
def playerGuess(name):
    return int(input(f'{name}, guess the value: '))

def checkGuess(guess, diceValue):
    #if player guess equals to dicevalue
    success = guess == diceValue
    if success:
        print('Correct')
    else:
        print('Wrong!')
    # will return True if correct else False 
    return success

def playGuessingGame(diceVal,players):
    #if all guesses are wrong
    isWrong = True
    while isWrong:
        for player in players:
            #name of player of first in the list of playerDetail 
            guess = playerGuess(player[0])
            #then check the guess of player to the value of dice
            if checkGuess(guess, diceVal):
                #if correct increment player index point by 1
                player[1] += 1
                #as theres 1 winner end game, if not repeat game again
                isWrong = False
                break
    
    return players

def gameResult(player_score):
    maxScore = max(player_score, key=lambda x: x[1])[1]
    print("$$$$", max(player_score, key=lambda x: x[1]))
    print("******",maxScore)
    maxPlayer = [player_score[index][0] for index in range(len(player_score))  if player_score[index][1] == maxScore]
    print("Winners: ", " ".join(maxPlayer))   


def main():
    people_max = 3
    dice_max = 3
    playAgain = 'y'
    player_info = getPlayer(people_max)
    
    #after 1 player gets correct, if playAgain var is 'y' then loop
    while playAgain[0].lower() in 'y':
        
        faceValue = diceValue(dice_max)
        player_info = playGuessingGame(faceValue, player_info)
        playAgain = input("Continue? y/n: ")
    
    gameResult(player_info)

main()