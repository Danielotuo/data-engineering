# This function takes two arguments and returns their sum. The second argument is optional and defaults to 0.
def sum_two(a, b=0):
    return a + b

# This function takes three arguments and returns their sum.


def sum_three(a, b, c):
    return a + b + c

# This function takes any number of arguments and returns their sum.


def sum_args(*args):
    s_args = 0
    for arg in args:
        s_args += arg
    return s_args

# This function takes any number of keyword arguments, prints each key-value pair, and concatenates the values into a single string.


def concatenate_strings(**kwargs):
    ans = ""
    for k, v in kwargs.items():
        print(f'key : {k}, value : {v}')
        ans += v
    return ans

# This function does nothing.


def cool_func():
    pass


# This block of code is executed when the script is run directly. It calls the functions defined above and prints the results.
if __name__ == '__main__':
    print(f'2 Sum : {sum_two(1)}')
    print(f'3 Sum : {sum_three(1, 2, 3)}')
    print(f'4 Sum : {sum_args(1, 2, 3, 4)}')
    print(f'5 Sum : {sum_args(1, 2, 3, 4, 5)}')
    print(concatenate_strings(one='python', two=' is ', three='fun'))
