class Car : 
    """
    *******************
    Car         : Class 
    Author      : Admin 
    Date        : 2023.10.17
    Description : Class, Static, Instance  
    *******************
    """
    price_per_raise = 1.0 

    # Instance method 
    def __init__(self, company, detail):
        self._company = company 
        self._detail = detail

    # Instance method 
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._detail)

    # Instance method 
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._detail)

    # Instance method 
    def __del__(self):
        pass 

    # Instance method 
    def detail_info(self):
        print("Current ID {}".format(id(self)))
        print("Car Detail ID {} {}".format(self._company, self._detail.get('price')))
    
    # Instance method 
    def get_price_before(self):
        return "Before Car price -> company {} price {}".format(self._company, self._detail.get('price'))
    
    # Instance method 
    def get_price_after(self):
        return "After Car price -> company {} price {}".format(self._company, self._detail.get('price')*Car.price_per_raise)
    
    # Class method 
    @classmethod 
    def raise_price(cls, per):
        
        if per <= 1:
            print("Please Enter 1 or more ")
            return 
        else :
            cls.price_per_raise = per 
            print("Succeed price increased")
    
    # Static method 
    @staticmethod
    def is_type(inst):
        if inst._company == "bmw":
            print()
            return 'Ok This car is {}'.format(inst._company)
        else:
            return 'Sorry This car is not bmw.\n this car is {}'.format(inst._company)

if __name__ == "__main__":

    car1 = Car("Audi", {"color":"brown", "horsepower":200, "price":300})
    car2 = Car("Bmw", {"color":"black", "horsepower":300, "price":400})
    car3 = Car("Ferrari", {"color":"white", "horsepower":400, "price":500})

    print(car1)
    print(car1.get_price_before())
    Car.price_per_raise = 4.0
    print(car1.get_price_after())
    print(car1.is_type(car1))