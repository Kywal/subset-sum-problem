from approx_subset_sum import approx_subset_sum

n = int(input())

s = []

for i in range (0, n):
    num = int(input())
    s.append(num)

t = int(input())

print(approx_subset_sum(s,t,0.05))

