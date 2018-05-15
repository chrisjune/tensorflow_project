# mylisthear=[1,2,3]
# print(mylist)

try:
    f = open('simple.txt','r')
    f.write("Test write to simple text!")
except IOError:
    print("Error: could not find file or read data!")
except:
    print("Error: Unknwoned")
else:
    print("Success!")
finally:
    f.close()
    print("I ALWYAS WORK NO MATTER WHAT!")


    