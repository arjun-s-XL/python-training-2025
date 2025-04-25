def my_decorator(func):
    def wrapper(name):
        print("Before function call.")
        func(name)
        print("After function call.")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
