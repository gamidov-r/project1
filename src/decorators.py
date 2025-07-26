from time import strftime


def log(filename=""):
    def print_log(func):
        def echo(msg):
            if filename:
                with open(filename, "a") as f:
                    f.write(f"{strftime('%d.%m.%y - %H:%M:%S')} -- {msg}" + "\n")
            else:
                print(f"{strftime('%d.%m.%y - %H:%M:%S')} -- {msg}")

        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                echo(f"{func.__name__} ok")
                return result
            except Exception as e:
                echo(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            # echo(f"{result}")

        return wrapper

    return print_log


# @log(filename="mylog.txt")
@log()
def my_function(x, y):
    return x + y


my_function(1, 2)
