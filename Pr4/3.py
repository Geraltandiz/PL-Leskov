A = int(input())
B = int(input())

for i in range(B, A-1, -1):
    if i % 2 != 0:
        print(i)