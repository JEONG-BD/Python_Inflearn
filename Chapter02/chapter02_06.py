from math import sqrt 
from collections import namedtuple

if __name__ == "__main__":
    point1 = (1.0, 5.0)
    point2 = (2.5, 1.5)

    len_1 = sqrt((point1[0] - point2[1]) ** 2 + (point1[1] - point2[1])**2 )
    print(len_1)

    #namedtuple
    Point = namedtuple('Point', 'x y')
    point3 = Point(1.0, 5.0)
    point4 = Point(2.5, 1.5)  
    print(point3)
    len_2 = sqrt((point3[0] - point4[1]) ** 2 + (point3[1] - point4[1])**2 )
    len_2 = sqrt((point3.x - point4.x) ** 2 + (point3.y - point4.y)**2 )
    
    print(len_2)

    Point2 = namedtuple('Point', ['x', 'y'])
    Point3 = namedtuple('Point', 'x, y')
    Point4 = namedtuple('Point', 'x y')
    Point5 = namedtuple('Point', 'x y x class', rename=True)

    #p2 = Point2(x=10, y=35)
    p3 = Point3(10, 35)
    p4 = Point4(45, y=20)
    p5 = Point5(10, 20, 30, 40)
    print(p5)

    # Dict to Unpacking
    temp_dict = {'x':75, 'y':35}
    p6 = Point3(**temp_dict)
    print(p6)
    print(p3[0] + p3[1])

    temp_list = [15, 25]
    p4 = Point4._make(temp_list)
    print(p4)
    print(p4._fields)
    x, y = p4 
    print(x, y)

    print(p3._asdict())

    Classes = namedtuple('Classes', ['rank', 'number'])
    numbers = [str(x) for x in range(1, 21)]
    ranks = 'A B C D'.split()
    print(numbers)
    print(ranks)
    students = [Classes(rank, number) for rank in ranks for number in numbers]
    print(len(students))
    print(students)

    students2 = [Classes(rank, number)
                for rank in 'A B C D'.split()
                    for number in range(1, 21)]
    print(students2)

    for s in students2:
        print(s)