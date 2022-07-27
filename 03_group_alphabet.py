n = 0
a = 'happy'
b = 'new'
c = 'year'

for i in range(len(a)):
    if i >= len(a):
        break
    if a[i] == b[i+1]:
        print(a[i])