n = int(input())

#arr = map(int, input().split())
#Replace line
#list comprehension
arr = [int(input()) for i in range(n)]

#The sorted() function accepts a reverse parameter as an optional argument.
#Setting reverse = True sorts the iterable in the descending order.
arr=sorted(arr,reverse=True)

for i in range(len(arr)):
    if arr[i]==arr[0]:
        continue
    else:
        print(arr[i])  
        break
