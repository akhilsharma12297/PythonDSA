

list = [ 1,2,3,4,5,6,7,8,9,10]


print(list[-1])


for items in list:
    print(items)
    
list.append(11)

# print(list)


for i in range(0, len(list)):
    print(list[i])
    
    
square = [ val + 1 for val in list]

print(square)

halfIdx =round( len(square) / 2)
print(halfIdx)

firstHalf = square[:halfIdx]

print(firstHalf)

print((10 in firstHalf))
