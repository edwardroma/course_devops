# while + if-continue

print("We are trying some STATEMENT at '2'")
print("(1) CONTINUE")
count = 0
while count <= 3:
    count += 1
    if count == 2:
        print("if - ", count)
        print("at '2', the IF is activated. "
              "Anything 'before' CONTINUE is executed.",
              "Anything 'after' CONTINUE is skipped to start a new cycle")
        continue
        print("after")
    print("while - ", count)

# while + if-break
print("(2) BREAK")
count = 0
while count <= 6:
    count += 1
    print("BREAK will kill the loop when it comes to '2'")
    if count == 2:
        print("if = ", count)
        print("BREAK is killing the while loop now")
        break
    print("while - ", count)

# try + except + else + finally
var1 = 1
try:
    a = 1/var1
    print(f"TRY is executed with now errors")
    print("but we should not do anything here")
except ZeroDivisionError:
    print("the error caught by EXCEPT")
else:
    print("instead we should do it inside ELSE block")
finally:
    print("finally is ALWAYS here")
