'''
Task:
Your task is to write a function which returns the sum of following series upto nth term(parameter).
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:
- You need to round the answer upto 2 decimal places and return it as String.
- If the given value is 0 then it should return 0.00
- You will only be given Natural Numbers as arguments.
Examples:
SeriesSum(1) => 1 = "1"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
'''


# Ex 1:
def series_sum(n):
    return '{:.2f}'.format(sum(1.0 / (3 * i + 1) for i in range(n)))


# Ex 2:
def series_sum1(n):
    sum = 0.0
    for i in range(0, n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % (sum)


print(series_sum1(4))

# Practice .format() function
x = 1.3555
y = float('{:.3f}'.format(x))
print(y)

x1 = 1.2345
y1 = 23.45678

print(f'x = {x1:.2f} and y = {y1:.3f}')
#x = 1.23 and y = 23.

import math

n = 3
p = math.pi
print('{0:.{1}f}'.format(p, n))
