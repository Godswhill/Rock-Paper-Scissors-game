import random
print("welcome to the rock paper scissors game")
choose = int(input("enter 0 for rock, 1 for paper, 2 for scissors\n"))
if choose > 2 or choose <0:
    print ("you entered a wrong number, you lose")
else:
    rock= '''
              _______
          ---'   ____)
                (_____)
                (_____)
                (____)
          ---.__(___)


    '''
    paper = '''
               _______
           ---'   ____)___
                    ______)
                    _______)
                   _______)
          ---.__________)
    '''

    scissor = '''
              _______
          ---'   ____)____
                    ______)
                 __________)
                (____)
          ---.__(___)
    '''


    rock_paper_sci = [rock, paper, scissor]
    user_choice = rock_paper_sci[choose]
    computer1 = random.randint(0, 2)
    com=int(computer1)
    computer = rock_paper_sci[computer1]
    print("you chose")
    print(user_choice)
    print("computer chose")
    print(computer)

    if choose == 0 and com == 2:
        print("you win")
    elif choose == 1 and com == 0:
        print("you win")
    elif choose == 2 and com == 1:
        print("you win")
    elif choose == com:
        print("its a draw")

    else:
        print("you lose")
