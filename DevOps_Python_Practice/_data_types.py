



x = input("gimmemore")
print("type is", type(x), ", bool is", bool(x))

if len(x) == 0:
    print("it is empty")
elif x:
    print("it is pure True")
elif x != False:
    print("it is None")

elif x != False:  # True
    print("it is bool(False)")
elif x == 0:  # True
    print("it is pure zero")
elif x == None:  # True
    print("it is pure None")

else:
    print("it is s.t.")

x = None
if x:
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")