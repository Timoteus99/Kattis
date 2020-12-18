fraza = input().split()

if len(fraza) != len(set(fraza)):
    print('no')
else:
    print('yes')