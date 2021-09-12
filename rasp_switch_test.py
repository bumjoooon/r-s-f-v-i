from switch_jamo_assemble import jamo_assemble
import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리
from hangul_utils import join_jamos 
from jamo import j2h 
from jamo import j2hcj

GPIO.setmode(GPIO.BCM)


Button_start = 18   #시작 버튼, gpio 24
Button_revise = 11    #정정 버튼, gpio 17
Button_conso = 13     #자음 버튼, gpio 27
Button_vowel = 15     #모음 버튼, gpio 22
Button_num = 16       #숫자 버튼, gpio 23
Button_down = 22       #아래 버튼, gpio 25
Button_up = 29        #위 버튼, gpio 5
Button_input = 31     #입력 버튼, gpio 6
Button_back = 33      #뒤로/다시 버튼, gpio 13'
Button_next = 35      #다음/네 버튼, gpio 19
input_mode = 0        #mode  1: 자음 2: 모음 3: 숫자
num_size = 0          #방향키로 조절할 숫자의 최대


GPIO.setup(Button_start, GPIO.IN) # 버튼 입력으로 설정 GPIO.setup(Button_start, GPIO.IN, initial = 1)로 초기값 설정 가능
GPIO.setup(Button_revise, GPIO.IN)
GPIO.setup(Button_conso, GPIO.IN)
GPIO.setup(Button_vowel, GPIO.IN)
GPIO.setup(Button_num, GPIO.IN)
GPIO.setup(Button_down, GPIO.IN)
GPIO.setup(Button_up, GPIO.IN)
GPIO.setup(Button_input, GPIO.IN)
GPIO.setup(Button_back, GPIO.IN)
GPIO.setup(Button_next, GPIO.IN)



try:
        while True:
                
            if GPIO.event_detected(Button_start):
                print('Button_start')
                
            elif GPIO.event_detected(Button_revise):
                print('Button_re')
            elif GPIO.event_detected(Button_conso):
                print('Button_co')
            elif GPIO.event_detected(Button_vowel):
                print('Button_vo')
            elif GPIO.event_detected(Button_num):
                print('Button_nu')
            elif GPIO.event_detected(Button_down):
                print('Button_do')
            else :
                print('nothing')
                
except KeyboardInterrupt:
        pass

GPIO.cleanup()


# if GPIO.event_detected(Button_start):
#     print('Button_start')
    
# elif GPIO.event_detected(Button_revise):
#     print('Button_')
# elif GPIO.event_detected(Button_conso):
#     print('Button_')
# elif GPIO.event_detected(Button_vowel):
#     print('Button_')
# elif GPIO.event_detected(Button_num):
#     print('Button_')
# elif GPIO.event_detected(Button_down):
#     print('Button_')
# else :
#     print('nothing')
