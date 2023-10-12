

def function1():
    print("Call function1!")

def function2(a, b):
    print("Call function2!")

def function3(x, y):
    print("Call function3!")

def function4(x, y):
    print("Call function4")
    return x + y 

def first_func_01(w):
    print('Hello', w)
    
def first_func_02(w1):
    value = "Hello " + str(w1)
    return value 

def func_mul_1(x):
    y1 = x * 10 
    y2 = x * 20 
    y3 = x * 30 
    return y1, y2, y3 

def func_tup_1(x):
    y1 = x * 10 
    y2 = x * 20 
    y3 = x * 30 
    return (y1, y2, y3) 

def func_list_1(x):
    y1 = x * 10 
    y2 = x * 20 
    y3 = x * 30 
    return [y1, y2, y3]

def func_dic_1(x):
    y1 = x * 10 
    y2 = x * 20 
    y3 = x * 30 
    return {"1":y1, "2":y2, "3":y3}

def arg_func(*args):
    print(type(args))
    for i, v in enumerate(args):
        print('Result {0}'.format(i), v)
    print("-------")

def kwarg_func(**kwargs):
    print(type(kwargs), kwargs)

    for k, v in kwargs.items():
        print("Result key : {0} value : {1}".format(k, v))

def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
    print(type(args_1), type(args_2), type(args), type(kwargs))

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("Inner Function")
    func_in_func(num+100)

def mul_func(x, y):
    print(x, y)
    return x * y

def final_func(x, y, func):
    print(x * y * func(100, 100))    

if __name__ == "__main__":
    # function 
    print(">>>>>>")
    function1()
    function2(1, 2)
    function3("a", "b")
    
    result = function4(1, 2)
    print(result)
    first_func_01('Good boy')

    x = first_func_02('Good boy')
    print(x)

    x, y, z = func_mul_1(10)
    print(x, y, z)

    total = func_tup_1(10)
    print(total, type(total))

    total = func_list_1(10)
    print(total, type(total))

    total = func_dic_1(10)
    print(total, type(total))

    arg_func("Lee", "Jeong")

    #kwarg_func({"name":"pythobn", "type":"interpreter"})
    kwarg_func(name="python", type="interpreter")

    example(10, 20, 30, "Lee", "Kim", age1=10, age2=20)
    nested_func(100)

    # lambda
    result_ = mul_func(10, 20)
    print(result_)

    lambda_mul = lambda x, y: x*y 
    print(f"lambda {lambda_mul(10, 20)}")

    final_func(10, 20, lambda_mul)