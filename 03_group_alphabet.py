cnt = 3

for i in range(cnt):
    word = input()
    for x in range(len(word)-1):
        if word[x] != word[x+1]:
            if word[x+1] in word[:x]: 
                cnt -= 1
                break
            
print(cnt)