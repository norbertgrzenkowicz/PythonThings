def binarysearch(arr, l, r, x):
    while(l<=r):
        mid= l + (r-l)//2
        if (arr[mid]==x):
            return mid
        elif (arr[mid] < x):
            l=mid +1
        else:
            r=mid-1
    return -l

num = [-232, -11, 0, 5, 190, 2210]
x= 5

res= binarysearch(num, 0, len(num)-1,x)

if (res!=-1):
    print(f'\n\nSzukana liczba jest w komorce num[{res}]')
else:
    print(f'\n\nNie znaleziono podanej liczby')
