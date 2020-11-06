while True:
 y = input(' Text: ')
 for x in y:
     x = x * 2
     if x == '  ':
         x = x.replace("  ", " ")
     print(x, end="")
print (" ")