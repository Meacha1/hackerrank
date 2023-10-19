if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # The `format()` function is used to format the output to have two decimal places.
    # The `student_marks[query_name]` is used to get the scores of the student whose name is `query_name`.

    print("{:.2f}".format(sum(student_marks[query_name])/3))