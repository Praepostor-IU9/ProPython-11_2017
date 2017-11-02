def ignore_exceptions(exceptions):
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except exceptions:
                res = None
            return res

        return new_func

    return decorator


@ignore_exceptions(ZeroDivisionError)
def div(a, b):
    return a // b


print(div(5, 2))
print(div(5, 0))