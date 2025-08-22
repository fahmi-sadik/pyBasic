freq = {}
str ="rrffffggg ff sdaa"

for i in range (len(str)):
    ch =str[i]

    if ch not in freq:
        freq[ch]=0

    freq[ch]+= 1


print(freq)