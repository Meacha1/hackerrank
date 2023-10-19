if __name__ == '__main__':
    s = input().strip()
    print(any([char.isalnum() for char in s]))
    # The `any` function in Python returns `True` if at least one element in the given iterable
    # is `True`, and `False` otherwise. In this code, `any([char.isalnum() for char in s])`
    # checks if any character in the input string `s` is alphanumeric (i.e., a letter or a
    # digit). If there is at least one alphanumeric character, it will return `True`, otherwise
    # `False`.