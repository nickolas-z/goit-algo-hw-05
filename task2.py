def binary_search_with_upper_bound(arr, target):
    """
    Function for binary search of an element in a sorted array with fractional numbers.
    
    Parameters:
    arr (list): Sorted array for searching.
    target: Element we are searching for.

    Returns:
    tuple: A tuple where:
           - the first element is the number of iterations to find the element,
           - the second element is the upper bound (the smallest element greater than or equal to the target).
    """
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None  # Variable for the upper bound

    while left <= right:
        iterations += 1
        mid = (left + right) // 2  # Middle of the array

        if arr[mid] == target:
            # Return the number of iterations and the found element (upper bound equals target)
            return (iterations, arr[mid])  
        
        elif arr[mid] < target:
            left = mid + 1  # If the target element is greater, shift the left boundary
        else:
            upper_bound = arr[mid]  # Update the upper bound
            right = mid - 1  # If the target element is smaller, shift the right boundary

    # If the element is not found, return the number of iterations and the upper bound
    return (iterations, upper_bound)

# Example usage
array = [2.1, 5.5, 8.8, 12.3, 16.7, 23.4, 38.9, 56.0, 72.2, 91.3]
target = 17.0
result = binary_search_with_upper_bound(array, target)

print(f"Number of iterations: {result[0]}, Upper bound: {result[1]}")