import random




TopOfRange=input("type a number :")

if TopOfRange.isdigit():
    TopOfRange=int(TopOfRange)
    if TopOfRange <= 0:
        print("please make it lager than 0 next time")
        quit()
    
else:
    print("please write a number next time")
    quit() 
    
random_num=random.randrange(0,TopOfRange)
print(random_num)
while True:
    userGuess=input("guess the number :")
    if userGuess.isdigit():
        userGuess=int(userGuess)
        
    else :
        print("please write a number ")
        continue
    
    if userGuess==random_num:
        print("You win")
        break
    else :
        print("try again ")
        
    