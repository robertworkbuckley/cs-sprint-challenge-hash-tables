def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    length = len(arrays)
    numbers = {}
    for array in arrays:
        for num in array:
            if num not in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1

    samezies = []
    for item in list(numbers.items()):
        if item[1] == length:
            samezies.append(item[0])
            
    return samezies


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
