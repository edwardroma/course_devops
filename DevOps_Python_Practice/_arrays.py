# LIST is: [...]
list1 = [1, 2]
print("This is list1: ", type(list1), list1)
for l1 in list1:
    print(l1)
# or LIST is: list((...))
list2 = list((3, 4))
print("this is list2: ", type(list2), list2)
for l2 in list2:
    print(l2)

# TUPLE is: (...)
tuple1 = (5, 6)
print("\nThis is tuple1: ", type(tuple1), tuple1)
for t in tuple1:
    print(t)

# or TUPLE is: tuple((...))
tuple2 = tuple((7, 8))
print("\nThis is tuple2: ", type(tuple2), tuple2)
for tt in tuple2:
    print(tt)


# SET is: {...}
set1 = {"q", "qq"}
print("\nThis is set1: ", type(set1), set1)
for s in set1:
    print(s)

# or SET set is: set((...))
set2 = ("w", "ww")
print("\nThis is set2: ", type(set2), set2)
for ss in set2:
    print(ss)

# DICTIONARY is: {...: ...}
dictionary1 = {"a": "1", "b": "2"}
print("\nThis is dictionary1: ", type(dictionary1), dictionary1)
for key1, value1 in dictionary1.items():
    print(key1, ":", value1)

# or DICTIONARY is: dict((...= ...))
dictionary2 = dict(a="saf", b="abcdefg")
print("\nThis is dictionary2: ", type(dictionary2), dictionary2)
for key2, value2 in dictionary2.items():
    print(key2, ":", value2)

# or DICTIONARY is: dict(zip([...,...],[...,...]))
dictionary3 = dict(zip(["x", "y"], ["1", "2"]))
print("\nThis is dictionary3: ", type(dictionary2), dictionary2)
for key3, value3 in dictionary3.items():
    print(key3, ":", value3)
