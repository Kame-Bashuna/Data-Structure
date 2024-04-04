#access item by use of index
tup=('home','school',2000)
print(tup[1])

#add item to tuple
add=tup+('hope',23)
print(add)

#remove item in tuple
tup=list(tup)
print(tup)
tup.remove('school')
print(tup)
tup=tuple(tup)
print(tup)
