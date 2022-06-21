n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
i = 0
total = 0
while i < len(arr):
    if total >= n:
        print(i)
        break
    else:
        total += arr[i]
        i += 1

if total >= n:
    print(i)
else:
    print(-1)