lst = [1,2,3,4,5]
new =[]
for x in range(0,4):
    new.append(lst[x])
lst = lst[4:]
print(lst)
print(new)