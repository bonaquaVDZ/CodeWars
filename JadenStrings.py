'''
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Examples:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

'''
# Ex 1
def toJadenCase(string):        
    return " ".join(x.capitalize() for x in string.split())

print(toJadenCase("How can mirrors be real if our eyes aren't real"))

# Ex 2
import string
def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)

# Ex 3
from string import capwords as toJadenCase


# Ex 4
toJadenCase = string.capwords


# -------------------------------------------------
# -------------------------------------------------
# Not fully adjustable code. Just for consideration. 
def to_jaden_case(string):
    collector = ""
    for i in string.split():
        collector += i.capitalize() + " "
    return collector

print(to_jaden_case("wow it is great"))


case = 'something is here. Are you ready?'

print(case.split())

def to_jaden_case1(string):
  return string.title()

print(to_jaden_case1("How can mirrors be real if our eyes aren't real"))

