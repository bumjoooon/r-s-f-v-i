#-*-coding: utf-8-*-

#-*-coding: euc-kr-*-


from switch_jamo_assemble import jamo_assemble
import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리
from hangul_utils import join_jamos 
import numpy as np           #numpy는 행렬,배열에 이용할 함수

import switch_button_input
import switch_button_revise
import switch_jamo_assemble



# LED = 23
Button_start = 24   #시작 버튼, 18
Button_revise = 17    #정정 버튼, 11
Button_conso = 27     #자음 버튼, 13
Button_vowel = 22     #모음 버튼, 15
Button_num = 23       #숫자 버튼, 16
Button_down = 25       #아래 버튼, 22
Button_up = 5       #위 버튼, 29
Button_input = 6     #입력 버튼, 31
Button_back = 13      #뒤로/다시 버튼, 33
Button_next = 19      #다음/네 버튼, 35

input_mode = 0        #mode  1: 자음 2: 모음 3: 숫자
# num_size = 2          #방향키로 조절할 숫자의 최대, 그때 그때 받아오기

count_updown = 0        #방향키로 조절할 때 조절될 숫자


num_input = 0           #입력 버튼 -  저장될 값
num_input_save = 0      #다음 버튼 - 저장될 값

chosung_index = ""       #문자열로 선언 해주어야 하나
jungsung_index = ""
jongsung_index = ""
sung_index_1 = []
sung_index_2 = []
sung_index_3 = []
sung_index_4 = []
sung_index = ""         #필요한가??  #겹받침 없을때에 문자 인덱스
sung_index_gyup = ""    #필요한가??  #겹받침 검사용 문자 인덱스


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
jamo_join_input = ''            #입력버튼 - 저장될 문자
jamo_join_input_index = []      #입력버튼 - 글자가 완성되면 저장
jamo_join_input_save = ''       #다음버튼 - 저장될 문자
jamo_join_input_index_save = [] #다음버튼 - 저장될 문자

jamo_join_input_save = ''
jamo_join_input_index_save = []
jamo_join_input_index_save_index = []

adress_input = []



#유니코드 중에서 초성 19개, 중성 21개, 종성 28개 ,,,, 다시 알아보기
syllables = np.array([chr(code) for code in range(44032, 55204)])
syllables = syllables.reshape(19, 21, 28)
        #ord(' ')를 넣으면 해당하는 글자값 출력




GPIO.setmode(GPIO.BCM)      # GPIO BCM 모드 셋    #GPIO.setmode(GPIO.BOARD) board모드 셋

# GPIO.setup(LED, GPIO.OUT)   # LED 출력으로 설정

#GPIO.setup(Button_start,Button_revise, GPIO.IN)이런식으로 되는지 확인해보자
#GPIO.setup(핀번호,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) 이렇게 해야되나?? 확인해보자
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


print('input_mode : ',input_mode)
print('count_updown : ', count_updown)


try:
        while True:
                
                
                if GPIO.event_detected(Button_conso):
                        input_mode = 1
                        count_updown = 0
                        print('input_mode : ', input_mode)
                        #자음이라는 말 출력
                if GPIO.event_detected(Button_vowel):
                        input_mode = 2
                        count_updown = 0
                        print('input_mode : ', input_mode)
                        #모음이라는 말 출력
                if GPIO.event_detected(Button_num):
                        input_mode = 3
                        count_updown = 0
                        print('input_mode : ', input_mode)
                        #숫자라는 말 출력        
                                
                
                                
                if GPIO.event_detected(Button_input):
                        
                        print('Button_input is pushed')
                        
                        if input_mode == 1 :
                                

                                sung = switch_button_input.push_Button_input_conso(count_updown) #count_updown 숫자에 따라 자음 설정
                                
                                sung_index_1.append(sung)                                          #설정된 자음 sung_index에 추가
                                sung_index_2.append(sung)
                                sung_index_3.append(sung)
                                sung_index_4.append(sung)                                          #설정된 자음 sung_index에 추가
                                                                
                                
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

                                                     
                                
                        else  :                 #자음,모음 아니면 무조건 숫자로 받게
                                num_input = switch_button_input.push_Button_input_num(num_input,count_updown)                   #num_input이 처음엔 빈 공백으로 있으면 어떻게 되는가???
                                #num_input 읽어주기
                        
                                
                        
                        if len(sung_index_1) == 4:    
                                if sung_index_1[3] in jungsung:
                                        
                                        sung_index_1 = sung_index_1[:2]
                                        jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                        jamo_join_input_index = jamo_join_input_index[:-1]
                                        jamo_join_input_index.append(jamo_join_final_1)
                                        
                                        
                                        sung_index_1 = sung_index_2[2:]
                                        sung_index_2 = sung_index_2[2:]
                                        sung_index_3 = sung_index_2[2:]
                                        sung_index_4 = sung_index_2[2:]
                                        jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                        jamo_join_input_index.append(jamo_join_final_2)
                                        
                                
                                                        
                                        
                                else:
                                        jamo_join_input_index = jamo_join_input_index[:-1]
                                        jamo_join_input_index.append(jamo_join_final_1)
                                        
                        elif len(sung_index_1) == 5:               
                                if sung_index_1[4] in jungsung:
                                        
                                        sung_index_2 = sung_index_2[:3]
                                        jamo_join_final_2 = switch_jamo_assemble.jamo_assemble(sung_index_2)
                                        print('jjjjamo_join_final_2',jamo_join_final_2)
                                        jamo_join_input_index = jamo_join_input_index[:-1]
                                        jamo_join_input_index.append(jamo_join_final_2)
                                        sung_index_1 = sung_index_3[3:]
                                        sung_index_2 = sung_index_3[3:]
                                        sung_index_3 = sung_index_3[3:]
                                        sung_index_4 = sung_index_3[3:]
                                        jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                        jamo_join_input_index.append(jamo_join_final_1)
                                
                                elif sung_index_1[4] in chosung:
                                        
                                        sung_index_1 = sung_index_1[:4]
                                        jamo_join_final_4 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                        print('jjjjamo_join_final_4',jamo_join_final_4)
                                        jamo_join_input_index = jamo_join_input_index[:-1]
                                        jamo_join_input_index.append(jamo_join_final_4)
                                        sung_index_1 = sung_index_3[4:]
                                        sung_index_2 = sung_index_3[4:]
                                        sung_index_3 = sung_index_3[4:]
                                        sung_index_4 = sung_index_3[4:]
                                        jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                        jamo_join_input_index.append(jamo_join_final_1)
                                        
                                
                                else:
                                        jamo_join_input_index = jamo_join_input_index[:-1]
                                        jamo_join_input_index.append(jamo_join_final_1)
                        
                        elif  len(sung_index_2)==6:      
                                if sung_index_2[5] in jungsung:
                                        
                                        sung_index_3 = sung_index_3[:3]
                                        jamo_join_final_3 = switch_jamo_assemble.jamo_assemble(sung_index_3)
                                        print('jamo_join_final_3:',jamo_join_final_3)
                                        jamo_join_input_index = jamo_join_input_index[:-1]
                                        jamo_join_input_index.append(jamo_join_final_1)
                                        sung_index_1 = sung_index_2[4:]
                                        sung_index_2 = sung_index_2[4:]
                                        sung_index_3 = sung_index_2[4:]
                                        sung_index_4 = sung_index_2[4:]
                                        jamo_join_final_1 = switch_jamo_assemble.jamo_assemble(sung_index_1)
                                        jamo_join_input_index.append(jamo_join_final_1)
                                else :
                                        jamo_join_input_index = jamo_join_input_index[:-1]
                                        jamo_join_input_index.append(jamo_join_final_1)
                                       
                                        
                        else : 
                                if len(sung_index_1) == 1:
                                        jamo_join_input_index.append(jamo_join_final_1)
                                else:
                                        jamo_join_input_index = jamo_join_input_index[:-1]
                                        jamo_join_input_index.append(jamo_join_final_1)
                        
                                    
                                        
                                              
                        print('jamo_join_input:',jamo_join_input)
                                                                                             #jamo_join_input을 jamo_join_input_index에 저장
                        print('jamo_join_input_index : ',jamo_join_input_index)
                        jamo_join_input = ''
                        
                        count_updown = 0
                        
                        print('jamo_join_input : ',jamo_join_input)
                        print('num_input:',num_input)
                        print('count_updown: ',count_updown)
                        print('jamo_join_input_index:',jamo_join_input_index)
                        sleep(0.5)
                
                else:
                        pass
                
                
                #button_up&down부분
                
                if GPIO.event_detected(Button_up):
                        count_updown = count_updown + 1
                        
                        if input_mode == 1:
                                count_updown = count_updown % 19 
                                sung = switch_button_input.push_Button_input_conso(count_updown)
                                print('sung:',sung)
                                #sung 읽어주기
                           
                                
                        elif input_mode == 2:
                                count_updown = count_updown % 21
                                sung = switch_button_input.push_Button_input_vowel(count_updown)
                                print('sung:',sung)
                                #sung 읽어주기
                                
                                
                        else :
                                count_updown = count_updown % num_size                                                          #num_size가 최대값
                                print('count_updown:',count_updown)
                                                                        #!!!!수정해야됨 임시로 적어둔 것
                                #count_updown 읽어주기
                                
                                
                if GPIO.event_detected(Button_down):                                                 # 왜틀렸징;;
                        count_updown = count_updown - 1

                        if input_mode == 1:
                                count_updown = count_updown % 19 
                                sung = switch_button_input.push_Button_input_conso(count_updown)
                                print('sung:',sung)
                                #sung 읽어주기
                                
                           
                                
                        elif input_mode == 2:
                                count_updown = count_updown % 21
                                sung = switch_button_input.push_Button_input_vowel(count_updown)
                                print('sung:',sung)
                                #sung 읽어주기
                                
                                
                        else :
                                count_updown = count_updown % num_size  
                                print('count_updown:',count_updown)     #!!!!수정해야됨!! 임시로 적어둔 것
                                #count_updown 읽어주기
                                
                
                
                
                
                if GPIO.event_detected(Button_revise):
                        if jamo_join_input_index != []:
                                jamo_join_input = switch_button_revise.push_Button_revise_sung(jamo_join_input_index)
                                print(jamo_join_input)
                                
                                
                                
                        elif  num_input != 0:
                                num_input = switch_button_revise.push_Button_revise_num(num_input)
                                print(num_input)
                                
                        else :
                                pass
                                
                                
                
                
                if GPIO.event_detected(Button_next):
                        
                        #step 올리기!!   
                        
                        if jamo_join_input != '' or jamo_join_input_index != []:
                                jamo_join_input_save = jamo_join_input
                                
                                jamo_join_input_index_save = jamo_join_input_index
                                jamo_join_input_index_save_index = jamo_join_input_index
                                jamo_join_input_index_save = ''.join(jamo_join_input_index)
                                
                                jamo_join_input = ''
                                jamo_join_input_index = []
                                
                                count_updown = 0

                        else :
                                num_input_save = num_input
        
                                num_input = 0
                                
                                count_updown = 0
                
                        print('jamo_join_input : ',jamo_join_input)
                        print('jamo_join_input_index : ',jamo_join_input_index)
                        print('jamo_join_input_save',jamo_join_input_save)
                        print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                        
                        print('num_input : ',num_input)
                        print('num_input_save : ', num_input_save)
                
                
                
                if GPIO.event_detected(Button_back):
                        #step 내리기!!
                        
                        if jamo_join_input_save != '' or jamo_join_input_index_save != []:
                                jamo_join_input_index = jamo_join_input_index_save_index
                                print(''.join(jamo_join_input_index_save))
                                #jamo_join_input_index_save 읽어주기?? 내용 어떻게 할지 생각
                                
                                count_updown = 0

                        else :
                                print(num_input_save)
                                #num_input_save 읽어주기?? 내용 어떻게 할지 생각해보자
        
                                num_input = num_input_save
                                
                                count_updown = 0
                                
                        print('jamo_join_input 5 : ',jamo_join_input)
                        print('jamo_join_input_index : ',jamo_join_input_index)
                        print('jamo_join_input_save',jamo_join_input_save)
                        print('jamo_join_input_index_save : ',jamo_join_input_index_save)
                        
                        print('num_input : ',num_input)
                        print('num_input_save : ', num_input_save)
                
                                        
                sleep(0.1)                                                                                                                #!!슬립시간 조절!!
                
                
                
except KeyboardInterrupt:      # CTRL-C를 누르면 발생 
        print('finish')
        GPIO.cleanup()   
        quit()
        