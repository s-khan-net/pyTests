dic = {'x': 1, 'y': 2, 'z':'vscode'}
print(dic)
print(dic['y']) 
#print(dix['a']) results in key error as a is not there
print(dic.get('a')) #gives none
print(dic.get('a','NA')) #gives default value of NA
for key in dic:
    print(key, dic[key])
print("dic.items() ->", dic.items(),"type ->", type(dic.items())) ## dic.items returns dict_items thats iterable tuples
for x in dic.items(): 
    print(x)
#those can be spread
for k, v in dic.items(): 
    print(k, v)


#Dictionary Comprehensions
generated_dict = {x:x * 2 for x in range(10)}
print("dictionary generated from a comprehension:", generated_dict)
#majik
generated_dict = {'x':x * 2 for x in range(10)}
print("dictionary when key is same:", generated_dict, "18 is the last item of the generated dictionary")
