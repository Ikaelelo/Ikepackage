def bubble_sort(items):
    """
     Iterative function to return a bubble sort of an array in ascending order

     Arg:
         items (array) is the list or array-type object that contains numerical values that needs to be sorted

     Returns:
            items: array sorted in ascending order

     Examples:
        >>> items = ([56,26,93,17,97,31,47,55,20])
        1
        >> items = ([4,26,93,57,77,31,14,55,20])
        1
        >> items = ([45,13,93,17,99,31,44,60,20])
        2
        """


    #Setting the range for comparison (first round: x, second round: x-1  and so on)
    for x in range(0,len(items) - 1):

        #Comparing within set range
        for y in range(0,len(items) - 1 -x):

            #swapping
            if items[y]>items[y+1]:
                items[y], items[y+1] = items [y+1], items[y]
    return items


def merge_sort(items):
    """
     Iterative function to return a merge sort of an array in ascending order

     Arg:
         items (array) is the list or array-type object that contains numerical values that needs to be sorted

     Returns:
            items: array sorted in ascending order

     Examples:
        >>> items = ([56,26,93,17,97,31,47,55,20])
        1
        >> items = ([4,26,93,57,77,31,14,55,20])
        1
        >> items = ([45,13,93,17,99,31,44,60,20])
        2
        """
    #Return if there is no list or array of items to sort
    if not items:
        return []


    lists = [[a] for a in items]
    while len(lists) > 1:
        lists = merge_lists(lists)
    return lists[0]

#Finding the mid of the array
def merge_lists(lists):
    result = []
    for i in range(0, len(lists) // 2):
        result.append(merge2(lists[i*2], lists[i*2 + 1]))
    if len(lists) % 2:
        result.append(lists[-1])
    return result

def merge2(xs, ys):
    i = 0
    j = 0
    result = []
    while i < len(xs) and j < len(ys):
        x = xs[i]
        y = ys[j]
        if x > y:
            result.append(y)
            j += 1
        else:
            result.append(x)
            i += 1
    result.extend(xs[i:])
    result.extend(ys[j:])
    return result


def quick_sort(items):
    """ quick_sort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not items:
        return []

    pivots = [x for x in items if x == items[0]]
    lesser = quick_sort([x for x in items if x < items[0]])
    greater = quick_sort([x for x in items if x > items[0]])

    return lesser + pivots + greater
