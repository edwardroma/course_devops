x = input("give me more")
print("type is", type(x), ", bool is", bool(x))

if x == False:
    print("it is bool(False)")
elif len(x) == 0:
    print("it is zero length")
elif x:
    print("it is pure True")
elif x == 0:  # True
    print("it is pure zero")
elif x == None:  # True
    print("it is pure None")
else:
    print("it is s.t.")

y = None
if y:
    print("Do you think None is True?")
elif y is False:
    print("Do you think None is False?")
else:
    print("None is not True, or False, None is just None...")
