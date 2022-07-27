alphapet = "Mississipi"
alphapet_list = [0] * 26
max_num = 0
max_index = 0

for i in alphapet:    
    if i.isalpha():
        index = ord(i) - ord('a')
        alphapet_list[index] += 1

for i in alphapet_list:
    if i > max_num:
        max_num = i
        max_index = alphapet_list.index(i)

print(chr(max_index + ord('a')))

    