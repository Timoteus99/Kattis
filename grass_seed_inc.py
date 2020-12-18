cost = float(input())
lawns = int(input())
surf = 0
for element in range(lawns):
    lawn1, lawn2 = input().split()
    surf += float(lawn1) * float(lawn2)
print(surf * cost)