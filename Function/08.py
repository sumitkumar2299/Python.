def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name = "shaktiman",power = "lazer")
print_kwargs(name = "shaktiman")
print_kwargs(name = "shaktiman", power= "lazer", enemy = "dr.jackal")