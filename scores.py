inputLine = ""

while inputLine != "stop":
#     this is a grading program 
# it helps users to grade according to the scores
    score = int(input("Please enter your score: "))
    if score >= 0 and score <= 100:
        if score >= 90:
            print("A")
        elif score >= 70:
            print("B")
        elif score >= 50:
            print("C")
        elif score >= 30:
            print("D")
        else:
            print("F")
        inputLine = input("Enter stop to discontinue and any other value to continue.")
    else:
        print("please enter a number between 0 and 100")
    



