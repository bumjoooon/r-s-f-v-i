#import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리
from hangul_utils import join_jamos 
import numpy as np           #numpy는 행렬,배열에 이용할 함수

#import switch_main


input_mode = 1
count_updown = 3
sung_index = []

######함수 실행 했을 때 글자에 저장 되는 거 한번 살펴보기!!!!!


chosung = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
jungsung = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']



#입력 버튼 눌렀을 때 input_mode에 따라서 
# 1 : push_Button_input_conso
# 2 : push_Button_input_vowel
# 3 : push_Button_input_num



def push_Button_input_conso(count_updown):                      #count_updown 받아와서 글자로 변환
        vowel_index = chosung[count_updown]
        
        print(vowel_index)
        return vowel_index
        
        
        
aa = push_Button_input_conso(count_updown)
sung_index.append(aa)        
print(aa)
                


def push_Button_input_vowel(count_updown):
        
        
        return
        
        
        
