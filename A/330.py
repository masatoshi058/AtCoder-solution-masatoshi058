n, l = map(int, input().split())
lis = map(int, input().split())

a = list(lis)

count = 0
for score in a:
    if score >= l:
      count += 1

print(count)