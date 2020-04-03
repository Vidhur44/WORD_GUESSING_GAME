import time,random

print("What's your name??")
user_name=input()
print()

print("Hello "+user_name+"!!..."+"Let's Start the Game !!")
print()

time.sleep(1)

print("Start Guessing : ....")

turns=10
print("Turns Left : "+str(turns))

words=['secret','apple','chocolate','india','python','java','time',
          'coronavirus','game','milkshake','bottle','friends',
          'movies','abstract','photography','canon','nikon','sony','laptop']

word = random.choice(words)

guesses=''

while turns > 0:
    failed=0

    for char in word:
        if char in guesses:
            print(char)

        else:
            print('*')

            failed+=1

    if failed == 0 :
         print("You Won !!!")
         print()
         print("The Word is : "+word)
           
         break
             


    guess=input("Guess a character: ")
    guesses+=guess

    if guess not in word:
       turns-=1
       print("Turns Left : "+str(turns))
       if turns == 0:
            print("You ran out of Turns & You Lost !!") 
       else: 
            print("Wrong Guess....Try again !!")

 
