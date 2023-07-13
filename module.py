import random

computer_score = 0
user_score = 0
for d in range(1, 10,1):
    user_guess = int(input("Enter a guess number"))
    computer_guess = random.randint(0,6)
    print(computer_guess)
    if user_guess> computer_guess:
       user_score+=10
       print("user_score is:" +str(user_guess))
    elif computer_guess> user_guess:
       computer_score+=10
       print("computer_score is:" +str(computer_guess))
    elif  computer_guess== user_guess:
       print("No change at all")
    else:
       print("wrong range")
 