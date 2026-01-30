# because strings are immutable!

s = "cat"
# s[0] = "r"
s = "r" + s[1:]
print(s)

s1 = "bob"
s2 = "banana"
print(s1 < s2) # false because banana is smaller because of b then a which is smaller than b then o

s1 = "BOB"
s2 = "bob"
print(s1 > s2) # upper case letters are smaller than lower case

# in operator checks if a string is part of another
print("ana" in "banana") # true
print("Ana" in "banana") # false because of capital A
