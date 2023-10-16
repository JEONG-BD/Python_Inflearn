class Car : 
    """
    *******************
    Car    : Class 
    Author : Admin 
    Date   : 2023.10.17
    *******************
    """
    car_count = 0 

    def __init__(self, company, detail):
        self._company = company 
        self._detail = detail 
        Car.car_count += 1 

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._detail)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._detail)

    def __del__(self):
        Car.car_count -= 1 

    def detail_info(self):
        print("Current ID {}".format(id(self)))
        print("Car Detail ID {} {}".format(self._company, self._detail.get('price')))

if __name__ == "__main__":

    car1 = Car("Audi", {"color":"brown", "horsepower":200, "price":300})
    car2 = Car("Bmw", {"color":"black", "horsepower":300, "price":400})
    car3 = Car("Ferrari", {"color":"white", "horsepower":400, "price":500})

    print(id(car1))
    print(id(car2))
    print(id(car3))

    print(car1._company == car2._company)
    print(car1 is car2)

    print(dir(car1))
    print(dir(car2))
    print(car1.__dict__)
    print(car2.__dict__)
    print(car1.__doc__)

    car1.detail_info()
    print(car1.__class__)
    print(id(car1.__class__), id(car2.__class__), id(car3.__class__))
    print(car1.car_count)
    print(car1.car_count)
    print(Car.car_count)

    