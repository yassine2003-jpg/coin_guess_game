import random
#show the option:
print("Welcome the coin guissing Game!")
print("Choose a method to toss the coin:")
print("1 - Use random.random()")
print("2 - Use random.randint()")
method = int(input("Enter 1 or 2: "))
#save the user guise in a variable
guise=input("please choose 'head' or 'tail':").lower()
if guise=="head":
    guise="head"
elif guise=="tail":
    guise="tail"
else:
    print("please type ether head or tail:")
#storing the computer choise:
if method==1:
    PC_answer=random.random()
    if PC_answer<0.5:
        reasult="head"
    else:
        reasult="tail"
elif method==2:
    PC_answer=random.randint(0,1)
    if PC_answer==1:
     reasult="head"
    else:
     reasult="tail"
#showing the reasult:      
else:
   print("please ether type (1 or 2):")     
if guise==reasult:
   print(f"congratulation you win the answer is {reasult}")  
else:
   print(f"sorry wrong guess the answer is {reasult}")