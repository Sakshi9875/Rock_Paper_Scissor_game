import random
def gamewin(comp,you):
    if comp == you:
      return None
    elif comp == 'R':
        if you =='P':
            return True 
        elif you =='S':
            return False
    elif comp == 'S':
        if you =='P':
            return False 
        elif you =='R':
            return True
    elif comp == 'P':
        if you =='R':
            return False 
        elif you =='S':
            return True
print("comp turn: rock(R) paper(P) scissor(S)")
randno = random.randint(1,3)
if randno == 1:
    comp = 'R'
elif randno == 2:
    comp = 'P'
elif randno ==3:
    comp = 'S' 
you = input("your turn:rock(R) paper(P) scissor(S)")
a = gamewin(comp,you)
print(f"computer choose{comp}")
print(f"you choose{you}")
if a == None:
    print("game is tie!")
elif a :
    print("you win!")
else:
    print("you lose")    










