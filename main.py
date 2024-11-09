from flask import Flask

app = Flask(__name__)

@app.route("/A1G/pure_function")
def calculate_power(a, b):
    return a ** b

@app.route("/A1G/procedual_function")
def add_ten(value):
    for i in range(0, 10):
        value += 1
    print(value)

@app.route("/A1F/immutable_value")
def immutable_value():
    our_tuple = ("a", "b", "c")
    new_tuple = our_tuple + ("d",)
    print(new_tuple)

@app.route("/A1F/referenced_object")
def referenced_object():
    our_list = ["a", "b", "c"]
    our_list.append("d")
    print(our_list)

@app.route("/A1E/object_oriented")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(circle.area())

@app.route("/B1G/algorithm")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route("/B1F/algorithm")
def add(a, b):
    return a + b

def fibonacci_2(n):
    if n <= 1:
        return n
    else:
        return add(fibonacci_2(n-1), fibonacci_2(n-2))

@app.route("/B1E/algorithm")
def fibonacci_3(n):
    def add(a, b):
        return a + b

    if n <= 1:
        return n
    else:
        return add(fibonacci_3(n-1), fibonacci_3(n-2))

@app.route("/B2G/greet")
def greet(name):
    return f"Hello, {name}!"

greeting_function = greet

print(greeting_function("Alice"))

@app.route("/B2F/higher_order_function")
def multiply(x, y):
    return x * y

def apply_function(func, a, b):
    return func(a, b)

result = apply_function(multiply, 5, 3)
print(result)

@app.route("/B2E/inner_outer_function")
def outer_function(outer_variable):
    def inner_function(inner_variable):
        return outer_variable + inner_variable
    return inner_function

closure_function = outer_function(10)
result = closure_function(5)
print(result)

@app.route("/B3G/lambda")
def lambda_example_one():
    square = lambda x: x ** 2
    print(square(5))

@app.route("/B3G/lambda_two")
def lambda_example_two():
    to_uppercase = lambda s: s.upper()
    print(to_uppercase("hello"))

@app.route("/B3F/lambda")
def lambda_example_three():
    add = lambda a, b: a + b
    print(add(3, 4))

@app.route("/B3E/lambda")
def lambda_example_four():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

@app.route("/B4G/map")
def map_example():
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(squared_numbers)

@app.route("/B4G/filter")
def filter_example():
    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

@app.route("/B4G/reduce")
def reduce_example():
    from functools import reduce

    numbers = [1, 2, 3, 4]
    sum_result = reduce(lambda x, y: x + y, numbers)
    print(sum_result)

@app.route("/B4F/combination")
def combination_example():
    from functools import reduce

    numbers = [1, 2, 3, 4, 5, 6]
    result = reduce(
        lambda x, y: x + y,
        map(
            lambda x: x ** 2,
            filter(lambda x: x % 2 == 0, numbers)
        )
    )
    print(result)


@app.route("/B4E/aggregation")
def aggregation_example():
    from functools import reduce

    products = [
        {"name": "Product A", "price": 30},
        {"name": "Product B", "price": 20},
        {"name": "Product C", "price": 50}
    ]
    total_price = reduce(
        lambda x, y: x + y,
        map(lambda p: p["price"], products)
    )
    print(total_price)

@app.route("/B4E/transformation")
def transformation_example():
    products = [
        {"name": "Product A", "price": 30},
        {"name": "Product B", "price": 20},
        {"name": "Product C", "price": 50}
    ]
    transformed_products = list(map(lambda p: {"name": p["name"], "cost": p["price"]}, products))
    print(transformed_products)

@app.route("/C1F/refactoring")
def refactoring_example():

    #original code
    def calc(x, y):
        return x * y - (x + y)

    #refactored code
    def calculate_profit(price, cost):
        return price * cost - (price + cost)

@app.route("/C1E/refactoring")
def refactoring_example_constant():

    #before refactoring
    def calculate_age(birth_year):
        current_year = 2024
        return current_year - birth_year

    #after refactoring
    CURRENT_YEAR = 2024

    def calculate_age_refactored(birth_year):
        return CURRENT_YEAR - birth_year


if __name__ == "__main__":
    app.run()
