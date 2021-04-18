
#input name
name = input("Please enter your name: ")

#start of game/ intro
print("welcome to Evading Malware The Game,", name, "lets get started!")
print(" ")
print("Its 1 o'clock in the afternoon,", name, " woke up and realized that they slept in. ")


#downstairs or computer?
print("Now that you are up, what will you do?")
print(" ")
print("if you want to go on your computer, type 1")
print("if you want to go downstairs, type 2")


print(" ")

answer1 = input("Which option do you want? ")

#decide computer or downstairs

while answer1 != "1" or answer1 != "2":
  answer1 = input("Which option do you want? ")
    

  if answer1 == "1":
    print("yeah")
  elif answer1 == "2":
      print("You then decide to go downstairs, and you think, what would I want to eat?")
      print("enter")

      #making food

      food = input("what do you want to eat?: ")
      print("enter")

      print("You decide to make yourself some", food , "but somehow ended up burning it. How did you manage to mess that up?")
      print("You then decide to go out on a walk but end up seeing one of your friends")

      #talk to friend

      friend_name = input("What is your friends name?: ")


      #name easter egg

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

        #decide on friend name

      else:
        print("You say hi to", friend_name ,"and you continute to walk.")
        print('You admire the scenery and say to yourself "this is some nice scenery" ')
        print("At this point you have been walking for about 4 hours when you realize that you are hungry again")

        #resteraunt
        print(" ")
        print("You then see three resteraunts up ahead, Mcdonalds, KFC and Taco Bell ")
        print(" ")
        print("to go to mcdonalds, type 1")
        print("to go to KFC, type 2")
        print("to go to Taco Bell, type 3")
        resteraunt = input("which resteraunt will you go to?: ")

        #resteraunt descision 

        while resteraunt != "1" or resteraunt != "2" or resteraunt != "3":
          resteraunt = input("which resteraunt will you go to?: ")
        
          if resteraunt == "1":
            print("You ordered a big mac and enjoyed your meal but still feel hungry")
          elif resteraunt == "2":
            print("You ordered a bucket of chicken and enjoyed your meal, you are now full")
          elif resteraunt == "3":
            print("You ordered 20 soft tacos and that was too much for you to handle. You threw up half of it but still feel full")

          #car crash
          print(" ")
          print("As you are about to leave the resteraunt a car comes crashing through the side entrance")
          print("You see a person injured as the building begins to catch fire, what will you do?")
          print("If you want to sit there and finish your drink, type 1")
          print("If you want to help the person out, type 2")
          print("If you want to walk out the door and pretend you saw nothing, type 3")


          #choose the crash options

          crash_choice = input("which you chose?: ")

          if crash_choice == "1":
            print("You decide that you do not care that a car has come crashing through into the building and continue to sit there and drink the sprite you didnt finish.")
            print("Your realized that it tastes funny, thats because some antifreeze from the car got into your drink and shut down your organs.")
            print("You fell on the floor and your kidneys proceeded to shut down")
            print(" ")
            print("TRY AGAIN NEXT TIME!")
          elif crash_choice == "3":
            print("You start walking out of the resteraunt and just as you think that you are in the clear an ambulance comes out of no where and hits you, sending you flying 30 feet into a nearby pond and get eaten by the local aligators because you are a terrible person.")
            print(" ")
            print("TRY AGAIN NEXT TIME!")
          elif crash_choice == "2":
            print("you run over and help the injured person and ")


