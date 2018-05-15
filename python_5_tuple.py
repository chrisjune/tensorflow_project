#Boolean
#Tuples
t = (1,2,3)
print(t[0])
t = ['a',True,123]
print(t)
t[0]='New'

#Tuple is immutable 


#Set
x = set()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(0.1)
x.add(1)
print(x)
print(len(x))

converted = set([1,1,1,1,2,2,2,2,2,2,3,3])
print(converted)


## list
a=[1,2,3,4]
#자유자재 대체가능

## dictionary
a={"key1":"value1","key2":"value2"}
a["key1"]="changedValue"
a["key3"]="addValue3"

##Tuple
a=(1,2,3,4)
#변경, 추가, 삭제가 안됨

##Set
a=set(1,2,3,4,44,41,121,1,112,2,2,2,2)
#고유값만 들어가고
#순서는 일정하지 않음