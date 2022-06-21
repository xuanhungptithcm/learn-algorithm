n = int(input())
arr = list(map(int, input().split()))[:n]
max = 0
count = 0

frequency = [0] * 1001

for i in range(n):
    frequency[arr[i]] += 1

for i in range(1001):
    if frequency[i] != 0:
        count += 1
    if frequency[i] > max:
        max = frequency[i]

print(max, count)