#nested if
drink = input("What would u like to drink?, coffee or tea? : ")
if drink == "coffee":
    sugar= input("What type do u love more?, with suger or black? : ")
    if sugar == "with suger":
        print("Oh!, nice choice, enjoy ur sugary coffee!")
    elif sugar == "black":
        print("r u sure u really want this?!")

if drink == "tea":
    type_of_tea= input("Okay!, traditional choice as we see, so .. green tea or red tea?")
    if type_of_tea == "grean tea":
        print("Lol, seems like u doing a dite!")
    elif type_of_tea == "red tea":
        print("Such a perfect choice, i like red tea too!")
else :
    print("sorry, i don't get it .. can u try again?")