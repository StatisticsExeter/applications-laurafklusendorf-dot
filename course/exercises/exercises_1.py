
###"""Return the sum of all elements in the list 'numbers'."""
def sum_list(numbers):
    x=sum(numbers)
    return x
numbers= [1,2,3,4,5]
sum_list(numbers)


###    """Return the first element of the tuple 't'."""
def first_of_tuple(t):
    first=t[0]
    return first
mytuple=("Inky", "Pinky", "Blinky", "Clyde")
first_of_tuple(mytuple)


###"""Return True if 'key' exists in dictionary 'd', else False."""
def has_key(d, key):
    if key in d:
      return True
    else:
      return False
    
key = 4
d= [1,2,3,5]
has_key(d, key)

###    """Round the float 'f' to 2 decimal places."""
def round_float(f):
    rounded=round(f, 2)
    return rounded
f=2.32623
round_float(f)


###    """Return a new list that is the reverse of 'lst'."""
def reverse_list(lst):
    reverse=lst[::-1]
    return reverse
lst=[1,2,3,4,5]
reverse_list(lst)


### """For a list of items 'lst', count how many times element 'item' occurs."""
def count_occurrences(lst, item):
    count=lst.count(item)
    return count
lst=[1,1,1,2,2,3,3,5,6,7,7]
item=1
count_occurrences(lst, item)


###  """Convert a list of (key, value) tuples 'pairs' into a dictionary."""
def tuples_to_dict(pairs):
    dictionary=dict(pairs)
    return dictionary
  
pairs = [('a',1),('b',2),('c',3)]
tuples_to_dict(pairs)

###    """Return the number of characters in string 's'."""
def string_length(s):
    length=len(s)
    return length
s=("Laura Klusendorf")
string_length(s)


###    """Return a list of unique elements from 'lst'."""
def unique_elements(lst):
    unique = list(set(lst))
    return unique
  
lst=[1,1,1,2,3,4,5,5,5,6,6]
unique_elements(lst)


###    """Return a new dictionary with keys and values of 'd' swapped."""
def swap_dict(d):
    swap={value: key for key, value in d.items()}
    return swap

d={'a':1, 'b':2, 'c':3}
swap_dict(d)


