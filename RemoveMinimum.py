# Task

# 1. Given an array of integers, remove the smallest value. 
# 2. Do not mutate the original array/list. 
# 3. If there are multiple elements with the same value, remove the one with a lower index. 
# 4. If you get an empty array/list, return an empty array/list.
# 5. Don't change the order of the elements that are left.


# Ex 1
test1 = [2, 3, 1, 5]
test2 = []
test3 =  [1, 1, 3, 4, 7]

def remove_smallest(numbers):
    x = numbers[:]
    if x:
        x.remove(min(x))
    return x

# Test
print(remove_smallest(test1))
print(remove_smallest(test2))
print(remove_smallest(test3))
  
# Ex 2
def Remove_Smallest(numbers):
    if numbers is None or len(numbers) == 0:
        return []
    copy = numbers.copy()
    copy.remove(min(numbers))
    return copy

# Test
print(Remove_Smallest(test1))
print(Remove_Smallest(test2))
print(Remove_Smallest(test3))