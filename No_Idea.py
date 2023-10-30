def happiness():
    # The line `n, m = map(int, input().split())` is taking input from the user and splitting it into
    # multiple values. It expects the user to input two integers separated by a space. The
    # `input().split()` function splits the input string into a list of strings using space as the
    # delimiter. The `map(int, ...)` function then converts each string in the list to an integer.
    # Finally, the values are assigned to the variables `n` and `m` using multiple assignment.
    n, m = map(int, input().split())
    main_arr = map(int, input().split())
    A = set(map(int, input().split()))  # set() to remove duplicates
    B = set(map(int, input().split()))
    happiness = 0
    for i in main_arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)
happiness()