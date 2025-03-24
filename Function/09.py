# generator function with yield 
limit = 10
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
    
for num in even_generator(10):
    print(num)




# once again watch this whole concept 
