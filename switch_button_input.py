#import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리
from hangul_utils import join_jamos 
import numpy as np           #numpy는 행렬,배열에 이용할 함수

#import switch_main

# #test
# input_mode = 1
# count_updown = 3


sung_index = []


chosung = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
jungsung = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']



#입력 버튼
def push_Button_input_conso(count_updown):                      #count_updown 받아와서 글자로 변환
        conso_index = chosung[count_updown]
        
        print(conso_index)
        return conso_index
        
        
        
def push_Button_input_vowel(count_updown):
        vowel_index = jungsung[count_updown]
        
        
        return vowel_index
        
        
        
