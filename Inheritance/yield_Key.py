def fun_generator():
    yield "CP1890 Class is great"
    yield "maybe it the instructor?"
    yield "maybe it the students?"


obj = fun_generator()

print(type(obj))

print(next(obj))

print(next(obj))

print(next(obj))

test_list = [1, 4, 5, 6, 7]


def print_even(some_list):
    for num in some_list:
        if num % 2 == 0:
            yield num


print("the even numbers in the list: ", end=' ')
for k in print_even(test_list):
    print(k, end=' ')
