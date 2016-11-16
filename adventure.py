# An adventure game
name = ""
from random import randint
def player_name():
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
            player_name()
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
        scene3b()
    else:
        print("Answer not recognised")
        scene2()

def scene3a():
    global name
    print("""The teleporter took no time at all. 'I bet you're glad you went through there' you hear.
    You aren't alone. Your old friend was coming along for the ride, one you had not seen since your last mission.
    There had been ups and downs, but considering your friend was a turned robot, you feel a little concern for your friend.""")
    print("Do you...")
    print("Take them with you")
    print("Leave them behind")
    reply = input("Take or leave?: ")
    if reply.lower() == "take":
        scene4a()
    elif reply.lower() == "leave":
        scene4b()
    else:
        print("Answer not recognised")
        scene3a()

def scene3b():
    global name
    print("""You choose not to go through the portal. You'd had enough issues with them in the past.
    You would do it the old fashioned way. You walk to the garage. But which vehicle will get you there faster?""")
    print("Do you take...")
    print("The hoverboard?")
    print("Or the car?")
    choice = input("Board or car?: ")
    if choice.lower() == "board":
        print("Don't be stupid - both humans and robots aren't that smart.")
        scene4c()
    elif choice.lower() == "car":
        scene4c()
    else:
        print("Answer not recognised")
        scene3b()

def scene4a():
    global name
    print("""You can't bare to see the digital face on your friend droop, so you let them join you,
    besides, you have a feeling there will be things you will not be able to do.
    You realise that you are close enough to make three choices. The front door was in plain sight,
    not paticularly guarded either. The roof and side entrances were easily accessible with the gadgets you could get hold of.
    And then there was the disguise method. It had worked in the past, why wouldn't it now, right?""")
    print("How do you get in?")
    print("Do you...")
    print("Make a loud and obvious entrance?")
    print("Disguise as a robot and snoop around?")
    print("Or sneak in?")
    choice = input("Loud, disguise or secret?: ")
    if choice.lower() == "loud":
        scene5a()
    elif choice.lower() == "disguise":
        print("""You stroll into the building looking clearly not very robot-like.
    The robots notice too. You get multiple rounds shot into your stomach. The end.""")
        player_name()
    elif choice.lower() == "secret":
        scene5b()
    else:
        print("Answer not recognised")
        scene4a()
    

def scene4b():
    global name
    print("hi", name, ". this is scene 4b. it's not completed yet")

def scene4c():
    global name
    print("hi", name, ". this is scene 4c. it's not completed yet")

def scene5a():
    global name
    print("hi", name, ". this is scene 5a. it's not completed yet")

def scene5b():
    global name
    print("hi", name, ". this is scene 5b. it's not completed yet")
    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    player_name()
