# Time Complexity = O(n * log(n))
# Space Complexity = O(n * log(n))




def merge_sort(arr):
    if len(arr) > 1:
        lA = arr[:len(arr)//2]
        rA = arr[len(arr)//2:]

        merge_sort(lA)
        merge_sort(rA)

        i,j,k = 0,0,0

        while i < len(lA) and j < len(rA):
            if int(lA[i]) < int(rA[j]):
                arr[k] = lA[i]
                i+=1
            else:
                arr[k] = rA[j]
                j+=1
            k+=1

        while i < len(lA):
            arr[k] = lA[i]
            i+=1
            k+=1

        while j < len(rA):
            arr[k] = rA[j]
            j+=1
            k+=1




arr = []

with open('1000.txt','r') as f:
    val = f.read()
arr = val.split(',')
arr.pop()

merge_sort(arr)

print(arr)
