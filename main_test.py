from switch_jamo_assemble import jamo_assemble
#import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리
from hangul_utils import join_jamos 
from jamo import j2h 
from jamo import j2hcj
import keyboard


import numpy as np           #numpy는 행렬,배열에 이용할 함수

import switch_button_input
import switch_button_revise
import switch_jamo_assemble



# LED = 23
Button_start = 's'  #시작 버튼, gpio 24
Button_revise = 'r'    #정정 버튼, gpio 17
Button_conso = 'c'     #자음 버튼, gpio 27
Button_vowel = 'v'     #모음 버튼, gpio 22
Button_num = 'n'       #숫자 버튼, gpio 23
Button_down = 'd'       #아래 버튼, gpio 25
Button_up = 'u'        #위 버튼, gpio 5
Button_input = 'i'     #입력 버튼, gpio 6
Button_back = 'b'      #뒤로/다시 버튼, gpio 13'
Button_next = 'x'      #다음/네 버튼, gpio 19
input_mode = 0        #mode  1: 자음 2: 모음 3: 숫자
num_size = 'z'          #방향키로 조절할 숫자의 최대

count_updown = 0

num_input = 0

chosung_index = ""       #문자열로 선언 해주어야 하나
jungsung_index = ""
jongsung_index = ""
sung_index_1 = []
sung_index_2 = []
sung_index_3 = []
sung_index_4 = []

chosung = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
jungsung = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
jongsung = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
#한글 유니코드 다 적어야 하나??
hangul = []

jamo_join_final_1 = ''
jamo_join_final_2 = ''
jamo_join_final_3 = ''
jamo_join_final_4 = ''

jamo_index = []
jamo_join_input = ''            #다음버튼 누르면 어딘가에 저장될 최종 문자
jamo_join_input_index = []      #글자가 완성되면 저장



#유니코드 중에서 초성 19개, 중성 21개, 종성 28개 ,,,, 다시 알아보기
syllables = np.array([chr(code) for code in range(44032, 55204)])
syllables = syllables.reshape(19, 21, 28)
        #ord(' ')를 넣으면 해당하는 글자값 출력




# GPIO.setmode(GPIO.BCM)      # GPIO BCM 모드 셋    #GPIO.setmode(GPIO.BOARD) board모드 셋

# GPIO.setup(LED, GPIO.OUT)   # LED 출력으로 설정

# #GPIO.setup(Button_start,Button_revise, GPIO.IN)이런식으로 되는지 확인해보자
# GPIO.setup(Button_start, GPIO.IN) # 버튼 입력으로 설정 GPIO.setup(Button_start, GPIO.IN, initial = 1)로 초기값 설정 가능
# GPIO.setup(Button_revise, GPIO.IN)
# GPIO.setup(Button_conso, GPIO.IN)
# GPIO.setup(Button_vowel, GPIO.IN)
# GPIO.setup(Button_num, GPIO.IN)
# GPIO.setup(Button_down, GPIO.IN)
# GPIO.setup(Button_up, GPIO.IN)
# GPIO.setup(Button_input, GPIO.IN)
# GPIO.setup(Button_back, GPIO.IN)
# GPIO.setup(Button_next, GPIO.IN)

print ('Start the GPIO App')  # 시작을 알리자!
print ("Press the button (CTRL-C to exit)")



#버튼이 눌릴때 설정
# GPIO.wait_for_edge(pin/port number, GPIO.FALLING, timeout=5000) #falling edge 감지, 스위치는 평상시 1, 눌렸을때 0 인데 1에서 0으로 값이 떨어지는(Falling) 경우가 스위치를 누른 동작에 해당
# GPIO.add_event_detect(Button_up, GPIO.RISING, callback=count_up, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300

# GPIO.add_event_detect(Button_start, GPIO.RISING, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300
# GPIO.add_event_detect(Button_revise, GPIO.RISING, bouncetime=300)
# GPIO.add_event_detect(Button_conso, GPIO.RISING, bouncetime=300)
# GPIO.add_event_detect(Button_vowel, GPIO.RISING, bouncetime=300)
# GPIO.add_event_detect(Button_num, GPIO.RISING, bouncetime=300)
# GPIO.add_event_detect(Button_down, GPIO.RISING, bouncetime=300)
# GPIO.add_event_detect(Button_up, GPIO.RISING, bouncetime=300)
# GPIO.add_event_detect(Button_input, GPIO.RISING, bouncetime=300)
# GPIO.add_event_detect(Button_back, GPIO.RISING, bouncetime=300)
# GPIO.add_event_detect(Button_next, GPIO.RISING, bouncetime=300)


print('input_mode : ',input_mode)
print('count_updown : ', count_updown)

try:
        while True:
                
                                
                # 버튼이 눌릴 때 실행할 것들
                if keyboard.read_key() ==Button_conso:
                        input_mode = 1
                        count_updown = 0
                        #자음이라는 말 출력
                        print('input_mode : ', input_mode)
                
                
                if keyboard.read_key() ==Button_vowel:
                        input_mode = 2
                        count_updown = 0
                        #모음이라는 말 출력
                        
                        print('input_mode : ', input_mode)
                
                
                if keyboard.read_key() ==Button_num:
                        input_mode = 3
                        count_updown = 0
                        #숫자라는 말 출력        
                        
                        print('input_mode : ', input_mode)

                
                                
                if keyboard.read_key() == Button_input:
                        
                        print('Button_input is pushed')
                        
                        #count_updown 숫자에 따라 자음 설정
                        if input_mode == 1 :
                                

                                sung = switch_button_input.push_Button_input_conso(count_updown) 
                                
                                sung_index_1.append(sung)                                          #설정된 자음 sung_index에 추가
                                sung_index_2.append(sung)
                                sung_index_3.append(sung)
                                sung_index_4.append(sung)
                                
                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                                jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_4)
                                
                                                                         
                                                                
                                #jamo-join_final 읽어주기       
                                               
                        
                        elif input_mode == 2 :
                                
                                sung = switch_button_input.push_Button_input_vowel(count_updown)
                                
                                sung_index_1.append(sung)
                                sung_index_2.append(sung)
                                sung_index_3.append(sung)
                                sung_index_4.append(sung)
                                
                                jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                jamo_join_fianl_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                                jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_4)
                                
                                
                                #jamo-join_final 읽어주기
                                
                                
                        else  :                                                 #숫자 input
                                num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                                #num_input 읽어주기

                
                        
                                              
                        #글자가 완성되면 jamo_join_input_index에 저장                                           #!!!!테스트가 필요하다!!!!
                        if jamo_join_final_1 != '' and jamo_join_final_2 != '' and jamo_join_final_3 != '' and jamo_join_final_4 != '' :
                        
                                if ord(jamo_join_final_4) >= 44032 and ord(jamo_join_final_4) <= 55203:
                                                                                
                                        jamo_join_input= jamo_join_final_4
                                        
                                        jamo_join_final_4 = ''
                                        jamo_join_final_3 = ''
                                        jamo_join_final_2 = ''
                                        jamo_join_final_1 = ''
                                        
                                        jamo_join_input = ''
                                        
                                elif ord(jamo_join_final_3) >= 44032 and ord(jamo_join_final_3) <= 55203:
                                        
                                        jamo_join_input= jamo_join_final_3
                                        
                                        jamo_join_final_3 = ''
                                        jamo_join_final_2 = ''
                                        jamo_join_final_1 = ''
                                        
                                        jamo_join_input = ''
                                        
                                elif ord(jamo_join_final_2) >= 44032 and ord(jamo_join_final_2) <= 55203:
                                        
                                        jamo_join_input= jamo_join_final_2
                                        
                                        jamo_join_final_2 = ''
                                        jamo_join_final_1 = ''
                                        
                                        jamo_join_input = ''
                                        
                                elif ord(jamo_join_final_1) >= 44032 and ord(jamo_join_final_1) <= 55203:                       #없어도 될듯???
                                        
                                        jamo_join_input= jamo_join_final_1
                                                                                
                                        jamo_join_final_1 = ''
                                        
                                        jamo_join_input = ''
                                                

                                else :
                                        continue                                                                                   #jamo_join_input에 들어갈 것 저장완료
                        
                        else :
                                pass
                        
                        
                        jamo_join_input_index.append(jamo_join_input)                                                   #jamo_join_input을 jamo_join_input_index에 저장

                        count_updown = 0
                        print('jamo_join_input : ',jamo_join_input)
                        print('num_input:',num_input)
                        print('count_updown: ',count_updown)
                        print('jamo_join_input_index:',jamo_join_input_index)
                        sleep(0.5)
                

                
                
                #button_up&down부분
                
                if keyboard.read_key() ==Button_up:
                        count_updown = count_updown + 1
                        
                        if input_mode == 1:
                                sung = switch_button_input.push_Button_input_conso(count_updown)
                                print('sung:',sung)
                                #sung 읽어주기
                           
                                
                        elif input_mode == 2:
                                sung = switch_button_input.push_Button_input_vowel(count_updown)
                                print('sung:',sung)
                                #sung 읽어주기
                                
                                
                        else :
                                print('count_updown:',count_updown)                                                               #아님 .수정해야됨!!!
                                #count_updown 읽어주기
                                
                                
                if keyboard.read_key() ==Button_down:                                                 
                        count_updown = count_updown - 1

                        if input_mode == 1:
                                sung = switch_button_input.push_Button_input_conso(count_updown)
                                print('sung:',sung)
                                #sung 읽어주기
                           
                                
                        elif input_mode == 2:
                                sung = switch_button_input.push_Button_input_vowel(count_updown)
                                print('sung:',sung)
                                #sung 읽어주기
                                
                                
                        else :
                                print('count_updown:',count_updown) 
                                                                   #!!!!수정해야됨!! 임시로 적어둔 것
                                #count_updown 읽어주기
                
                
                
                
                if keyboard.read_key() ==Button_revise:
                        
                        if input_mode == 1 or 2:
                                jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                                
                                
                        else :
                                num_input = switch_button_revise.push_Button_revise_num(num_input)

                
                
                
                
                
                
                
                
                # if GPIO.input(Button_start) == 0: #누를 때 button신호 0
                #         count_updown = 0
                        
                #         GPIO.add_event_detect(Button_up, GPIO.RISING, callback=count_up, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300
                #         GPIO.remove_event_detect(Button_up)
                        
                #         GPIO.add_event_detect(Button_down, GPIO.RISING, callback=count_down, bouncetime=300)
                #         GPIO.remove_event_detect(Button_down)
                        
                #         GPIO.add_event_detect(Button_input, GPIO.RISING, callback=count_input, bouncetime=300)
                #         GPIO.remove_event_detect(Button_input)
                        
                        
                #         GPIO.add_event_detect(Button_conso, GPIO.RISING, callback=push_Button_conso, bouncetime=300)
                #         input_mode = push_Button_conso()                        # input_mode값 1인지 확인
                #         input_mode = callback                                   # input_mode값 1인지 확인
                                
                #         GPIO.remove_event_detect(Button_conso)
                        
                        
                        

                         
                #         GPIO.output(LED, True)
                                                                              
                # else:
                #         GPIO.output(LED, False)
                #         print ("Button was Not Pressed!")
                        
                
                
                                
                sleep(0.1)
                
                


except KeyboardInterrupt:      # CTRL-C를 누르면 발생 
        # GPIO.cleanup()  #cleanup변수 뭔지 알아보기 
        print('finish')