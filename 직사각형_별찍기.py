a, b = map(int, input().strip().split(' '))
s = ''
for _ in range(b):
    s += f'{"*"*a}\n'
print(s)