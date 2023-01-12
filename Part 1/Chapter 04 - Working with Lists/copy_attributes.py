# This derives from foods.py, in which it is shown that when the value of a list
# is another list, then the value in the formers updates itself when the one of
# the latter does so, and vice versa.  However, in this file it is exposed that
# the same doesn't happen with variables.

var1 = 1
var2 = var1
print(var1)
print(var2)

var1 = 2
print(var1)
print(var2)
