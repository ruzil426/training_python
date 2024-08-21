def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results

def min_(x):
    min_number = min(x)
    return min_number

def max_(x):
    max_number = max(x)
    return max_number

def len_(x):
    len_list = len(x)
    return len_list

def sum_(x):
    sum_number = sum(x)
    return sum_number

def sorted_(x):
    sorted_numbers = sorted(x)
    return sorted_numbers

numbers = [6, 20, 15, 9]

print(apply_all_func(numbers, max_, min_))
print(apply_all_func(numbers, len_, sum_, sorted_))