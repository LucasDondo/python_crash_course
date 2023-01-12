# The confusing thing is that the first part is like always: for the first item
# we use 0 (the off-by-one rule).
# However, the second value is like the range() function, in which (1;10)
# displays 1-9.  So we need to add one.  But, at the same time we use the
# off-by-one rule, and in the end, to display until (and inclusive) the fourth
# item, we use (:4).

players=["Lucas", "Nico", "Bosco", "Mago", "Toto"]
print(players[2])
print(players)
print(players[:])
print(players[-2:])
print(players[:2])
print(players[2:4])