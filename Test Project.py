l1 = [1,2,3,3,5,4,6,6,7,8,9,10,10]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)
