import RPi.GPIO as GPIO      # gpio 라이브러리
from time import sleep       # sleep 라이브러리

LED = 23
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

conso = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
vowel = ['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ']


GPIO.setmode(GPIO.BCM)      # GPIO BCM 모드 셋    #GPIO.setmode(GPIO.BOARD) board모드 셋

GPIO.setup(LED, GPIO.OUT)   # LED 출력으로 설정

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

GPIO.wait_for_edge(pin/port number, GPIO.FALLING, timeout=5000) #falling edge 감지, 스위치는 평상시 1, 눌렸을때 0 인데 1에서 0으로 값이 떨어지는(Falling) 경우가 스위치를 누른 동작에 해당

print ('Start the GPIO App')  # 시작을 알리자!
print ("Press the button (CTRL-C to exit)")


def conso_input():
        input_mode = 1
        count_updown = 0
        return count_updown

def vowel_input():
        input_mode = 2
        count_updown = 0
        return count_updown



def count_up(count_updown):
        count_updown = count_updown + 1
        return count_updown

def count_down(count_updown):
        count_updown = count_updown - 1
        return count_updown



def count_input(count_updown):
        if input_mode == 1:                     #자음입력
                count_updown
                
        elif input_mode == 2:                   #모음입력
                count_updown
                
        elif input_mode == 3:                   #숫자입력
                count_updown
                
                
        count_updown = 0
        return count_updown 



        

try:
        while True:
                if GPIO.input(Button_start)==0: #누를 때 button신호 0
                        count_updown = 0
                        
                        GPIO.add_event_detect(Button_up, GPIO.RISING, callback=count_up, bouncetime=300) # Botton_up이 rising될때 count_up함수 호출, 디바운싱 300
                        GPIO.remove_event_detect(Button_up)
                        
                        GPIO.add_event_detect(Button_down, GPIO.RISING, callback=count_down, bouncetime=300)
                        GPIO.remove_event_detect(Button_down)
                        
                        GPIO.add_event_detect(Button_input, GPIO.RISING, callback=count_input, bouncetime=300)
                        GPIO.remove_event_detect(Button_input)
                        
                        
                        GPIO.add_event_detect(Button_conso, GPIO.RISING, callback=conso_input, bouncetime=300)
                        GPIO.remove_event_detect(Button_conso)
                        
                        
                        

                         
                        GPIO.output(LED, True)
                                                                              
                else:
                        GPIO.output(LED, False)
                        print ("Button was Not Pressed!")
                        
                sleep(1)
                
                
                
except KeyboardInterrupt:      # CTRL-C를 누르면 발생 
        GPIO.cleanup()  #cleanup변수 뭔지 알아보기 
        
        