def sum_two_smallest_numbers(numbers):
    ans =0
    ans += min(numbers)
    numbers.remove(min(numbers))
    ans += min(numbers)
    numbers.remove(min(numbers))
    return ans