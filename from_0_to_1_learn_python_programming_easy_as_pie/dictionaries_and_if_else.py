empty_var = {}
# Here we assign a name to an empty dictionary, the dictionary is denoted by the curly braces "{}".
empty_var[25] = "Square of negative 5"
# Now we are adding a key, '25', and the value for that key "Square of negative 5".
# We can add other 'key/value pairs' to the dictionary through the same method.
empty_var['Smart Ladies'] = 'Ada Lovelace' , 'Marie Curie'
# Here I show that we can add multiple values to a single key within the dictionary.
print(empty_var)
# This will give us an output of the entire dictionary.

dict_var = {}
dict_var[3.14]= 'Pi'
print("The value corresponding to the key " + str(3.14) + " is: " + dict_var[3.14])
# Here when we index the dictionary with dict_var[3.14] we are asking the dictionary to return the values
# that are associated with the key '3.14'.
# Sometimes you will get a 'KeyError' this is likely because the key that you are calling on does not 
# yet exist. This is quickly fixed by adding in the key with its appropriate values or by calling a 
# different key.

dict_var.keys() 
# Using the function 'keys()' will output all of the keys within a dictionary. This id very useful for
# when you need to find a specific key within a dictionary but you cant remember what that key might be called.
print(dict_var.values())
# Using the 'values()' function will do the same as the 'keys()' function but for the values of a dictionary.
# This could be beneficial for if you need to check the type of information that is in a dictionary, separate
# from the information provided by the keys.
len(dict_var.keys())
# Using the 'len()' funciton on a dictionary while calling the 'keys()' or 'values()' will give you the number
# of keys or values within the dictionary.


input_key_to_delete = input("Please enter the key you wish to delete from the dictionary ")
# The following checks if the variable 'input_key_to_delete' is within the dictionary 'dict_var'
if input_key_to_delete in dict_var:
    dict_var.pop(input_key_to_delete)
    # Once the variable is found within the dictionary then this line of code is applied to the dictionary
    # Here what we are doing is searching for 'input_key_to_delete' within 'dict_var' then when we find it
    # the function 'pop()' is applied and removes 'input_key_to_delete' and stores it.
    print("Ok, zapped the key/value pair for key = " + input_key_to_delete)
print(dict_var)