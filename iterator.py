"""
#iter(),next()
L=[1,2,3,4]
for i in L:
    iterable_list=iter(L)
    print(type(iterable_list))
    print(next(iterable_list))
    print(next(iterable_list))
#usr define iter()
#create an iterator that returns numbers, starting with 1,and each sequence
#will increase by one (returning 1, 2, 3, 4, 5 etc.)

class Numbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x
number_class=Numbers()
number_iter=iter(number_class)

print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))

class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        val = self.num
        if val <= 10:
            self.num+=1
            return val
    #raise StopIteration#exception handling

value = TopTen()
print(value)
print(type(value))
for i in value:
    print(i)
    

a = [0,5,10,15,20]
for i in a:
    if i % 2 == 0:
        print(str(i)+"is an even number")
    else:
        print(str(i)+"is an odd number")

#Strings are also iterable
mystr = "Benglore"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#iterate the values of tuple using for loop
fruit_tuple = ("apple","banana","cherry")

for fruit in fruit_tuple:
    print(fruit)

#Return an iterator from a tuple, and print each value
fruit_tuple = ("apple", "banana", "cherry")
fruit_it = iter(fruit_tuple)

print(next(fruit_it))
print(next(fruit_it))
print(next(fruit_it))


#stop after 20 iteration
class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a<= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

number_class = Numbers()
number_iter = iter(number_class)

for x in number_iter:
    print(x)

"""

