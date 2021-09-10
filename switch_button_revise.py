# import switch_jamo_assemble
from jamo import h2j, j2hcj
import math




# #test
# sung_index_1 = ['ㄱ','ㅘ','ㄱ']
# num  = 1524


# #test        
# a = switch_jamo_assemble.jamo_assemble(sung_index_1)
# print(a)

# a = j2hcj(h2j(a))
# print(a)
# a = a[:-1]
# print(a)

# input mode 에 따라 함수 다르게


def push_Button_revise_sung(jamo_join_input_index):                          # 글자 해체해서 마지막 글자 지우기 
    
    jamo_join_input = ''.join(jamo_join_input_index)
    
    jamo_join_input = j2hcj(h2j(jamo_join_input))
    jamo_join_input = jamo_join_input[:-1]
    
    return jamo_join_input
    
    
def push_Button_revise_num(num_input):                                  # num_input받아서 1의 자릿수 내림 
    
    num_input_revise = num_input / 10
    num_input_revise = math.floor(num_input_revise)
    num_input = num_input_revise
    
    return num_input


##글자지우기 test
# aa = push_Button_revise_sung(a)
# print(aa)



# #숫자 지우기 test
# bb = push_Button_revise_num(num)
# print(bb)

# bb = push_Button_revise_num(bb)
# print(bb)


# cc = num/10
# cc = math.floor(cc)
# num = cc * 10
# print(num)