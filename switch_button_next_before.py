#-*-coding: utf-8-*-

#-*-coding: euc-kr-*-

# import switch_main
import main_test

def push_Button_next(num_input,join_jamo_input,join_jamo_input_index,count_updown):
    
    if join_jamo_input != '' or join_jamo_input_index != []:
        
        join_jamo_input_save = join_jamo_input
        join_jamo_input_index_save = join_jamo_input_index
        
        join_jamo_input = ''
        join_jamo_input_index = []
        
        count_updown = 0
        
    else :
        
        num_input_save = num_input
        
        num_input = 0
        
        count_updown = 0
        
        
    return join_jamo_input,join_jamo_input_index,join_jamo_input_save,join_jamo_input_index_save,num_input,num_input_save,count_updown
        
        
    
