

name = input("Please enter your name: ")
print("welcome to Evading Malware The Game,", name, "lets get started!")
print(" ")
print("Its 1 o'clock in the afternoon,", name, " woke up and realized that they slept in. ")
print("Now that you are up, what will you do?")
print(" ")
print("if you want to go on your computer, type 1")
print("if you want to go downstairs, type 2")


print(" ")

answer1 = input("Which option do you want? ")


if answer1 == "1":
  print("yeah")
elif answer1 == "2":
    print("You then decide to go downstairs, and you think, what would I want to eat?")
    print("enter")
    food = input("what do you want to eat?: ")
    print("enter")
    print("You decide to make yourself some", food , "but somehow ended up burining it. How did you manage to mess that up?")
    print("You then decide to go out on a walk but end up seeing one of your friends")
    friend_name = input("What is your friends name?: ")
    if friend_name == "i have no friends":
      print("You remember that you have no friends and that reminds you, you should take your schizophrenia meds. You take your meds then proceed to keep walking")
      print("You then proceed to walk 3 steps forward and get hit by a car, instantly killing you")
      print(" ")
      print("TRY AGAIN NEXT TIME!")
    elif friend_name == "i dont have any friends":
      print("You remember that you have no friends and that reminds you, you should take your schizophrenia meds. You take your meds then proceed to keep walking")
      print("You then proceed to walk 3 steps forward and get hit by a car, instantly killing you")
      print(" ")
      print("TRY AGAIN NEXT TIME!")
    else:
      print("You say hi to", friend_name ,"and you continute to walk.")
      print('You admire the scenery and say to yourself "this is some nice scenery" ')
      print("At this point you have been walking for about 4 hours when you realize that you are hungry again")
      print(" ")
      print("You then see three resteraunts up ahead, Mcdonalds, KFC and Taco Bell ")
      print(" ")
      print("to go to mcdonalds, type 1")
      print("to go to KFC, type 2")
      print("to go to Taco Bell, type 3")
      resteraunt = input("which resteraunt will you go to?: ")
      if resteraunt == "1":
        print("You ordered a big mac and enjoyed your meal but still feel hungry")
      elif resteraunt == "2":
        print("You ordered a bucket of chicken and enjoyed your meal, you are now full")
      elif resteraunt == "3":
        print("You ordered 20 soft tacos and that was too much for you to handle. You threw up half of it but still feel full")
      print(" ")
      print("As you are about to leave the resteraunt a car comes crashing through the side entrance")
