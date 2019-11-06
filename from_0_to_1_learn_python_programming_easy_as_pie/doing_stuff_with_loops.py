muskateers = ['Athos', 'Pothos', 'Aramis', "D'Artagnan"]

# 'Muskateer' takes on the value of the elements within 'muskateers'
for muskateer in muskateers:
    print("The variable 'muskateer' currently contains " + muskateer + ". This is inside a for-loop.")

empty_var = {}
empty_var[25] = 'The square of 5'
empty_var[36] = 'The square of 6'

for dict_key in empty_var.keys():
    print("The dictionary 'empty_var' contains the key " + str(dict_key) + ". This is inside a for-loop.")

for dict_value in empty_var.values():
    print("The dictionary 'empty_var' contains the value '" + str(dict_value) + "'. This is inside a for-loop.")

for dict_value, dict_key in empty_var.values(), empty_var.keys():
    print("The dictionary 'empty_var' contains the value " + str(dict_value) + " with the key " + str(dict_key))
    # This isn't working right yet.

for dict_key in empty_var.keys():
    print("The key '" + str(dict_key) + "' has value '" + empty_var[ dict_key] + "' in the dictionary 'empty_var'.")

break # This allows you to exit the loop once a condition has been met

continue # Same as break except this allows you to move on once a condition has been met.