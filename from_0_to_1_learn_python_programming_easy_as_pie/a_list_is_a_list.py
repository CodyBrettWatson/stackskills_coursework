list_var = [3.14, 25, "Cody"]
list_var.append("new last element of list")
list_var.insert(0, "new first element of list")
print (list_var)

# First, we build a list (list_var) with different data type variables, a float, a number, and a string.
# Second, we are appending a new item, in this case a string, to list_var. Append will add the new item to the end of the list.
# Third, we are inserting a new item into list_var, while assigning its position within the list (denoted by the 0). In this case,
# the new item, another string, will become the new first item in the list.
# Lastly, we print list_var in order to have an output.

# List indexing
list_var[1:4] # This chooses all items in the list starting with item 1(the second item) and ending before item 4 (meaning the 
# fourth item in the list) will be displayed.
list_var[1:] # This chooses all items in the list from item 1 till the end of the list, any item before 1 will not be included.
list_var[:4] # This chooses all items in the list from the beginning until the item prior to item 4. Item 4 and any item listed
# after item 4 will not be included in the output.

# Removing items/elements from a list
a = [0, 2, 2, 3]
a.remove(2) # Removes the first matching value, not a specific index. In this case it will remove the first '2' in the list and
# and not the item indexec at 2 which also happens to be '2'.
a

b = [3, 2, 2, 1]
del b[1] # Removes a specific index. In this case the the item at index 1, '2', will be deleted from the list. If this were remove
# then the last item in the list, '1', would be removed, since it is the first item to match the value.

c = [4, 3, 5]
c.pop(1) # Returns the removed element. This is slightly less intuitive. This is removing the item at a specific index and then
# making that number the output. In this case the number being removed is '3' which will also be the output.

# More notes on list indexing
somestring = 'some string'
# This itself is a list of individual character strings. So indexing somestring[1] = 'o'

