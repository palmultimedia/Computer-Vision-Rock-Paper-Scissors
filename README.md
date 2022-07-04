# Computer-Vision
Computer vision - rock paper scissors 

![Image](https://wp-assets.futurism.com/2014/05/rock-paper-scissors.jpg)

## Introduction:
With live camera matchin look at the hand of a persoin and predict the class (Rock, Paper, Scissor or Nothind) in realtime.

## System Requirments
1) Camera
2) Python
3) Teachable Machine
4) TensorFlow


## Milestone 1:

Build image project model on Teachable_matchine with four classes [Rock, Paper, Scissor and Nothing], train atleast 200 frames minimum.

Download completed model files (keras_model.h5 and labels.txt) into the project and synchronize with github


## Milestone 2:

Setup virtual environment (conda) and activate it.
Install pip and required library (opencv-python, tensorflow and ipykernel)

## Milestole 3:
Manual game - Rock, Paper, Scissor. 
file - name : manual_rps.py

Store user random computer choice and ask user input and store in variable. Check user input match with the list words [rock, paper, scissor], conver it into lower case.

Use two function
1) get_computer_choice
2) get_user_choice

Run comparision and check who won.


## Milestone 4:
Create game model with camera to pay rock-paper-scissor

** Load tensorflow - keras model
** define choices (Rock, Paper, Scissor and Nothing)
** Set "0" points for computer and user

Get random choice for computer as computer_choice
Campture image from webcam as user_choice and get probability output 

Set timer in the beginning to start the game. Use time.time() function to avoice video screen freez.

Compare coumputer_choice vs user_choice and predict result - winner.

At the end set an option to play again by pressing enter key.
