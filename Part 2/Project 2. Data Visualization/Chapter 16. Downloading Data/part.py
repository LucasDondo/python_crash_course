import numpy as np


d = {'a': 1, 'b': 2, 'c': 3}
l = [9, 4, 4, 3, 3, 9, 0, 4, 6, 0]
print(*l)
a = np.array(l)
print(a)

ind = np.argpartition(a, -4)[:-4]
print(ind)

top4 = a[ind]
print(top4)

top_l = [l[i] for i in ind]
print(top_l)
print(len(top_l))




# Python 3 code to demonstrate
# removing duplicate elements from the list
l = [1, 2, 4, 2, 1, 4, 5]
print("Original List: ", l)
print(set(l))
print(type(set(l)))
print(*set(l))
res = [*set(l)]
print("List after removing duplicate elements: ", res)
