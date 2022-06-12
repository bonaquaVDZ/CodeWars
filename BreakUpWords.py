# Complete the solution so that the function will break up camel casing, using a space between words.

"""
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

# Ex 1
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)

  
# Ex 2
def solution1(s):
  return ''.join(' ' + c if c.isupper() else c for c in s)

print(solution1("letUsAssumeThatYouAReCorrect"))

# Ex 3
def solution2(s):
    return ''.join(i if i.islower() else ' ' + i for i in s)


# Ex 4
def solution3(s):
  final_string = ""
  for i in range(len(s)):
    char = s[i]
    if char.isupper():
      final_string += " " + char
    else:
      final_string += char
  return final_string

print(solution3("newStringForTesting"))

sentence = 'Why?'
for i in range(len(sentence)):
  print(i)

      