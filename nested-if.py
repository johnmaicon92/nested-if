"""
Question 1
Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

Buggy Code:

place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")
"""

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
else:
    print("You found a hidden treasure!")




"""
Task 2: Setting the Scene

Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.
"""

place = input("Choose a place: forest or cave? ").lower()

if place == "forest":
    action = input("climb a tree or cross a river? ").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
   action = input("Would like to light a torch or proceed in the dark? (torch or dark) ").lower()
   if action == "torch":
       print("You found a hidden chamber filled with gold coins!")
   else:
       print("You found a dark cave, but it's too dark to see anything.")
else:
    print("Uh oh! Should we try again and continue this adventure?")



"""
Task 3: Default Path

If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?
"""

place = input("Choose a place: forest or cave? ").lower()

if place == "forest":
    action = input("climb a tree or cross a river? ").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
   action = input("Would like to light a torch or proceed in the dark? (torch or dark) ").lower()
   if action == "torch":
       print("You found a hidden chamber filled with gold coins!")
   elif action == "dark":
       print("You found a dark cave, but it's too dark to see anything.")
   else:
       pass
else:
    print("Uh oh! Should we try again and continue this adventure?")





"""
Question 2. Quick Decisions: The Event Planner 

Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

Buggy Code:

attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
"""

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)



"""
Task 2: Venue Selection

Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.
"""

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"

if attendees > 100:
    print(f"The recommended venue for {attendees} attendees is a {venue} with audio system.")
else:
    print(f"The recommended venue for {attendees} attendees is a {venue} with projector.")

"""a Simpler code"""
# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" if attendees > 100 else "conference room"

# if venue == "large hall":
#     print("Consider taking an audio system to the Large hall")
# else:
#     print("A projector should be enough for the Conference Room")





"""
Task 3: Catering Choices

Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
"""

attendees = int(input("Enter number of attendees: "))
vegetarian_food = input("Would you like vegetarian food? yes/no ")
venue = "large hall" if attendees > 100 else "conference room"

if attendees > 100:
    print(f"The recommended venue for {attendees} attendees is a {venue} with audio system.")
else:
    print(f"The recommended venue for {attendees} attendees is a {venue} with projector.")
if vegetarian_food == "yes":
    print("Recommended caterer: Veggie Delight Caterers")
else:
    print("Recommended caterer: Gourmet Meals Caterers")