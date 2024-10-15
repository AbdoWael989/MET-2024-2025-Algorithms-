##### selection-sort #####
def sel_sort(arr):
    n=len(arr)
    if n<=1:
        return
    for i in range(n):
        k = i
        for j in range(i+1,n):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
arr=[11,12,13,5,6]
sel_sort(arr)
print(arr)