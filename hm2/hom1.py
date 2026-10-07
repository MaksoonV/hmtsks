max_num = int(input("Максимальне число: "))
n = 0


for i in range(1, max_num+1):
    if i % 2 == 0:
        n += i

print(n)