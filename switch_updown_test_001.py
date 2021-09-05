# import RPi.GPIO as GPIO      # gpio 라이브러리
# from time import sleep       # sleep 라이브러리

# LED = 23
# Button_start = 18   #시작 버튼, gpio 24
# Button_revise = 11    #정정 버튼, gpio 17
# Button_conso = 13     #자음 버튼, gpio 27
# Button_vowel = 15     #모음 버튼, gpio 22
# Button_num = 16       #숫자 버튼, gpio 23
# Button_down = 22       #아래 버튼, gpio 25
# Button_up = 29        #위 버튼, gpio 5
# Button_input = 31     #입력 버튼, gpio 6
# Button_back = 33      #뒤로/다시 버튼, gpio 13'
# Button_next = 35      #다음/네 버튼, gpio 19


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


# print ('Start the GPIO App')  # 시작을 알리자!
# print ("Press the button (CTRL-C to exit)")

# def count_up(count_updown):
#         count_updown = count_updown + 1
#         return count_updown

# def count_down(count_updown):
#         count_updown = count_updown - 1
#         return count_updown




# GPIO.add_event_detect(Button_up, GPIO.RISING, callback=count_up, bouncetime=300)
# GPIO.remove_event_detect(Button_up)
