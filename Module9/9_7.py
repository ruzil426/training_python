def is_prime(func):
    def wrapper(*args):
        value = func(*args)
        count = 0
        for i in range(1, value + 1):
            if value % i == 0:
                count += 1
        print('Простое число') if count == 2 else print('Составное число')
    return wrapper

@is_prime
def sum_three(*numb):
    sum_ = 0
    for i in numb:
        sum_ += i
    return sum_

result = sum_three(2, 3, 6)
print(result)
