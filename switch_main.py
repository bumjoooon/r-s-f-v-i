from switch_jamo_assemble import jamo_assemble
import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리
from hangul_utils import join_jamos 
import numpy as np           #numpy는 행렬,배열에 이용할 함수

import switch_button_input



# LED = 23
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

chosung_index = ""       #문자열로 선언 해주어야 하나
jungsung_index = ""
jongsung_index = ""
sung_index = ""



chosung = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
jungsung = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
jongsung = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
#한글 유니코드 다 적어야 하나??
hangul = []
jamo_index = []


#유니코드 중에서 초성 19개, 중성 21개, 종성 28개 ,,,, 다시 알아보기
syllables = np.array([chr(code) for code in range(44032, 55204)])
syllables = syllables.reshape(19, 21, 28)
        #ord(' ')를 넣으면 해당하는 글자값 출력




GPIO.setmode(GPIO.BCM)      # GPIO BCM 모드 셋    #GPIO.setmode(GPIO.BOARD) board모드 셋

# GPIO.setup(LED, GPIO.OUT)   # LED 출력으로 설정

#GPIO.setup(Button_start,Button_revise, GPIO.IN)이런식으로 되는지 확인해보자
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

print ('Start the GPIO App')  # 시작을 알리자!
print ("Press the button (CTRL-C to exit)")



#버튼이 눌릴때 설정
# GPIO.wait_for_edge(pin/port number, GPIO.FALLING, timeout=5000) #falling edge 감지, 스위치는 평상시 1, 눌렸을때 0 인데 1에서 0으로 값이 떨어지는(Falling) 경우가 스위치를 누른 동작에 해당
# GPIO.add_event_detect(Button_up, GPIO.RISING, callback=count_up, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300

GPIO.add_event_detect(Button_start, GPIO.RISING, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300
GPIO.add_event_detect(Button_revise, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_conso, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_vowel, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_num, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_down, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_up, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_input, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_back, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(Button_next, GPIO.RISING, bouncetime=300)




try:
        while True:
                
                
                # 버튼이 눌릴 때 실행할 것들
                if GPIO.event_detected(Button_conso):
                        input_mode = 1
                        count_updown = 0
                        #자음이라는 말 출력
                if GPIO.event_detected(Button_vowel):
                        input_mode = 2
                        count_updown = 0
                        #모음이라는 말 출력
                if GPIO.event_detected(Button_num):
                        input_mode = 3
                        count_updown = 0
                        #숫자라는 말 출력        
                                
                
                                
                if GPIO.event_detected(Button_input):
                        if input_mode == 1 :
                                

                                sung = switch_button_input.push_Button_input_conso(count_updown) #count_updown 숫자에 따라 자음 설정
                                
                                sung_index.append(sung)                                          #설정된 자음 sung_index에 추가
                                
                                
                                jamo_join_final = jamo_assemble(sung_index)                      #sung_index에 저장된 글자 합치기 #이부분 불안함 자음모음 따로 들어오면 어카지..;;
                                #jamo-join_final 읽어주기       
                                
                                
                                
                        
                        
                        
                        elif input_mode == 2 :
                                
                                sung = switch_button_input.push_Button_input_vowel(count_updown)
                                sung_index.append(sung)
                                
                                jamo_join_final = jamo_assemble(sung_index)
                                #jamo-join_final 읽어주기

                        
                                
                                
                        else  :
                                
                                input_num = count_updown
                                #input_num 읽어주기
                                
                                              
                        
                        
                        count_updown = 0
                
                
                
                #button_up&down부분
                
                if GPIO.event_detected(Button_up):
                        count_updown = count_updown + 1
                        
                        if input_mode == 1:
                                sung = switch_button_input.push_Button_input_conso(count_updown)
                                #sung 읽어주기
                           
                                
                        elif input_mode == 2:
                                sung = switch_button_input.push_Button_input_vowel(count_updown)
                                #sung 읽어주기
                                
                                
                        else :
                                #count_updown 읽어주기
                                
                                
                if GPIO.event_detected(Button_down):                                                 # 왜틀렸징;;
                        count_updown = count_updown - 1

                        if input_mode == 1:
                                sung = switch_button_input.push_Button_input_conso(count_updown)
                                #sung 읽어주기
                           
                                
                        elif input_mode == 2:
                                sung = switch_button_input.push_Button_input_vowel(count_updown)
                                #sung 읽어주기
                                
                                
                        else :
                                #count_updown 읽어주기
                
                
                
                
                if GPIO.event_detected(Button_revise):
                
                
                
                
                
                
                
                
                
                if GPIO.input(Button_start) == 0: #누를 때 button신호 0
                        count_updown = 0
                        
                        GPIO.add_event_detect(Button_up, GPIO.RISING, callback=count_up, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300
                        GPIO.remove_event_detect(Button_up)
                        
                        GPIO.add_event_detect(Button_down, GPIO.RISING, callback=count_down, bouncetime=300)
                        GPIO.remove_event_detect(Button_down)
                        
                        GPIO.add_event_detect(Button_input, GPIO.RISING, callback=count_input, bouncetime=300)
                        GPIO.remove_event_detect(Button_input)
                        
                        
                        GPIO.add_event_detect(Button_conso, GPIO.RISING, callback=push_Button_conso, bouncetime=300)
                        input_mode = push_Button_conso()                        # input_mode값 1인지 확인
                        input_mode = callback                                   # input_mode값 1인지 확인
                                
                        GPIO.remove_event_detect(Button_conso)
                        
                        
                        

                         
                        GPIO.output(LED, True)
                                                                              
                else:
                        GPIO.output(LED, False)
                        print ("Button was Not Pressed!")
                        
                sleep(1)
                
                
                
except KeyboardInterrupt:      # CTRL-C를 누르면 발생 
        GPIO.cleanup()  #cleanup변수 뭔지 알아보기 
        
        