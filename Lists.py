if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        command = input().split()# The `split()` method is used to split a string into a list of substrings
        # based on a specified delimiter. In this code, `input().split()` is
        # splitting the user input into a list of strings, where each string
        # represents a command and its arguments.
        
        if command[0] == 'insert':
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(arr)
        elif command[0] == 'remove':
            arr.remove(int(command[1]))
        elif command[0] == 'append':
            arr.append(int(command[1]))
        elif command[0] == 'sort':
            arr.sort()
        elif command[0] == 'pop':
            arr.pop()
        elif command[0] == 'reverse':
            arr.reverse()
        else:
            pass
