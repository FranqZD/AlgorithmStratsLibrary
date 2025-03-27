from time import perf_counter, sleep
from random import random

def timeit(n):  # Accept n as an argument
    def decorator(f):  # This is the actual decorator
        def wrapper(*args, **kwargs):
            exec_time = 0
            return_value = None #
            for i in range(n):
                start = perf_counter()
                return_value = f(
                    *args, **kwargs
                )  # Important to calculate the return value inside the loop
                end = perf_counter()
                exec_time += end - start
            print(
                f"@timeit Function {f.__name__}: Average execution time {exec_time / n} over {n} iterations."
            )
            return return_value
        return wrapper
    return decorator  # Return the decorator

if __name__ == "__main__":
    @timeit(10)
    def example_function():
        # Simular una tarea que toma tiempo
        sleep(5 * random())

    example_function()
