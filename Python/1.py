import smtplib
import sys
import timeit
from timeit import default_timer as timer
from collections import Counter






# LISTS
list = [1, 2, 3]

if "apple" in list:
    print("yes")
else:
    print("no")

print(len(list))
list.append(4)
list.insert(0, "apple")

item = list.pop()
print(item)
print(list)

list.remove(1)
list.clear()
list.reverse()

list2 = [1] * 5
a = list[::2]
b = list[::-1]
c = [i*i for i in list]






# TUPLES
mytuple = tuple(["Tim", 20, "New York"])
print(mytuple)

item = tuple(3)
print(item)

my_tuple = ("a", "p", "p", "l", "e")
print(my_tuple.count("p"))
print(my_tuple.index("p"))
print(len(my_tuple))
print(my_tuple[::-1])

my_list = list(my_tuple)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
print(timeit.timeit(stmt="[0, 1, 2, 3]"), number=1000000)
print(timeit.timeit(stmt="[0, 1, 2, 3]"), number=1000000)






# DICTIONAIRIES
mydict = {"tim": "T", "kim": "K"}
mydict["email"] = "tim@gmail.com"
del mydict["email"]
mydict.pop("kim")
mydict.popitem()

for key in mydict:
    print(key)

for key, value in mydict.items():
    print(key, value)

mydict_copy = mydict
mydict_copy["email"] = "max@gmail.com"
# points to the same dictionairy in memory
print(mydict)
print(mydict_copy)

mydict_copy = mydict_copy()
mydict_copy = dict(mydict)
mydict_copy["email"] = "max123@gmail.com"
print(mydict)
print(mydict_copy)

my_dict_2 = dict(name="Mary", age=25, city="Boston")
mydict.update(my_dict_2)
print(mydict)

mytuple = (10, 10)
mydict = {mytuple: 15}
print(mydict)






# SETS
myset = set("hey")
print(myset)

myset.add(1)
myset.add(2)
myset.add(3)

myset.remove("hey")
myset.discard(3)
print(myset)

for x in myset:
    print(x)

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
i = evens.intersection(primes)
print(i)
d = odds.difference(primes)
d = evens.symmetric_difference(primes)
print(d)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setC = {7, 8}
setD = setC.copy()
setE = frozenset([1, 2, 3, 4]) #immutable

myset.update({1, 2, 3})
setB.intersection_update(setA)
setB.symmetric_intersection_update(setA)
setA.difference_update(setB)
setA.symmetric_difference_update(setB)

print(setA.issubset(setB)) #false
print(setB.issubset(setA)) #true
print(setA.issuperset(setB)) #true
print(setB.issuperset(setA)) #false

print(setA.isdisjoint(setB)) #false
print(setA.isdisjoint(setC)) #true






# STRINGS
mystring = 'I\'m a person'
mystring = "I'm a person"
mystring = """
    Hey now,
    you're okay!
"""

mystring = "Hello world"
char = mystring[-1]
print(char) #d
char = mystring[1:5]
print(char) #ello
substring = mystring[::2]
print(substring) #HloWrd
substring = mystring[::-1]
print(substring) #dlroW olleH
# strings are immutable so you cannot do "mystring[0] = 'c'"

greeting = "Hello"
for i in greeting:
    print(i)
#H
#e
#l
#l
#o

if 'p' in greeting:
    print("yes")
else:
    print("no")

mystring = "    Hey     "
string = "hey,there,dont,fret"

mystring = mystring.strip()
print(mystring) #hey
print(mystring.strip()) #    Hey     
print(mystring.upper())
print(mystring.lower())
print(mystring.startswith('H')) #true
print(mystring.startswith("Hello")) #true
print(mystring.startswith("World")) #false
print(mystring.count('l')) #2
print(mystring.replace("World", "Universe")) #Universe

mylist = string.split(",")
print(mylist) #['how', 'are', 'you', 'doing']
newstring = ''.join(mylist)
print(newstring) #howareyoudoing

start = timer()
my_list = ['a'] * 6
# bad code, because string are immutable and here you create a new string and reassign it back to the original string
start = timer()
my_string = ''
for i in my_list:
    my_string += 1
stop = timer()
print(stop - start)
print(my_string) #aaaaaa
# good code, because it is cleaner and faster
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)
print(my_string) #aaaaaa

a_string = 3
state = "the variable is %s" % a_string
an_integer = 3
state = "the variable is %d" % an_integer
a_float = 3.145435
another_float = 2.3242
state = "the variable is %f" % a_float
state = "the variable is {:.2f} and {}".format(a_float, another_float)
state = "the variable is %.2f" % a_float
state = "the variable is {a_float} and {another_float}"






# COLLECTIONS
















