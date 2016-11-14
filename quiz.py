# Our quiz!

wscore = 0
fscore = 0
escore = 0
ascore = 0
name = ""

def quiz():
    global wscore
    global fscore 
    global escore
    global ascore
    global name
    print("Welcome to a quiz upon which you shall discover your true elemental power...")
    name = input("Please enter you name: ")
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()
    q10()

    print("water =", wscore, "%")
    print("fire =", fscore, "%")
    print("earth =", escore, "%")
    print("air =", ascore, "%")

def q1():
    global wscore, fscore, escore, ascore
    global name
    print("Welcome to a quiz upon which you shall discover your true elemental power...")
    print("Question 1 - How would you describe your personality most?")
    print("A: Calm and collected")
    print("B: Headstrong and quick-thinking")
    print("C: Down-to-Earth and brave")
    print("D: Creative and crazy")
    answer = input("Pick your answer: ")
    if answer.lower() == "a":
        wscore += 10
    elif answer.lower() == "b":
        fscore += 10
    elif answer.lower() == "c":
        escore += 10
    else:
        ascore += 10
def q2():
    global wscore, fscore, escore, ascore
    global name

    print("Question 2 - What is your favourite colour?")
    print("A: Blue")
    print("B: Orange")
    print("C: Red")
    print("C: Yellow")
    print("D: Green")
    print("E: Brown")
    print("F: White")
    print("G: Black")
    print("H: Silver")
    answer = input("Pick your answer: ")
    if answer.lower() == "a" or answer.lower() == "d":
        wscore += 10
    elif answer.lower() == "b" or answer.lower() == "c":
        fscore += 10
    elif answer.lower() == "e" or answer.lower() == "g":
        escore += 10
    else:
        ascore += 10
def q3():
    global wscore, fscore, escore, ascore
    global name
    print("Question 3 - What is your weapon of choice?")
    print("A: Nunchucks")
    print("B: Trident")
    print("C: Bow and Arrow")
    print("D: Sharks")
    print("E: Sword")
    print("F: Magic")
    print("G: Flamethrower")
    print("H: A Skeleton Army")
    answer = input("Pick your answer: ")
    if answer.lower() == "b" or answer.lower() == "d":
        wscore += 10
    elif answer.lower() == "g" or answer.lower() == "f":
        fscore += 10
    elif answer.lower() == "h" or answer.lower() == "e":
        escore += 10
    else:
        ascore += 10
def q4():
    global wscore, fscore, escore, ascore
    global name
    print("Question 4 - Are you...")
    print("A: The brains?")
    print("B: The brawn?")
    print("C: The speed?")
    print("D: The leader?")
    answer = input("Pick your answer: ")
    if answer.lower() == "a":
        wscore += 10
    elif answer.lower() == "d":
        fscore += 10
    elif answer.lower() == "b":
        escore += 10
    else:
        ascore += 10
def q5():
    global wscore, fscore, escore, ascore
    global name
    print("Question 5 - Which mythical creature is your favourite?")
    print("A: Phoenix")
    print("B: Pegasus")
    print("C: Merpeople")
    print("D: Centaur")
    answer = input("Pick your answer: ")
    if answer.lower() == "c":
        wscore += 10
    elif answer.lower() == "a":
        fscore += 10
    elif answer.lower() == "d":
        escore += 10
    else:
        ascore += 10
def q6():
    global wscore, fscore, escore, ascore
    global name
    print("Question 6 - Which power do you most want?")
    print("A: The ability to fly")
    print("B: Fire protection")
    print("C: Underwater breathing")
    print("D: Earth manipulation")
def q7():
    global wscore, fscore, escore, ascore
    global name
    print("Question 7 - You have £1 million. How do you use it?")
    print("A: Save it")
    print("B: Spend it")
    print("C: Give it to charity")
    print("D: Give it to others")
    answer = input("Pick your answer: ") 
    if answer.lower() == "d":
        wscore += 10
    elif answer.lower() == "b":
        fscore += 10
    elif answer.lower() == "a":
        escore += 10
    else:
        ascore += 10
def q8():
    global wscore, fscore, escore, ascore
    global name
    print("Question 8 - What type of secret base would you have?")
    print("A: A sky base")
    print("B: An underground base")
    print("C: An underwater base")
    print("D: A volcano base")
    answer = input("Pick your answer: ")
    if answer.lower() == "c":
        wscore += 10
    elif answer.lower() == "d":
        fscore += 10
    elif answer.lower() == "b":
        escore += 10
    else:
        ascore += 10
def q9():
    global wscore, fscore, escore, ascore
    global name
    print("Question 9 - Of these eight, what is your favourite food?")
    print("A: Tacos")
    print("B: Vegetables")
    print("C: I prefer water")
    print("D: Chicken")
    print("E: Beef or pork")
    print("F: Soup")
    print("G: Pizza")
    print("H: Eggs")
    answer = input("Pick your answer: ")
    if answer.lower() == "c" or answer.lower() == "f":
        wscore += 10
    elif answer.lower() == "a" or answer.lower() == "g":
        fscore += 10
    elif answer.lower() == "b" or answer.lower() == "e":
        escore += 10
    else:
        ascore += 10
def q10():
    global wscore, fscore, escore, ascore
    global name
    print("Question 10 - Finally, what would be your fighting tactic?")
    print("A: Overpower the enemy")
    print("B: Solid defence")
    print("C: Evasive manoeuvres")
    print("D: Aim for the vital organs")
    answer = input("Pick your answer: ")
    if answer.lower() == "d":
        wscore += 10
    elif answer.lower() == "a":
        fscore += 10
    elif answer.lower() == "b":
        escore += 10
    else:
        ascore += 10





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
