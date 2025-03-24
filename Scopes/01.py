username = 'sumit kumar'

def func():
    username = "chai"
    print(username)

print(username)
func()



# parsing, lexical scoping 


x = 99

# def func2(y):
#     z = x+y
#     return z
# result = func2(1)
# print(result)



def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()







# closure / factory function 

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual
f =  chaicoder(2)
g = chaicoder(3)

print(f)



# once again watch this topic of closure. 


