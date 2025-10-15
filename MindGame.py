import random
import time

print("Welcome to MIND MASTER")
print("Train your focus, logic, and memory!\n")

while True:
    print("Press 1 - Start the Game \nPress-2 To Exit")
    start = time.time()
    choice = input("Enter the number(1-2): ")
    score  = 0
    match choice:
        case '2':
            print("------Exiting the game------")
            break
    print("Level 1: Simple Math Challenge:-- Answer 4 ques!")
    for i in range(4):
        a = random.randint(1,100)
        b = random.randint(1,10)
        op = random.choice(["+", "-","*","%","/"])
        ques = f"{a} {op} {b}"
        ans= int(eval(ques))
        aUser = int(input(f"Q{i+1}. What is the ans of {ques}? "))
        if aUser== ans:
            print("Correct, You earned 10 points!")
            score +=10
        else:
            print(f"Wrong! Answer was {ans}")
    print(f"\nYour math score: {score}\n")  
    
    print("Memory Test: Remember the sequence!")
    print("You will be displayed with the list remember it and then try to reenter it!-- 5sec timer")
    seq = [random.randint(1,9) for _ in range(5)]
    print(seq)
    for i in range(5,0,-1):
        print(f"Countdown: {i}",end="\r")
        time.sleep(1)
    print("\033[E" + " "*50 , end="\r")
    print("\033[F" + " "*25 , end="\r")
    user_seq = input("Enter the sequence you remember (space-separated): ").split()
    user_seq = [ int(i) for i in user_seq]
    if user_seq == seq:
        print("Coreect!")
        score += 20
    else:
        print(f"Wrong!Correct ans is {seq}")
    print(f"\nTotal Score: {score}")
    
    print("\nPattern Logic Test:")
    print("Find the next number in the sequence:")
    patterns = {
        "1" : [2,4,8,16],
        "2" : [3,6,9,12],
        "3" : [5,10,20,40]
     }
    key = random.choice(list(patterns.keys()))
    seqq = patterns[key]
    print(seqq)
    ans3 = int(input("Enter the next number: "))

    if (key == "1" and ans3 == 32) or (key == "2" and ans3 == 15) or (key == "3" and ans3 == 80):
        print("You’ve got great logical power!")
        score += 30
    else:
        print("Wrong logic!")
        print("Correct answer was:", 32 if key == "1" else 15 if key == "2" else 80)
    end = time.time()
    
    print("\nFINAL SCORE:", score)
    print("TIme taken: ", round(end-start, 3),"sec")
    if score >= 50:
        print("You’re a Mind Master!")
    elif score >= 30:
        print("Great! Your mind is sharp.")
    else:
        print("Keep practicing to level up your mental power.")

    

