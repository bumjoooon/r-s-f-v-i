import switch_main



# input mode 에 따라 함수 다르게


def push_Button_revise_sung(jamo_join_final):
    
    size = len(jamo_join_final)                     # len 문자열 길이 설정
    jamo_join_final = jamo_join_final[:size - 1]
        
    return jamo_join_final
    
    
def push_Button_revise_num(input_num):
    
    size = len(input_num)                           
    input_num = input_num[:size - 1]
    
    return input_num