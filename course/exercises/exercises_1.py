
###"""Return the sum of all elements in the list 'numbers'."""
def sum_list(numbers):
    x=sum(numbers)
    return x


###    """Return the first element of the tuple 't'."""
def first_of_tuple(t):
    first=t[0]
    return first


###"""Return True if 'key' exists in dictionary 'd', else False."""
def has_key(d, key):
    if key in d:
      return True
    else:
      return False
    

###    """Round the float 'f' to 2 decimal places."""
def round_float(f):
    rounded=round(f, 2)
    return rounded


###    """Return a new list that is the reverse of 'lst'."""
def reverse_list(lst):
    reverse=lst[::-1]
    return reverse



### """For a list of items 'lst', count how many times element 'item' occurs."""
def count_occurrences(lst, item):
    count=lst.count(item)
    return count



###  """Convert a list of (key, value) tuples 'pairs' into a dictionary."""
def tuples_to_dict(pairs):
    dictionary=dict(pairs)
    return dictionary


###    """Return the number of characters in string 's'."""
def string_length(s):
    length=len(s)
    return length



###    """Return a list of unique elements from 'lst'."""
def unique_elements(lst):
    unique = list(set(lst))
    return unique
  



###    """Return a new dictionary with keys and values of 'd' swapped."""
def swap_dict(d):
    swap={value: key for key, value in d.items()}
    return swap



