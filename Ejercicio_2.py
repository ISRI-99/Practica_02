class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make + ' '+self.model
        return long_name.title()
    def read_odometer(self):
        self.odometer= 0 
        print("This car has " + str(self.odometer) + " miles on it")
        
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
"""el error aparecia en el self odometer_reading porque no estaba definido con ese nombre dentro de la funcion"""
