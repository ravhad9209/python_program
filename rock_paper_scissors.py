import random

choices = ["rock","paper","scissors"]

while True:
        user_choices = input("enter the choices(rock,paper,scissors):").lower
        if user_choices in choices:
                break
        else:
                print("Invalid choices.please choose from rock,paper,scissors")

computer_choices = random.choices(choices)

print(user_choices)
print(computer_choices)

if user_choices == computer_choices:
        print("it's a tie")

elif (user_choices == "rock" and computer_choices == "scissors") or \
     (user_choices == "paper" and computer_choices == "rock") or\
     (user_choices == "scissors" and computer_choices == "paper"):
        print("you win")

else:
        ("computer win")

if __name__ == "__main__":
    play_rock_paper_scissors()        
          


