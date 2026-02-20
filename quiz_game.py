print("welcome to my computer quiz ")

playing=input("Do you want to play ?").lower()

if playing  !="yes":
    quit()
    
print("okay let's play")
Score=0

answer1 = input("what does CPU stand for ?").lower()
if "central processing unit" in answer1 or "CPU" in answer1:
    print("correct !")
    Score+=1
else:
    print("incorrect !")
    
answer2 = input("what does GPU stand for ?").lower()
if "graphics processing unit" in answer2 or "GPU" in answer2:
    print("correct !")
    Score+=1
else:
    print("incorrect !")
    
answer3 = input("what does RAM stand for ?").lower()
if "random access memory" in answer3 or "RAM" in answer3:
    print("correct !")
    Score+=1
else:
    print("incorrect !")
    
answer4 = input("what does PSU stand for ?").lower()
if "power supply unit" in answer4 or "PSU" in answer4:
    print("correct !")
    Score+=1
else:
    print("incorrect !")
    
print("you got "+str(Score)+" correct out of 4 ")