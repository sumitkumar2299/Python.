# basic class and objects 

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

# inheritance 
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("tesla","model s","85kwh")
print(my_tesla.full_name())
print(my_tesla.brand)





# my_car = Car("toyota","corolla")
# print(my_car.brand);
# print(my_car.model)
# print(my_car.full_name());



# my_new_car = Car("tata","safari");
# print(my_new_car.brand)
# print(my_new_car.model)



