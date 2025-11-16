from utils_log import log_decorator

@log_decorator
def sum(a, b):
    return a + b

sum(7,8)
sum(7, "8")
sum(6,9)
sum(8,3)