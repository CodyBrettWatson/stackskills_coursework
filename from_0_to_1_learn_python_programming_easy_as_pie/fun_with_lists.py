regal_input = input("My king what is your name? ")
# Creates a user (the king) input and asks for a name which is declared as the variable 'regal_input'.
number_of_jewels = input("My liege " + regal_input + " how many jewels are there? ")
# Asks for the user to input a number. This is combined with the 'regal_input' variable to create another variable 'number_of_jewels'.
cost_of_each_jewel = input("My lord " + regal_input + " what is the worth of each jewel? ")
# This is the same actions performed by the 'number_of_jewels' variable.
total_prize_size = cost_of_each_jewel * number_of_jewels
# This creates a variable 'total_prize_cost' which is the combination of the other two numerical inputs.

muskateers = ['Athos', 'Pothos', 'Aramis']
# Create a list of strings
muskateers_ages = [55, 34, 67]
# Create a list of numbers
muskateers.insert(0, "D'Artagnan")
# Insert a new string into the list 'muskateers', at the front.
muskateers_ages.append(16)
# Append a number to the list 'muskateers_ages', this automatically adds this number to the back of the list. 
# We have just created a conflict with the order of the data in the two lists. In order to fix this we can do the following.
temp_variable = muskateers.pop(0)
# This stores the removed element from the list as the variable 'temp_variable'.
muskateers.append(temp_variable)
# We then append the 'temp_variable' to the 'muskateers' list, which move it to the back of the list.
# This shifted the newly added name to be in line with its corresponding age in the 'muskateers_age' list.

print("Total number of muskateers" + str(len(muskateers)))
# The str() function converts the len() function output into a string so that it can be combined with the rest of the string output and not have any conflicts.
# The len() function counts the length of a given variable. If it is a list it counts the number of indexes in the list. 
# If it is a sting it counts the individual characters in the string, including whitespace.

scapegoat = input("Your majesty" + regal_input + "which of these malcontents shall be sent to the guillotine? ")
# Here we are just creating another input variable to follow the narrative.

print("Erasing existence of " + muskateers[scapegoat-1] + ",aged" + str(muskateers_ages[scapegoat-1]))
# To follow the narrative we would want to remove the information of the scapegoat. This gives us the information of the scapegoat.