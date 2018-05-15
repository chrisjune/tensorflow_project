def hello():
    return "hello"
print(hello())


def add_num(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, need Integers!"
result  = add_num(2,3)
print(result)


###Lambda Expression###

##Filter
mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2==0

evens=filter(even_bool, mylist)
print(evens)

lambda num:num%2==0
evens = filter(lambda num:num%2==0, mylist)
print(evens)

st="hello World! Programmer"
st.lower()
st.upper()
splitted=st.split(' ')
print(splitted)

print('x' in [1,2,3,'x'])
print([1,2,3,'x'].__contains__('x'))
 
def arrayCheck(nums):
    # CODE GOES HERE
    arr=set(nums)
    result=False
    if 1 in arr:
        if 2 in arr:
            if 3 in arr:
                result=True
    print(result)
arrayCheck([1,1,2,3,1])
arrayCheck([1,1,2,4,1])
arrayCheck([1,1,2,1,2,3,])

def stringBits(str):
    # CODE GOES HERE
    result=''
    for i in range(len(str)):
        if i%2==0:
            result=result+str[i]
    print(result)
stringBits('hi')



def end_other(a, b):
    # CODE GOES HERE
    print(b.upper() in a.upper() or a.upper() in b.upper()) 
end_other('hellAbc','abC')
end_other('aBC','heAbcllo')

def doubleChar(str):
    # CODE GOES HERE
    out=""
    for char in str:
        out=out+char+char
    print(out)

doubleChar('Hi-there')
doubleChar('Junyeong')



def count_evens(nums):
    # CODE GOES HERE
    count=0
    for num in nums:
        if num%2==0:
            count=count+1
    print(count)

count_evens([0,1,2,3,4,5])