N = int(input())
line = input().split()

count = 0
for element in line:
    if int(element) < 0:
        count += 1
print(count)