import random
player_rating = {}
file = 'rating.txt'
draw = 50
win = 100
rules = []
choice = ""
computer = ""

name = input('Enter your name:')
print('Hello,', name)
with open(file, 'r') as rating_file:
    for rating in rating_file:
        player_name, score = rating.split(sep=" ", maxsplit=1)
        player_rating[player_name] = int(score)
        if name in player_rating:
            player_score = int(score)
            break

rules = input()
if not rules:
    rules = 'rock,paper,scissors'
rules = rules.split(sep=',')
print("Okay, let's start")


def user_winner(user, comp):
    index_to = rules.index(user)
    index_from = index_to + 1
    elements_after = rules[index_from:]
    elements_before = rules[:index_to]
    elements = elements_after + elements_before

    half = len(elements) // 2
    beating_to_option = elements[:half]
    return comp not in beating_to_option


while True:
    computer = random.choice(['rock', 'paper', 'scissors'])
    choice = input()
    if choice == '!exit':
        print('Bye')
        break
    elif choice == '!rating':
        print("Your rating: " + str(player_rating[name]))
    elif choice not in rules:
        print('Invalid input')
        continue
    elif choice == computer:
        print(f'There is a draw {choice}')
        player_rating[name] += 50
    elif user_winner(choice, computer):
        print('Well done. Computer chose %s and failed' % computer)
        player_rating[name] += 100
    elif user_winner(choice, computer) is False:
        print('Sorry, but computer chose %s' % computer)
    else:
        print("Invalid input")
