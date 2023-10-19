# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ ==  '__main__':
    n = int(input())
    word_count = {}
    word_arr = []
    for _ in range(n):
        # `word = input().strip()` is reading a line of input from the user and assigning it to the
        # variable `word`. The `strip()` method is used to remove any leading or trailing whitespace
        # from the input.
        word = input().strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            word_arr.append(word)
    print(len(word_arr))
    print(' '.join([str(word_count[word]) for word in word_arr]))