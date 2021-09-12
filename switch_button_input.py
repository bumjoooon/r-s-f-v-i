#-*-coding: utf-8-*-

#-*-coding: euc-kr-*-


#import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리
from hangul_utils import join_jamos 
import numpy as np           #numpy는 행렬,배열에 이용할 함수

import switch_button_revise


#import switch_main

# #test
# input_mode = 1
# count_updown = 3


sung_index = []
num_index  = []


# #test
# num_input = 90
# count_updown = 4


chosung = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']      #19개
jungsung = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']     #21ㄴ개



#입력 버튼
def push_Button_input_conso(count_updown):                      #count_updown 받아와서 글자로 변환
        conso_index = chosung[count_updown]
        
        print(conso_index)
                #음성출력 코드 추가하기
        return conso_index
        
        
        
def push_Button_input_vowel(count_updown):
        vowel_index = jungsung[count_updown]
        
        
                #음성출력 코드 추가하기
        return vowel_index
        
        
def push_Button_input_num(num_input,count_updown):
        
        num_input = str(num_input) + str(count_updown)
        num_input = int(num_input)
        # print(num_input)
        
        return num_input
        
        



# #test
# num_input = push_Button_input_num(num_input,count_updown)
# print('num_input : ',num_input)

# num_input = push_Button_input_num(num_input,count_updown)
# print('num_input : ',num_input)

        
# num_input = switch_button_revise.push_Button_revise_num(num_input)
# print('num_input : ',num_input)


# num_input = switch_button_revise.push_Button_revise_num(num_input)
# print('num_input : ',num_input)
