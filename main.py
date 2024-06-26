from typing import List
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and returns an even list.
    
    Args:
    int_list: A list of integers.
    
    Returns:
    A list of even integers.
    """
    even_numbers = []
    for num in int_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list.
    
    Args:
    even_int_list: A list of even integers.
    
    Returns:
    The sum of the squares of all even numbers in the list.
    """
    sum_of_squares_of_even = 0
    for num in even_int_list:
        sum_of_squares_of_even += num ** 2
    return sum_of_squares_of_even

# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main() 
