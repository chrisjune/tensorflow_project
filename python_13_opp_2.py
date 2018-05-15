# class Animal():
#     def __init__(self):
#         print("Animal Created")
    
#     def who_am_i(self):
#         print("Animal")

#     def eat(self):
#         print("Eating")
    
# class Dog(Animal):

#     def __init__(self):
#         #Animal.__init__(self)
#         print("Dog Created")
#     def bark(self):
#         print("Woolf")
#     def eat(self):
#         print("Dog Eating")

# mydog = Dog()
# mydog.who_am_i()
# mydog.eat()
# mydog.bark()

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroied!")

b= Book("Python","jose",200)
del b