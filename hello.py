def addthis(x, y):
    import pdb

    pdb.set_trace()

    print(f"This is x: {x} and the x-type {type(x)}")
    print(f"This is y: {y} and the y-type is {type(y)}")

    try:
        result = x + y
    except TypeError:
        print("x and y inputs must be integers.")
        result = int(x) + int(y)

    print(f"This is the result: {result}")
    return result


# print(addthis("five",2))
