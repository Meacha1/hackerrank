if __name__ == '__main__':
    from collections import deque
    n = int(input())
    d = deque()
    for _ in range(n):
        command = input().split() # The `split()` method in Python is used to split a string into a list of
        # substrings based on a specified delimiter. By default, the delimiter is a
        # space character.
        
        if command[0] == 'append':
            d.append(command[1])
        elif command[0] == 'appendleft':
            d.appendleft(command[1])
        elif command[0] == 'pop':
            d.pop()
        elif command[0] == 'popleft':
            d.popleft()
    # `print(' '.join(d))` is joining all the elements in the deque `d` into a single string, with
    # each element separated by a space. It then prints the resulting string.
    print(' '.join(d))