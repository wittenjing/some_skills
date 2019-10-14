import random

class Person:
    def __init__(self, a, b):
        self.a = a 
        self.b = b

before = []

#def compare(p1, p2):
#    return p1.b > p2.b

for i in range(10):
    p = Person(i, random.randint(0, 100))
    before.append(p)

#before.sort(cmp = compare, reverse = True)
before.sort(cmp = None, key = lambda x : x.a, reverse = True)

for item in before:
    s = str(item.a) + ", " + str(item.b)
    print s

