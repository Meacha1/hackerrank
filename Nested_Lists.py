if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    # The line `arr.sort(key=lambda x: x[1])` is sorting the list `arr` based on the second element of
    # each sublist.
    arr.sort(key=lambda x: x[1]) # sort by score
    List_of_scores = list(set([x[1] for x in arr])) # get all unique scores
    # `sorted()` returns a sorted list. `sort()` sorts the list in place and returns `None`.
    List_of_scores.sort() # what is the difference between `sorted()` and `sort()`?
    # The line `filtered_list = list(set(List_of_scores))` is creating a new list called
    # `filtered_list` that contains only the unique elements from the `List_of_scores` list.
    second_lowest_score = List_of_scores[1]
    Student_names_with_second_lowest_score = []
    
    for name, score in arr:
        if score == second_lowest_score:
            Student_names_with_second_lowest_score.append(name)
    Student_names_with_second_lowest_score.sort(key=lambda x: x[0])
    print('\n'.join(Student_names_with_second_lowest_score))