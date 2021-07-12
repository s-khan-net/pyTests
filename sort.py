from collections import deque
items = [
    ("prod1", 10),
    ("prod2", 2),
    ("prod3", 5),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# lambda
# items.sort(key = lambda parameters:expression)
tuples = [
    ("prod1", 10),
    ("prod2", 2),
    ("prod3", 5),
]

tuples.sort(key=lambda x: x[1])
# ^the main tuple        #^single item can be called anything
print(tuples)

# map
tuples1 = [
    ("prod1", 10),
    ("prod2", 2),
    ("prod3", 5),
]
mapres = map(lambda x: x[1], tuples1)
print("mapres->", mapres)
listmapres = list(mapres)
print("listmapres->", listmapres)
sortedmapres = sorted(listmapres)
print("sortedmapres", sortedmapres)

# filter
tuples2 = [
    ("prod1", 10),
    ("prod2", 2),
    ("prod3", 12),
]

filres = filter(lambda x: x[1] >= 10, tuples2)
print("filres->", filres)
listfilres = list(filres)
print("listfilres ->", listfilres)

# List Comprehensions

products = [
    ("prod1", 10),
    ("prod2", 2),
    ("prod3", 12),
]
# result = [expression for item in items]
# expression -> the items in resultant list

mapresult = [item[1] for item in products] # note that this returns a list not a map object
# same as map(lambda item:item[1], products)
print("comprehension mapresult", mapresult)

# note that this returns a list not a filter object
filresult = [x for x in products if x[1] >= 10]
# same as filter(lambda item:item[1]>=10, products)
print("comprehension filresult", filresult)

#generator objects

mapresult = [item[1] for item in products]
print("list[] comprehension returns list type", type(mapresult))
mapresult = (item[1] for item in products)
print("tuple() comprehension returns generator type",type(mapresult))
#main diff in size
from sys import getsizeof
rangevals = [x for x in range(10000)]
print("size of list->", getsizeof(rangevals))
rangevals = (x for x in range(10000))
print("size of generator-->", getsizeof(rangevals))


# zip
l1 = [0, 2, 5]
l2 = [7, 98, 3]

print(zip(l1, l2))
print("zipping 3 lists using zip", list(zip('abc', l1, l2)))

# que
que = deque([])
que.append(1)
que.append(4)
que.append(3)
print("que", que)
que.popleft()
print("que after popleft", que)
for x in que.__iter__():  # __iter__ is a member of the dque class that converts dque to iterable, iter(que) can be used too
    print(x)

#tuples

point = (10,20,30,40,50,60)
print(point,"of type->", type(point))
print("point[1]",point[1]) #cannot point[1] = 10 will throw error as tuples are readonly
print("point[1:5]",point[1:5]) #after 1(10) before 5(60) > (20,30,40,50)
x = 10
y = 20
z= 30
x,y,z = z,y,x #swap these are actully tuples
print("x=",x,"y=",y,"z",z)