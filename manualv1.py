from random import choice

'''
Play game without camera
Create two module get_computer_choice and get_user_choice
'''


def get_computer_choice(choice_list: list) ->str:
    
    game_choice = choice(choice_list)
    print(f"Computer Choice: {game_choice}")

    return game_choice

def get_user_choice(choice_list: list) ->str:
    game_choice = ''
    while game_choice not in choice_list:
        game_choice = input("Choose your word: ").lower()
        game_choice = game_choice.lower()
            
    if game_choice == 'Nothing':print("Please enter word:\n")

    return game_choice

def get_winner(user_word: str, computer_word: str) -> int:

    if computer_word in lost_list[user_word]:
        print("You win")
        point=1
    elif user_word in lost_list[computer_word]:
        print("Computer Win")
        point = -1
    else:
        print("Draw")
        point = 0
    print("")
    return point

def play(choice_list: list, lost_list: dict):
    print("\n Play Game \n")

    user_point = 0
    computer_point = 0
    game_play = True

    while game_play:
        user_word = get_user_choice(choice_list=choice_list + ['Nothing'])

        if user_word != "Nothing":
            computer_word = get_computer_choice(choice_list=choice_list)
            point = get_winner(user_word=user_word, computer_word=computer_word)

            if point == 1:
                user_point += 1
            elif point == -1:
                computer_point += 1

            game_play = (user_point<3 and computer_point < 3)
        
    if user_point == 3:
        print("You win Game")
    elif computer_point == 3:
        print("Computer win")
    print("")

choice_list = ["rock", "paper", "scissor"]
lost_list = {
    'rock':'scissors',
    'paper':'rock',
    'scissor':'paper',
    }

play(choice_list=choice_list, lost_list=lost_list)




