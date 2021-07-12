letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3]
zeroes = [0] * 3
matrix = [[1, 0], [2, 3], [4, 5]]
iterating = list(range(5))
print("iterating ->", iterating)
words = list("words")
print("words ->", words)
combined = letters + numbers+zeroes+matrix+iterating+words
print(combined)
print("length of combined ->", len(combined))

# getting values
rangenums = list(range(20))

print("words[2] ->", words[2])
print("letters[1:3] ->", letters[1:3])
print("letters[:3] ->", letters[:3])
print("letters[::2] ->", letters[::2])
print("rangenums ->", rangenums)
print("rangenums[::2] ->", rangenums[::2])
print("rangenums[::3] ->", rangenums[::3])
print("rangenums[::2] ->", rangenums[::2])
print("rangenums[::-1] ->", rangenums[::-1])

#unpack
zero, one, two, *rest = rangenums
print(zero)
print(one)
print(two)
print(rest)

#enumerate
lets = ['a','b','c','b']

for i, l in enumerate(lets): #enumerate gets a tuple with index that can be unacked in a for loop
    print("index-",i,"letter:", l)

#find items

print("first index of b in lets is ->",lets.index("b"))
#lets.index("x") gives error
print("b apeears",lets.count("b"),"times")
print("x appears",lets.count("x"),"times")


