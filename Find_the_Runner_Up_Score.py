if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(set(arr))
    sorted_arr = sorted(arr1)
    print (sorted_arr[len(arr1) - 2])