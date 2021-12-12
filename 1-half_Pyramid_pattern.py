#no 1 half Pyramid pattern
n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()
print()

"""cara lain
for i in range(1, n+1):
    print("* "*i, end=' ')
    print()
"""