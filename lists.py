alist = ['bryce', 'bill', 'tom', 'don']


# changing a varible in a list
# alist[0] = 'not anymore'

# for loop through list
# for x in alist:
#     print(x)

# if, something exists in list
# if "bryce" in alist:
#     print('yes')


# find length of a list
# print(len(alist))


# access particular index of a list
# print(alist[0])


# add items to list
# alist.append('this in new')
# print(alist)


# alist.insert(2, 'this was inserted, this push everything after down')
# print(alist)

# remove something from a list
# alist.remove("bill")
# print(alist)


# remove last index if not specified out of a list, if index put in paramater you can choose which to pop
# alist.pop()
# print(alist)

# del deletes from list
# del alist[2]
# print(alist)

# empty out an array
# alist.clear()
# print(alist)


# copy list, allows you to manipulate the new list without touching the old list
# copiedlist = alist.copy()
# copiedlist.pop()
# print(copiedlist, alist)

# another way to copy list, allows you to manipulate the new list without
# newlist = list(alist)
# newlist.pop()
# print(newlist, alist)


# list() also can create completely new arrays, remember double parentetheses
newlist = list(('rad', 'tad', 'sad'))
print(newlist)
