nums = input().split()
N = int(nums[0])
K = int(nums[1])
h = 0
n = 1
while (n <= K) and (n < N):
    n *= 2
    h += 1
if n < N:
    h += ((N - n) // K + 1 if (((N - n) % K) != 0) else (N - n) // K)
print(h)







