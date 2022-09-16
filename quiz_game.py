print("Welcome to my Computer Quiz!!")
playing = input("Do you want to play this game? ")
if playing.lower() != "yes":
    quit()
print("Ok! Let's Play.")
score = 0

answer = input("What is CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print()
print("****Your Score****")
print("You have scored " + str(score) + " point.")
print("You got " + str((score / 4) * 100) + "%.")
