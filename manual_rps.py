import random


'''
Play game without camera
Create two module get_computer_choice and get_user_choice
'''
class ManualGame():
    def __init__(self):
        self.choice = ["rock", "paper", "scissor"]
        self.computer_score = 0
        self.user_score = 0
        self.draw_score = 0

# Get computer choice by random selectoin
    def get_computer_choice(self):
        computer_choice = random.choice(self.choice)
        return computer_choice
# get user choice by asking input and check if entered string match with word.
    def get_user_choice(self):
        user_choice = input("Enter your choice 'Rock', 'Paper' or 'Scissor': ")
        user_choice = user_choice.lower()
        
        if user_choice in self.choice:
            return user_choice
        
        print("Enter word from 'rock', 'paper' or 'scissor': ")
        
        
    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            result = "Draw" 
        elif computer_choice == "rock" and user_choice =="Scissor":
            result = "Computer Win"
        elif computer_choice == "paper" and user_choice =="rock":
            result = "Computer Win"
        elif computer_choice == "scissor" and user_choice == "paper":
            result = "Computer Win"
        return(result)

    def play(self):
        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()
        winner = self.get_winner(computer_choice, user_choice)
        return(winner)

    def score(self, result):
        if result == "Computer Win":
            self.computer_score += 1
        elif result == "User Win":
            self.user_score += 1
        elif result == "Draw":
            self.draw_score += 1

        if self.user_score >3:
            print("You Win")
        elif self.computer_score >3:
            print("Computer Win")
        elif self.draw_score >3:
            print("Game Draw")


game = ManualGame()

print(game.play())