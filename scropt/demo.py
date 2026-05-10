def pattern11(n):    
    for i in range(n):
        if i%2 == 0:
            start = 1
        else:           
            start = 0
        for j in range(i+1):
            print(start,end="")
            start=1-start
        # print new line after each row        
        print()
def pattern12(n):    
    for i in range(1,n+1):
        #number
        for j in range(1,i+1):
            print(j,end="")
        #space
        for k in range(2*n-2*i):
            print(" ",end="")
        #number
        for j in range(i,0,-1):
            print(j,end="")        
        print()
def pattern13(n):
    k=1    
    for i in range(1,n+1):
        #number
        for j in range(1,i+1):
            print(k,end=" ")
            k+=1      
        print()
def pattern14(n):
    # k=1    
    for i in range(n):
        #number
        # k = 'A'
        for j in range(ord('A'), ord('A')+n-i):
            print(chr(j),end=" ")  
        print()
def pattern15(n):
# A
# BB
# CCC
# DDDD
# EEEEE
    
    k= ord('A')
    for i in range(n):
        for j in range(i+1):
            print(chr(k),end="") 
        k=k+1 
        print()
def pattern16(n):
#      A
#     ABA
#    ABCBA
#   ABCDCBA
#  ABCDEDCBA
    
    for i in range(n):
        #space
        ch = ord('A')
        # for j in range(n-i-1):
        print(' '*(n-i-1),end="")
        for k in range(2*i+1):
            print(chr(ch),end="")
            if k < i:
                ch+=1 
            else:
                ch-=1
            
        #space
        for l in range(n-i-1):
            print(' ',end="")
        print()
def pattern17(n):
#E
#DE
#CDE
#BCDE
#ABCDE
    for i in range(n):
        #space
        #ch = ord('E')
        #ch = ch - i
        #for k in range(i+1):
        for k in range(ord('E')-i,ord('E')+1):
            print(chr(k),end=" ")
            # ch+=1

        print()
def pattern18(n):
#E
#DE
#CDE
#BCDE
#ABCDE
    for i in range(n):
        #space
        #ch = ord('E')
        #ch = ch - i
        #for k in range(i+1):
        for k in range(ord('E')-i,ord('E')+1):
            print(chr(k),end=" ")
            # ch+=1

        print()


#pattern11(5)
pattern18(5)
import sys
def reverse_arr(n,arr,i):
    if i>= n/2:
        return arr
    else:
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        # print('reverse array arr:', arr)
        reverse_arr(n,arr,i+1)
def palindrome(sting):
    if len(sting) <= 1:
        return True
    else:
        if sting[0] == sting[-1]:
            return palindrome(sting[1:-1])
        else:
            return False
def selection_sort(n,arr,i):
    if i == n-1:
        print(arr)
        return arr
    else:
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print('selection sort array arr:', arr,i)
        return selection_sort(n,arr,i+1)
def bubble_sort(n,arr,i):
    if i>= n-1:
        return arr
    else:
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print('bubble sort array arr:', arr)
        bubble_sort(n,arr,i+1)
def insertion_sort(n,arr,i):
    if i>= n:
        return arr
    else:        
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        # print('insertion sort array arr:', arr)
        insertion_sort(n,arr,i+1)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    print('left half arr:', left_half)
    right_half = merge_sort(arr[mid:])
    print('right half arr:', right_half) 
    return merge(left_half, right_half)
def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            print('merged array arr:', merged)
            i += 1
        else:
            merged.append(right[j])
            print('merged array arr:', merged)
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    # print('enter value n :')
    # str = input('enter string:\n')
    # result = palindrome(str)
    # print(f"The string '{str}' is a palindrome: {result}")
    print('enter value of n :')
    n = int(input())
    arr = []
    for i in range(n):
        value = int(input())
        arr.append(value)
    print('original array arr:', arr)
    # insertion_sort(n,arr,0)
    ss=selection_sort(n,arr,0)
    print('sorted array arr:', ss)