def greet():
    print("Yo dude Good morning")

greet()

def person(name, age):
    print(name," ", age)

person("dkanvcndlk", 38)

def sum(a,*b):
    
    for b in b:
        a+=b
    print(a)
sum(5,6,7,8,9)

def keyWordedArg(name, **details):
    print(name)
    print(details)
keyWordedArg('Rishabh', age=20, city='lucknow', mob=3914930392)

def fib(num, lst):
    a, b = 0, 1
    sum = 0
    lst.append(a)
    lst.append(b)
    while sum < num:
        sum = a + b
        if sum >= num:  # Add a condition to stop if the sum exceeds num
            break
        lst.append(sum)
        a, b = b, sum
    return lst

lst = []
ans = fib(100, lst)
print(ans)

f= lambda a,b : a+b
result= f(5,6)
print(result)

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()