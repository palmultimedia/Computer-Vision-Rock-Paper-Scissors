# Create function "get_prediction" that will return the output of the model you used earlier.
import cv2
import random
from keras.models import load_model
import time
import numpy as np


#from another import RPS_game

class computervision:
    def __init__(self) -> None:
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        self.choice = ['rock', 'paper','scissors', 'nothing']
        self.user_points = 0
        self.computer_points = 0
        

    def classify_output(self, prediction):
        '''Get probability output prediction from the webcam image'''
        #Returns the indices of the maximum values along an axis.
        max_index = np.argmax(prediction)

        user_category = self.choice[max_index]

        return(user_category)

        

    def countdown(self):
    #delay 3 sec. start before game start

        print("begin timer")
        measure1 = time.time()
        measure2 = time.time()

        count = 1

        while count < 5:
            if measure2 - measure1 >= 2:
                a=4
                print(a)
                a=a-1
                measure1 = measure2
                measure2 = time.time()
                count += 1
            else:
                measure2 = time.time()

        print("Start")
        return(None)

    ''' 
        print("User input in webcam ")
        n = 3
        while n>0:
            print(n)
            time.sleep(1)
            n -=1
        print("Start")
        return(None)
    '''
    '''

        
        for sec in range(3,0,-1):
            time.sleep(1)
            print(sec)
    '''

    def get_output(self, prediction):

        # Open camera, return probability for (Rock, Paper, Scissor or Nothing)
        while True:
            self.countdown()         
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            choice = self.classify_output(prediction[0])
            if choice != "nothing":
                break
            print("Invalide input, provide rock, paper, scissor option")
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                    
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        print(choice)
        return(choice)


    def get_computer_choice(self):
        computer_choice = random.choice(self.choice)
        return computer_choice

    def get_user_choice(self):

        user_input = CaptureVideo() #self.get_output(self.choice)
        user_choice = user_input.get_output()
        return(user_choice)

    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            return("Draw")
        elif computer_choice == "rock":
            if user_choice=="scissors":
                self.computer_points += 1
                return("Computer Wins")
            self.user_points += 1
            return("User Wins")
        elif computer_choice == "paper":
            if user_choice == "rock":
                self.computer_points += 1
                return("Computer Wins")
            self.user_points += 1
            return("User Wins")
        elif computer_choice =="scissors":
            if user_choice == "paper":
                self.computer_points +=1 
                return("Computer Wins")
            self.user_points += 1
            return("User Wins")    





    def play(self, wins=3):
      
        while True:
                      
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_choice()
            winner = self.get_winner(computer_choice, user_choice)

            print(f"User Choice '{user_choice}', Computer Choice '{computer_choice}'")
            print(f"{winner} \nUser Score: {self.user_points} \nComputer Score: {self.computer_points}")

            if self.computer_points == wins or self.user_points == wins:
                break
            
            while True:
                next = input("Please enter to play next")
                if next == '':
                    break
            
        if self.user_points > self.computer_points:
            winner = "User"
        elif self.user_points < self.computer_points:
            winner = "Computer"
        else:
            print("Something not right")
        
        print(f"Game Over. {winner} wins!")
     
        return(None)

rps_game = computervision()
rps_game.play()
