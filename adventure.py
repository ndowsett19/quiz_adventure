# An adventure game
name = ""
from random import randint
def player_name():
    global name
    print("\n"*10)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n"*10)
    name = input("Please enter your name. It may affect your future: ")
    scene1()

    
def scene1():
    global name
    print("You recieve a call.")
    print("You have been asked to do one of the most complicated jobs ever requested of you")
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
        fail_ans()
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
        fail_ans()
        scene2()

        
def scene3a():
    global name
    print("""The teleporter took no time at all. 'I bet you're glad you went through there,""", name,"""' you hear, before hearing the portal close.
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
        fail_ans()
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
        fail_ans()
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
        print("""You stroll into the building, you and your friend looking 'very robot-like'.
    The robots notice you. You get multiple rounds shot into your stomach.
    Clearly they know their enemies. The end.""")
        player_name()
    elif choice.lower() == "secret":
        scene5b()
    else:
        fail_ans()
        scene4a()

        
def scene4b():
    global name
    print("""As much as you want to have a companion for this mission,
    risking your friend's life isn't worth it. You tell your friend that you'll be fine.
    Their face drops, but you give them some oil and start your journey.""")
    print("You reach the building. How will you get in?")
    answer = input("Roof or side?: ")
    if answer.lower() == "roof":
        scene5c()
    elif answer.lower() == "side":
        scene5d()
    else:
        print("Answer not recognised")
        scene4b()

    
def scene4c():
    global name
    print("""You get in the car and use satellite navigation to find where you need to be.
    It takes 4 hours to get there. It's not worth it. You get back out of the car and head back to the portal.
    You dive through just as it begins to close""")
    scene3a()

    
def scene5a():
    global name
    random = randint(0, 1)
    if random == 0:
        print("The robots were quick on their feet. Four rockets come plummeting towards you.")
        print("Do you dive out the way or stay put?")
        choice = input("Dive or stay?: ")
        if choice.lower() == "dive":
            scene6a()
        elif choice.lower() == "stay":
            scene6b()
        else:
            fail_ans()
            scene5a()
    else:
        print("You burst through the doors, running past the shooting bots.")
        print("You make it into the corridor, the alarms blaring loud")
        print("There are 2 doors in this corridor. Do you go...")
        choice = input("Left or right?: ")
        if choice.lower() == "left":
            scene6c()
        elif choice.lower() == "right":
            scene6d()
        else:
            fail_ans()
            scene5a()

        
def scene5b():
    global name
    print("""The two of you go around the back, where you are greeted with a ladder and a door.
    Where do you want to go? Up the ladder, or through the door?""")
    choice = input("Ladder or door?: ")
    if choice.lower() == "ladder":
        scene6e()
    elif choice.lower() == "door":
        scene6f()
    else:
        fail_ans()
        scene5b()

    
def scene5c():
    global name
    print("""You climb up a ladder onto the roof. It is guarded by one solitary robot.
    You hide behind a crate, with several things at your disposal. There is a penny, a syringe gun and a whistle.
    Which do you use?""")
    choice = input("Penny, syringe or whistle?: ")
    if choice.lower() == "penny":
        scene6g()
    elif choice.lower() == "syringe":
        print("""You fire at the robot, before realising something. Robots aren't affected by syringes.
    Hey, no matter. You missed anyway, and the syringe is coming right back to you. Sleep tight""")
        scene5c()
    elif choice.lower() == "whistle":
        print("You blow the whistle. Nothing happens. No, wait! You hear a noise approaching you. Hello Robot Guard!")
        scene5c()
    else:
        fail_ans()
        scene5c()


def scene5d():
    global name
    print("You walk towards the door, instantly recognising the code lock to the side.")
    print("Do you take the roof, or decode the door?")
    choice = input("Roof or decode?: ")
    if choice.lower() == "roof":
        scene5c()
    elif choice.lower() == "decode":
        scene6h()
    else:
        fail_ans()
        scene5d()
    
    
def scene6a():
    global name
    print("You dive out of the way, just in time to watch the rockets explode behind you. Your friend took the hit. You see a door.")
    print("Do you make a run for it, or do you stand and fight?")
    choice = input("Run or fight?: ")
    if choice.lower() == "run":
        scene7a()
    elif choice.lower() == "fight":
        scene7b()
    else:
        fail_ans()
        scene6a()

        
def scene6b():
    global name
    print("""You stand your ground, staring at the missiles. You like to face things head on, despite danger.
    Your friend leaps in front of you, stopping the missiles in their tracks before they exploded. You knew it was a mistake to take them with you.
    Mourning your friend results in being fired at again. You fall on the floor, on top of your friend. Game Over.""")

    
def scene6c():
    global name
    print("You run towards the left door and slam it behind you.")
    if name.lower() == "wally":
        print("Despite all efforts to save it, the wireless mouse drops to the ground and shatters. Game Over.")
        player_name()
    elif name.lower() == "noah":
        print("You are faced with an AI, clearly controlling the robots. Do you barter or fight?")
        choice = input("Barter or fight?: ")
        if choice.lower() == "barter":
            scene7c()
        elif choice.lower() == "fight":
            scene7d()
        else:
            fail_ans()
            scene6c()
    elif name.lower() == "alex":
        print("""Seeing such an empty room fills you with determination. You step back outside and destroy the robots.
    hiding in one of the robots, you walk towards the CORE, where you shut off the power and save the world.""")
        goodending()
    elif name.lower() == "andrew" or name.lower() == "chazza":
        print("I am afraid continuing shall cause the death of many people, and proceeding could lead to the destruction of planet Earth.")
        choice = input("Proceed or leave?: ")
        if choice.lower() == "proceed":
              print("You step forward. You've killed us all. The world disintegrates in a flash of dust. Why would you do this? You monster.")
              badending()
        elif choice.lower() == "leave":
            print("""You made the right choice. Literally.
                  You leave the left room because it had to be left behind and enter the right room as it is the right choice.""")
            scene6d()
        else:
            fail_ans()
            scene6c()
    
def scene6d():
    global name
    print("""You enter the right room, and carefully shut the door behind you. A voice startles you.
    "Do you really want to kill us all? After all, without us, you wouldn't be here. We want your help in ruling the world, but we knew you wuold not accept from a simple question,
    so now, we aren't giving you a choice." You had been used. Your friend had too. You feel a pang of guilt inside you. They had died for no reason.""")
    choice = input("Do you accept the offer? Yes or no?: ")
    if choice.lower()  == "yes":
        scene7e()
    elif choice.lower() == "no":
        scene7f()
    else:
        fail_ans()
        scene6d()

def scene6e():
    global name
    print("""You and your friend take the ladder up to the roof. You find a two robot guards
    Do you fight them?""")
    choice = input("Yes or no?: ")
    if choice.lower() == "yes":
        print("The two of you try to take on the powerful guards, but they are too strong. Several bones cracks in your body as you fade from reality.")
        print("Game over.")
        player_name()

    elif choice.lower() == "no":
        scene7h()

    else:
        fail_ans()
        scene6e()

def scene6f():
    global name
    print("""You find a locked door, but your friend is already decoding the password.
    The door swings open shortly after, revealing 3 chutes. Which do you go down?""")
    choice = input("Left, middle or right?: ")
    if choice.lower() == "left":
        print("You fell into a trash compactor. You are squashed to death. Game over")
    elif choice.lower() == "middle":
        scene7g()
    elif choice.lower() == "right":
        print("You go down a chute that leads to a storage room. There is a cake. You try and eat it. The cake is a lie. Game Over")
    else:
        fail_ans()
        scene6f()

def scene6g():
    global name
    random = randint(0, 1)
    if random == 0:
        print("""You pick up a penny and throw it next to the robot. The robot notices, says "Ooh, a penny" and reaches to pick it up.
    All the while, you sprint to the vent and slide down.""")
        scene7g()
    else:
        print("You run, expecting it to reach down, but it spots you and shoots you off the roof. Game over")
        player_name
    

def scene6h():
    global name
    print("""You try and fail to hack the mainframe. Little did you know, alarms had been set off.
    You are surrounded. You have no escape and the door is not budging. You take a bullet to every possible bodily place.
    Ouch. Game Over.""")
    player_name()
    
def scene7a():
    global name
    print("Running, you reach a door. Behind it lies some sort of machine. You already know what it does.")
    print("Do you leave it on or turn it off?")
    choice = input("On or off?: ")
    if choice.lower() == "on":
        print("A fools choice. The enemy know where you are, and you have just surrendered to them. Game ov-")
        scene8a()
    elif choice.lower() == "off":
        scene8b()
    else:
        fail_ans()
        scene7a()

def scene7b():
    global name
    print("A feel for revenge takes over your body as you charge in.")
    random = randint(0, 3)
    if random == 3:
        scene8c()
    else:
        print("You took out", random, "of the four robots, but the ones left standing slice through you weak and feeble body with ease")
        print("Game over")
        player_name()

def scene7c():
    global name
    print("""You make an attempt to barter with the AI. You show them mercy and they hold off the whole "taking over the world" thing.""")
    random = randint(0, 1)
    if random == 0:
        print("""The robots accept that they are in the wrong, and set you free, before anything else happens.
              A portal opens up outside""")
        scene9a()
    else:
        print("The AI would have none of it, and filled the room with a deadly neurotoxin, capable of killing humans with a single breath.")
        print("Game over.")
        player_name()
        
def scene7d():
    global name
    print("""You have no choice but to fight. Charging forwards, you summon the strongest armour you have and the most deadly sword you can think of.
    The demonforged armour encases your body, and the soul reaper sword enters your hand, and with a flick of your wrist, the sword slices through wires and tubes.
    The monitor falls onto the ground and lays lifeless like it had been killed. Which it had. A portal opens up at the doorway, and as you walk towards it,
    you unequip your armour.""")
    goodending()

def scene7e():
    global name
    print("You take over the world together, having good times, without any regrets.")
    print("\n"*20)
    print("Then you get stabbed in the back. The end")
    badending()

def scene7f():
    global name
    print("You choose not to help them, but as they said, you had no choice. They obliterate you on the spot, leaving a pile of dust.")
    print("Game over")
    player_name()

def scene7g():
    global name
    print("""The chute takes you down to a room full of precious treasure, and an exit to the surface.
    But you are too cool to take the stairway up. You summon the portal to your location. Do you take the treasure or leave it?""")
    choice = input("Take or leave?: ")
    if choice.lower() == "take":
        scene8d()
    elif choice.lower() == "leave":
        print("All the evidence was left behind, and the robots were never found out or terminated.")
        badending()

def scene7h():
    global name
    print("""You sneak around the robots, making it past them. You are through the door before they even notice you were there.
    The next room is filled with water, and your friend fries, electrocuting you in the process. Game over.""")
    player_name()


def scene8a():
    global name
    print("""The robots have taken you to their leader. You are told to leave, and not to bother them again.
    Next time will result in certain death. It doesn't stop you from trying, though, does it. Nothing does.""")
    goodending()

def scene8b():
    global name
    print("""You turn the machine off, hearing the lively buzz of the machine die down.
    A portal opens up on the other side of the room, where you return home for the final word""")
    scene9a()

def scene8c():
    global name
    print("""You destroy all four robots, before moving on into the next corridor. There are two doors. The left and the right.""")
    choice = input("Left or right?: ")
    if choice.lower() == "left":
        scene6c()
    elif choice.lower() == "right":
        scene6d()
    else:
        fail_ans()
        scene8c()

def scene8d():
    global name
    print("""You keep the portal open while you carry every last piece of the treasure into your house.
    Summoning the agency, they pin the robots down for theft and save the world.""")
    goodending()

def scene9a():
    global name
    print("Congratulations", name, """!, is the first thing you hear as you pass through the doorway.
    You had saved the world, and humankind were now free to live however they pleased,
    without the imposing reign of the dreaded bots. You knew full well what would be happening next.
    You were going to be reinstated as an agent, but first, you had a party to show up to...""")
    goodending()


def goodending():
    global name
    print("\n"*5)
    print("Congratulations", name, "! You have completed one of many endings. Would you like to try and get them?")
    answer = input("Yes or no?: ")
    if answer.lower() == "yes":
        player_name()
    else:
        quit()

def badending():
    global name
    print("\n"*5)
    print("Sucks to be you. You failed. Unlucky.")
    print("\n"*10)
    print("But this is an ending, so we'll call it the bad one.")
    answer = input("Try again? Yes or no?: ")
    if answer.lower() == "yes":
        player_name()
    else:
        quit()

def fail_ans():
    global name
    print("Answer not recognised")







# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    player_name()
