#lists
mylist = ['a','b','c','d','e']
#mylist = ['string',1,2,3,3.2,True,'abcedf',[1,2,3]]
print(mylist)
mylist[0] = 'new item'
print(mylist)

mylist.append('f')
mylist.extend(['g','h','i'])
print(mylist)

item = mylist.pop(0)
print(mylist, item)

mylist.reverse()
print(mylist)

mylist=[1,2,['x','y','z']]
print(mylist[2][1])

#List comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([row[0] for row in matrix])

wordlist=['a','b','c','e','f']
seq_list = [n for n in wordlist]
print(seq_list)