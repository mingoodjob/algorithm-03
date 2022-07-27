cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input = 'ljes=njak'

for i in cro:
    input = input.replace(i, '0')

print(len(input))
