##IF
 
if 1>2:
    print('hello')
elif 3==3:
    print('elif ran')
else:
    print('last')


##Loop
seq=[1,2,3,4,5,6]

for item in seq:
    print(item)
list = [i for i in seq]
print(list)


d = {"Sam":1, "Frank":2, "Dan":3}
for key in d:
    print(key)
    print(d[key])

#Tuple
mypairs = [(1,2),(3,4),(5,6)]
for t1,t2 in mypairs:
    print(t1)
    print(t2)

##Loop while
i=1
while i<5:
    print("i is: {}".format(i))
    i = i + 1

#for
a=[range(5)]
print(a)

for item in range(10):
    print(item)

x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print(out)

result = [ num**2 for num in x]
print(result)