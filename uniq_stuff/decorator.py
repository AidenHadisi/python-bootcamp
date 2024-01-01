from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        v = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return v

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")
    
if __name__ == "__main__":
    say_whee()