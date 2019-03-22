# Python program to display the sum of an array using recursive functions
def sum_array(array):
    """
     Recursive function to return a sum of an array in ascending order

     Arg:
         array (int) is the list or array-type object that contains numerical values that needs to be summed up together

     Returns:
            int: the sum of all numerical values in the array

     Examples:
        >>> sum_array([1, 2, 3, 4, 5])
        1
        >> sum_array([8, 2, 5, 4, 7])
        1
        >> sum_array([3, 2, 7, 4, 2])
        2
        """
    sum = 0
    for i in array:
        sum += i
    return sum


    # Python program to display the Fibonacci sequence up to n-th term using recursive functions

def fibonacci(n):
    """
     Recursive function to return a Fibonacci sequence of an array in ascending order

     Arg:
         n (int) is the list or array-type object that contains numerical values that needs to be calculated

     Returns:
            int: nth term of fibonacci sequence,
             equal to sum of previous two terms

     Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
        """
    if n<0:
    # Input must be positive integer
        print("Input must be positive integer")
    # Return zero if input is zero
    elif n==1:
        return 0
    # Return 1 if input is 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


# Python program to display the factorial using recursive functions

def factorial(n):
    """
     Recursive function to return a factoral of an array in ascending order

     Arg:
         n (int) is the list or array-type object that contains numerical values that needs to be calculated

     Returns:
            int: nth term of a factoral sequence,
             equal to the product of an integer and all the integers below it

     Examples:
        >>> factoral(1)
        1
        >> factoral(2)
        1
        >> factoral(3)
        2
        """

# create a variable (such as "x") that stores the value of the n!.
    x = 1
# create a for loop that will iterate and calculate the factoral of a range of numbers starting at 1 until the nth plus 1 number is reached

    for i in range(1, n + 1):
        x *= i
# The last line of the function is return x, which exits the function and returns the value of the variable x
    return x



# Python program to display the reverse of an array using recursive functions

def reverse(word):
    """
     Recursive function to return the inverse of a string

     Arg:
         word can be any is a string

     Returns:
            String in reverse

     Examples:
        >>> reverse(car)
        1
        >> reverse(dog)
        1
        >> reverse(house)
        2
        """
    return word[::-1]
