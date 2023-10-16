class Car : 
    
    def __init__(self, company, detail):
        self._company = company 
        self._detail = detail 
    
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._detail)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._detail)


if __name__ == "__main__":
    print("class")
    
    car_company_1 = "Ferrari"
    car_detail_1 = [{"color":"white", "horsepower":400, "price":800}]


    car_company_2 = "Bmw"
    car_detail_1 = [{"color":"black", "horsepower":300, "price":700}]


    car_company_2 = "Audi"
    car_detail_1 = [{"color":"brown", "horsepower":200, "price":300}]

    car_company_list = ["Ferrari", "bmw", "Audi"]
    car_detail_list = [{"color":"white", "horsepower":400, "price":800},
                       {"color":"black", "horsepower":300, "price":700},
                       {"color":"brown", "horsepower":200, "price":300}]
    
    del car_company_list[0]
    del car_detail_list[0]
    print(car_company_list)
    print(car_detail_list)

    car_dicts = [{"car_company": "Ferrai1", "car_detail": {"color":"white", "horsepower":400, "price":800}},
                 {"car_company": "Ferrai2", "car_detail": {"color":"black", "horsepower":400, "price":800}},
                 {"car_company": "Ferrai3", "car_detail": {"color":"brown", "horsepower":400, "price":800}},
                 ]

    car1 = Car("Audi", {"color":"brown", "horsepower":200, "price":300})
    car2 = Car("Bmw", {"color":"brown", "horsepower":200, "price":300})
    car3 = Car("Ferrari", {"color":"brown", "horsepower":200, "price":300})

    print(car1)
    print(car1.__dict__)
    print(dir(car1))
    car_list = list()
    car_list.append(car1)
    car_list.append(car2)
    car_list.append(car3)

    print(car_list)

    