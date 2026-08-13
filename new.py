print("Hello, Shalom!")
print("Welcome to Python 🚀")
print ("Let's start coding!")
print(12 + 5)
x = 10
print(x)
print(9 + 2 * 15)
num1 = 20
num2 = 5
print(num1 + num2)

def add():
    a = 30
    b = 10
    c = a + b
    print(c)

add()
add()

def fact(num):
    res = 1

    for i in range(1, num+1):
        res = res * i
    return res
result = fact(5)
print(result)