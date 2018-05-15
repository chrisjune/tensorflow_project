mystring = 'Hello World'
print(mystring[2:5])

myname = 'my name is junyeong choi'
my = myname[:2]
name = myname[3:7]
iis = myname[8:10]
sung = myname[11:19]
first = myname[-4:]
print(my,name,iis,sung,first)

print(mystring[::3])
x = mystring.capitalize()
print(x)
x= mystring.split('e')
print(x)

x = "Insert another string hear:{}".format("INSERT ME")
print(x)
x = "Item one :{} Item two:{}".format("dog","cat")
print(x)
x = "Item one :{x} Item two:{y}".format(x="dog",y="cat")
print(x)