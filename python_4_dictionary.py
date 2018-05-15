my_stuff = {"key1":"value1","key2":"value2","key3":{'123':[1,2,'grabMe']}}
print(my_stuff["key3"]['123'][2].capitalize())

my_stuff={"lunch":"pizza","bfast":"eggs"}
my_stuff['lunch']='burger'
my_stuff['dinner']='pasta'
print(my_stuff['lunch'])
print(my_stuff)