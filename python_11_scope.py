x = 50

def func(x):
    print('x:',x)
    x = 1000
    print('local x changed to:',x)
func(x)
print(x)