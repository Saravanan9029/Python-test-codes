import time
import random
num=[]
p1=[]
p2=[]
s1,s2=0,0
name1=input("Player 1 Enter Your Name:")
name2=input("Player 2 Enter Your Name:")
print("Hello {} and {}, Welcome to the Choice Game".format(name1,name2))
print("Computer Has Choosen 5 numbers")
print("You both have 3 chances to guess the numbers")
print("Lets begin the game")
while len(num)!=5:
    n=random.randint(1,15)
    if n in num:
        n=random.randint(1,15)
    else:
        num.append(n)
for i in range(3):
    print("------------------TURN{}------------------".format(i+1))
    x=int(input("{} Enter Your Choice:".format(name1)))
    while x in p1 or x in p2:
          x=int(input("DUPLICATE CHOICE,{} Enter Your Choice AGAIN:".format(name1)))
    p1.append(x)
    if x in num:
        print("CORRECT")
        s1=s1+1
    else:
        print("WRONG")
    y=int(input("{} Enter Your Choice:".format(name2)))
    while y in p1 or y in p2:
          y=int(input("DUPLICATE CHOICE,{} Enter Your Choice AGAIN:".format(name2)))
    p2.append(y)
    if y in num:
        print("CORRECT")
        s2=s2+1
    else:
        print("WRONG")
print("COMPUTER HAS CHOOSEN {}".format(num))
print("{} had choosen :{}".format(name1,p1))
print("So {} scored {} points".format(name1,s1))
print("{} had choosen :{}".format(name2,p2))
print("So {} scored {} points".format(name2,s2))
print("SO FINALLY THE WINNER IS.............")
if s1>s2:
    print("{} is the WINNER".format(name1))
elif s1<s2:
    print("{} is the WINNER".format(name2))
else:
    print("THE MATCH HAS BEEN DRAWN")
