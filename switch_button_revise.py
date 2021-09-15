#-*-coding: utf-8-*-

#-*-coding: euc-kr-*-


import switch_jamo_assemble
from jamo import h2j, j2hcj
from hangul_utils import join_jamos



b = []

gyup = ''

# #test
# sung_index_1 = ['ㄱ','ㅘ','ㄱ']d

# #test        
# a = switch_jamo_assemble.jamo_assemble(sung_index_1)
# print(a)

# a = j2hcj(h2j(a))
# print(a)
# list2 = list(a)
# print(list2)
# list3 = list[:-1]
# print(list3)
# a = a[:-1]
# print(a)

#test
num_input = 302
jamo_join_input = '김범준'
# input mode 에 따라 함수 다르게


def push_Button_revise_sung(jamo_join_input):
    
    jamo_join_input = j2hcj(h2j(jamo_join_input))
    
    
    # list2 = list(jamo_join_input)
    # list3 = list[:-1]
    # jamo_join_input = jamo_join_input[:-1]
    
    
    size = len(jamo_join_input)                     # len 문자열 길이 설정
    jamo_join_input = jamo_join_input[:size - 1]
    jamo_join_input = join_jamos(jamo_join_input)
        
    return jamo_join_input
    
    
def push_Button_revise_num(num_input):
    
    
    a = []
    for i in str(num_input):
        a.append(i)
            
    if len(a) != 1 :    
        size = len(a)                           
        num_input = a[:size - 1]
    
        b = ''.join(num_input)
    
        num_input = int(b)
    
    elif len(a) == 1:
        num_input = 0
        
    else:
        pass
                
    return num_input




#test
print(num_input)
print(push_Button_revise_num(num_input))



print(jamo_join_input)
jamo_join_input = push_Button_revise_sung(jamo_join_input)
print(jamo_join_input)


print(push_Button_revise_sung(jamo_join_input))