
def letter_grade(score):
    if (80<= score <90):
        return "B"
    elif (score >= 90):
        return "A"
    elif (70<= score <80):
        return "C"
    elif (60<= score <70):
        return "D"
    else:
        return "F"
print(letter_grade(47))
userinput = int(raw_input("What is your grade"))
print(letter_grade(userinput))


    

  
