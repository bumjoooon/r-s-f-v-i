# import switch_main
# import switch_input

#switch_input에서 넘어온 문자를 행렬에 넣어서 넘어온 것을 한 문자로 합치자
#겹받침이 나오면 하나로 합치자 join함수로 합치자
#sung에 한 글자
#sung_index에 글자들 저장

from hangul_utils import join_jamos             #행렬에 있는 글자들 합쳐준다!
import numpy as np
syllables = np.array([chr(code) for code in range(44032, 55204)])
syllables = syllables.reshape(19, 21, 28)
from jamo import h2j, j2hcj




gyup = ''                               #겹받침을 만들기 위해 새로운 문자열 변수


##test
# sung_index_1 = ['ㄱ','ㅘ','ㄱ']
# sung_index_2 = ['ㄱ','ㅣ','ㅁ']
# sung_index_3 = ['ㅁ','ㅏ','ㄹ','ㄱ']
# sung_index_4 = ['ㅇ','ㅏ','ㄴ','ㅎ']
# sung_index_5 = ['ㅅ','ㅔ']
# sung_index_6 = ['ㄱ']




def jamo_assemble(sung_index):
    
    jamo_join = ''.join(sung_index)
       
    
    if 'ㄱㅅ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄳ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄴㅈ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄵ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄴㅎ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄶ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄹㄱ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄺ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄹㅁ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄻ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄹㅂ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄼ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄹㅅ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄽ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄹㅌ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄾ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄹㅍ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㄿ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㄹㅎ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㅀ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    elif 'ㅂㅅ' in jamo_join:
        
        print(jamo_join)
        
        gyup = jamo_join[2:3]
        gyup = 'ㅄ'
        print(gyup)
        
        jamo_join = jamo_join[0:2]
        print(jamo_join)
        jamo_join_input = jamo_join + gyup
        print(jamo_join_input)
        
        jamo_join_input = join_jamos(jamo_join_input)
        
        return(jamo_join_input)
    
    else :
        jamo_join_input = join_jamos(jamo_join)
        
        return jamo_join_input
    
    






           
# # #test        
# a = jamo_assemble(sung_index_1)
# print(a)



# test = int(input('plz type numb : '))
# if test == 1:
#     sung_index_1.append('ㅅ')
#     aa = jamo_assemble(sung_index_1)
#     print(aa)

# else:
#     print('다시')

# #revise(수정)부분 test용
# aa = j2hcj(h2j(aa))   
# print(aa)
# list2 = list(a)
# print(list2)
# list3 = list[:-1]
# print(list3)'
# aa = aa[:-1]
# print(aa)
    




# b = jamo_assemble(sung_index_2)
# print(b)

# c = jamo_assemble(sung_index_3)
# print(c)

# d = jamo_assemble(sung_index_4)
# print(d)

# e = jamo_assemble(sung_index_5)
# print(e)

# f = jamo_assemble(sung_index_6)
# print(f)