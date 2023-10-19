def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        # The line `if string[i:].startswith(sub_string):` is checking if the substring starting from
        # index `i` in the `string` variable starts with the `sub_string` variable.
        # `string[i:]` is slicing the `string` variable starting from index `i` to the end of the
        # string. It returns a new string that contains all the characters from index `i` onwards.        
        if string[i:].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)