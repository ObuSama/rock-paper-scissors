import random
from re import S
def play():
    user = input(" Lets play Rock-Paper-Scissors. Choose one --'r' for rock, 'p' for paper, 's' for scissors :")
    computer = random.choice(['r','p','s'])
    print(f"I have chosen {computer}")
    if user == computer:
        return 'It\'s a tie!'
    if is_win(user,computer):
        return 'You Won!'
    return 'You lost!'
def is_win(player,opponent):

    if (player=='p' and opponent =='s') or (player=='r' and opponent =='p') or (player=='s' and opponent =='r'):
        return False
    return True

if __name__ =="__main__":
    print(play())
    