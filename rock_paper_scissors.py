from itertools import count
import random

def play():
    user = input(" Choose one --'r' for rock, 'p' for paper, 's' for scissors :")
    computer = random.choice(['r','p','s'])
    print(f"I have chosen {computer}")
    return (user, computer)
def print_result(user,computer):    
    if user == computer:
        print('It\'s a tie!')
        return(0,0)
    elif is_win(user,computer):
        print( 'You Won!')
        return(1,0)
    else:
        print('You lost!')
        return(0,1)
def is_win(player,opponent):

    if (player=='p' and opponent =='s') or (player=='r' and opponent =='p') or (player=='s' and opponent =='r'):
        return False
    return True

if __name__ =="__main__":
    best_of = int(input("Lets play Rock-Paper-Scissors. Choose the number of games in set, best of :"))
    player_total = 0
    computer_total = 0
    games = 0
    while games< best_of:
        games+=1
        print(f"Game: {games}")
        user, computer = play()
        user_score,computer_score = print_result(user,computer)
        player_total += user_score
        computer_total += computer_score
    print(f"Score in the set -- You:{player_total}, Computer: {computer_total}")
    if player_total==computer_total:
        print("The set is tied")
    elif  player_total>computer_total:
        print("You won the set!")
    else:
        print("You lost the set!")
        