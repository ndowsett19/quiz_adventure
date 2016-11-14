# An adventure game
name = ""
from random import randint
def name():
    global name
    name = input("Please enter your name. It may affect your future: ")
    scene1()

def scene1():
    global name
    print("You recieve a call.")
    print("You have been asked to do one of the most complicaed jobs ever requested of you")
    print("Do you accept the job?")
    answer = input("Yes or no?: ")
    if answer.lower() == "yes":
        scene2()
    elif answer.lower() == "no":
        print("Well, that was boring. Do you want to try again?")
        answer = input("Yes or no?: ")
        if answer.lower() == "yes":
            scene1()
        elif answer.lower() == "no":
            name()
        else:
            print("Answer not recognised.")
            scene1()
    else:
        print("Answer not recognised.")
        scene1()

def scene2():
    global name
    print("You accepted the job")
    print("""You're given the low down - 25 years since the robots took over, and no one could stop them.
    The agency believe you are the only one capable of doing so. You will be teleported near the headquarters,
    but from there, you can choose how you do it""")
    print("You hear a whoosh behind you - it was a sound you had heard before")
    choice = input("Do you step through the portal? Yes or no?: ")
    if choice.lower() == "yes":
        scene3a()
    elif choice.lower() == "no":
        print("hi")
    else:
        print("Answer not recognised")
        scene2()

def scene3a():
    global name
    print("""The teleporter took no time at all. 'I bet you're glad you went through there' you hear.
    You aren't alone. Your old friend was coming along for the ride, one you had not seen since your last mission.
    There had been ups and downs, but considering your friend was a turned robot, you feel a little concern for your friend.
    The robot continues. 'I'm sure you wouldn't be able to get to Russia without a little help.'""")
    print("Do you...")
    print("Take them with you")
    print("Leave them behind")
    reply = input("Take or leave?: ")








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    name()
