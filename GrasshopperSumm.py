'''
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:
summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

'''

# Ex 1
# Mathematical shortcut
def sum(n):
    return n * (n + 1) // 2

  
# Ex 2:
# Loop 
def summation(num):
    total = 0
    for i in range(0, num+1):
        total = total + i
    return total



assert(sum(5)) == 15
assert(sum(3)) == 6
assert(summation(6)) == 21

    
