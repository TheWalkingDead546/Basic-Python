import random

possible_choices = ["Rock","Paper","Scissors"]
round_selection = int(input("""Hello Welcome to Rock Papper Scissors game
      
      Please select 1 or 2
      
      1.Best of 3
      2. Best of 5
      : 
      """))

comp_points = 0
user_points = 0

while(round_selection != 1 and round_selection !=2):
    round_selection = int(input("""Invalid Selection
      
      Please select press 1 or 2
      
      1. Best of 3
      2. Best of 5
      : 
      """))

while(True):
    if round_selection == 1:
        i = 1
        while i < 4:
            x = random.choice(possible_choices)
            user_input1 = input("Rock,Paper or Scissors? ")
            user_input = user_input1.capitalize()
            if x == user_input:
                print(f"Computer picked",x, "You picked", user_input, "The game has TIED, 0.5 points each")
                comp_points = comp_points + 0.5
                user_points = user_points +  0.5
            elif (x == "Rock" and user_input == "Paper") or (x == "Paper" and user_input == "Scissors") or (x == "Scissors" and user_input == "Rock") :
                print(f"Computer picked",x, "You picked", user_input, "CONGRATULATIONS YOU WIN ")
                user_points = user_points + 1
            elif (user_input == "Rock" and x == "Paper") or (user_input == "Paper" and x == "Scissors") or (user_input == "Scissors" and x == "Rock") :
                print(f"Computer picked",x, "You picked", user_input,"COMPUTER WINS ")
                comp_points = comp_points + 1
            else:
                print("Invalid Selection")
                continue
            i += 1
    elif round_selection == 2:
        i = 1
        while i < 6:
            x = random.choice(possible_choices)
            user_input1 = input("Rock,Paper or Scissors? ")
            user_input = user_input1.capitalize()
            if x == user_input:
                print(f"Computer picked",x, "You picked", user_input,"TIED, 0.5 points each ")
                comp_points = comp_points + 0.5
                user_points = user_points +  0.5
            elif (x == "Rock" and user_input == "Paper") or (x == "Paper" and user_input == "Scissors") or (x == "Scissors" and user_input == "Rock") :
                print(f"Computer picked",x, "You picked", user_input,"CONGRATULATIONS YOU WIN ")
                user_points = user_points + 1
            elif (user_input == "Rock" and x == "Paper") or (user_input == "Paper" and x == "Scissors") or (user_input == "Scissors" and x == "Rock") :
                print(f"Computer picked",x, "You picked", user_input,"COMPUTER WINS ")
                comp_points = comp_points + 1
            else:
                print("Invalid Selection")
                continue
            i += 1
    print(f"Computer points are", comp_points, "Your points are", user_points )

    if comp_points > user_points:
        print("Computer is victorious")
    elif user_points > comp_points:
        print("Contratulation you are victorious")
    elif user_points == comp_points:
        print("The Game has tied")
    break