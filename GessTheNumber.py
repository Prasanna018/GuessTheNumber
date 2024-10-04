

print('''
      Guess the Number between the 1-10 \n
      You Get Only 3 Chances to identify the Number
 ''')

import random
  
Computer_Number=random.randrange(0,11)
print(Computer_Number)

def PlayGame():
    Chances=3
    while(Chances > 0):
     User_Input=int(input("Enter the Number : "))
     if(User_Input>10):
      print("Please enter the Number between '1 to 10'")
     Chances=Chances-1
     if(User_Input==Computer_Number):
      print("You guessed Correctly")
      return 
    else:
      print("not correct reenter the number ")
    

 

PlayGame()



    
    