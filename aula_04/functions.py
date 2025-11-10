from typing import List

def order_list_numbers(numbers: List[int]) -> List[int]:
    '''Order a list of numbers in ascending order'''
    
    ordered_list: List = []
    ordered_list = sorted(numbers)
    return ordered_list

numbers: List = [1, 5, 3, 2, 4]
ordered_numbers: List = order_list_numbers(numbers=numbers)
print(F"Original list: {numbers}")
print(f"Ordered list: {ordered_numbers}")