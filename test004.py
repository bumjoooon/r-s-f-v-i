from jamo import j2h 
from jamo import j2hcj

from jamo import h2j, j2hcj


a = ord('ㄱ')
print(a)

a = ord('ㄲ')
print(a)

a = ord('ㄴ')
print(a)

a = ord('ㄷ')
print(a)

a = ord('ㄹ')
print(a)

a = chr(12593)
print(a)

a = ord('가')
print(a)

a = ord('각')
print(a)

a = ord('힣')
print(a)

a = ord('궁')
print(a)

# a = ord('궁ㄴ')
# print(a)

a = h2j('갅')
print(a)

a = j2hcj(h2j('간'))
print('a:',a)

b = ['ㄱ','ㅏ','ㄴ']
c = ''.join(b)
print('c:',c)

if a == c:
    print('a==c')
else:
    print('nope')
    pass


# a = len('궁ㄴ')
# print('len:',a)




# chosung = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
# jungsung = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
# jamo_index = []
# jamo_index_final = []

# vowel_index = chosung[0]

# print (vowel_index)

# jamo_index.append(vowel_index)


# vowel_index = chosung[2]

# print (vowel_index)

# jamo_index.append(vowel_index)



# print(jamo_index)


# size = len(jamo_index)                     # len 문자열 길이 설정
# print(size)
# print(jamo_index)
# print(size - 1)

# print(jamo_index[0:1])

# jamo_join_final = jamo_index[0:1]
# print(jamo_index_final)

# jamo_join_final = jamo_index[:1]
# print(jamo_index_final)

# jamo_join_final = jamo_index[:2]
# print(jamo_index_final)

# jamo_join_final = jamo_index[:size - 1]
# print(jamo_index_final)


# jamo_join_final = jamo_index[0:size -2]
# print(jamo_index_final)

# jamo_join_final.append(jamo_index[0:1])
# print(jamo_index_final)


a = 1
b = -1

# print(a/12)
# print(b/12)
# print(a%12)
print(b%12)


# if b < 0:
#     b = -b
#     print(b%12)
# else:
#     pass
