import random

x = random.randint(1,100)

y = int(input('Enter a number greater than 0 and less than 101 '))

while (y < 1 or y > 100):
        y = int(input('Please Enter a number greater than 0 and less than 101 '))

z = int(input("""Guess if your number is greater, less than or equal to the computers number
              1. Greater
              2. Less
              3. Equal
              
              Use 1,2, or 3 to answer if you answer correctly you win otherwise computer wins """))

while z > 3 or z < 1:
    z = int(input("""The choice you entered is invalid
                  Please only enter 1,2 or 3
                  1. Greater
                  2. Less
                  3. Equal
                  
                  Use 1,2, or 3 to answer if you answer correctly you win otherwise computer wins """))
if z == 1:
    if x > y:
        print(f"you entered {y} computer selected {x} you lose")
    elif x < y:
        print(f"you entered {y} computer selected {x} you win")
    elif x == y:
        print(f"you entered {y} computer selected {x} game tied") 
elif z == 2:
    if x > y:
        print(f"you entered {y} computer selected {x} you win")
    elif x < y:
        print(f"you entered {y} computer selected {x} you lose")
    elif x == y:
        print(f"you entered {y} computer selected {x} game tied")
elif z == 3:
    if x > y:
        print(f"you entered {y} computer selected {x} you lose")
    elif x < y:
        print(f"you entered {y} computer selected {x} you lose")
    elif x == y:
        print(f"you entered {y} computer selected {x} game win")
else:
    print("The choice you entered is invalid")