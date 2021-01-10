spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1]) # Last Element
print(spam[-2]) # 2nd Last Element
print(spam[0:4]) # Prints out elements from 0 index up to 4th index
print(spam[0:-1]) # Same as above but in a different way

# We can concatenate list like the following
print([1,2,3] + ['A','B','C'])
# We can also replicate a list multiple times
print([1,2,3] * 3)

# We can also remove values from a list 
del spam [1]
print(spam)

# Use append to add elements to the end of a list
# Use insert to add elements to a certain place in the list
spam.append('moose')
spam.insert(1, 'chicken')
print(spam)

# We can remove elements 
spam.remove('elephant')

# To make copies of a list, we do the following (deepcopy is used for list that contain other list)
import copy
new = copy.copy(spam)
new[1] = "Hello"
print(new)
print(spam)
