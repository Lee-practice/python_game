import turtle # 터틀 그래픽 사용하기 위한 코드
import random # 랜덤을 사용하기 위한 코드
import time   # 시간을 사용하기 위한 코드

def R():
    player.forward(20) 

def L():
    player.backward(20)

def plus(): # score 값을 증가시킬 수 있는  함수
    global score # 전역 함수 score 사용
    a1=turtle.Turtle() # 터틀 만들기
    a1.hideturtle() # a1의 모습 숨기기
    a1.right(90) # 오른쪽으로 90도 회전
    a1.shape("circle") # 원 모양으로 바꾸기
    a1.shapesize(1,1,1) # a1의 사이즈 정하기
    a1.up() # a1의 펜 올리기
    a1.speed(1) # 가장 느린 속도로 설정
    a1.goto(random.randint(-200,200),200) # x좌표는 -200에서 200 사이의 수를 랜덤하게 정하고, y좌표는 200으로 해서 이동하기
    a1.showturtle() # a1 모습이 보이게 하기
    x=a1.xcor() # a1의 x좌표를 x에 넣기
    while a1.ycor()> 0:
        a1.forward(random.randint(1,20)) # a1의 y좌표가 0보다 크다면 1~20 사이의 수 중 하나를 정해서 그만큼 아래로 이동하기
    if x-30 <= player.xcor() <= x+30 and -20<=a1.ycor()<=20: 
        score = score + 100 # 플레이어 캐릭터의 x좌표가 a1의 x좌표 값±30 사이의 수이고 a1의 y좌표가 ±20 사이의 값이라면 score에 100 더하기
    if a1.ycor() <= 0:
        a1.hideturtle() # a1의 y좌표가 0보다 작거나 같다면 a1의 모습을 숨기기
        del a1 # a1 삭제
    


def minus(): # score 값을 감소시킬 수 있는 함수
    global score
    a1=turtle.Turtle()
    a1.hideturtle()
    a1.right(90)
    a1.shape("arrow") # a1의 모양을 화살표로 만들기
    a1.shapesize(1,1,1)
    a1.up()
    a1.speed(1)
    a1.goto(random.randint(-200,200),200)
    a1.showturtle()
    x=a1.xcor()
    while a1.ycor() > 0:
        a1.forward(random.randint(1,20))
    if x-30 <= player.xcor() <= x+30 -20<=a1.ycor()<=20 :
        score = score - 50 # 플레이어 캐릭터의 x좌표가 a1의 x좌표 값±30 사이의 수이고 a1의 y좌표가 ±20 사이의 값이라면  score에서 50 빼기
    if a1.ycor() <= 0:
        a1.hideturtle()
        del a1
    
start = input("시작하시겠습니까?(예,아니요): ")
if start == "예":
    score = 0 # 초기 score 값을 0으로 설정
    Time = int(time.time()) # 게임을 시작할 때의 현재 시간을 Time에 넣기
    now = int(time.time()) # 현재 시간을 now에 넣기

    player = turtle.Turtle()
    player.shapesize(1,1,1)
    player.up()
    player.speed(0) # player의 이동 속도를 가장 빠르게 설정
    screen = player.getscreen() #player가 이동하는 화면 얻기
    image = "C:\\Users\\USER\\Desktop\\player.gif" # image에 저장경로를 넣어 사용할 이미지 저장
    screen.addshape(image) # screen에 image 추가
    player.shape(image) # player 모양을 image로 바꾸기
    screen.onkeypress(L,"Left") # 왼쪽 화살표를 누르면 왼쪽으로 20 이동
    screen.onkeypress(R,"Right") # 오른쪽 화살표 누르면 오른쪽으로 20이동
    screen.listen() # 사용자의 반응이 올 때까지 기다리기

    while now <= Time + 60: # now의 값이 Time + 60의 값보다 작은 동안 실행
        random.choice([plus(), minus()]) # plus()와 minus() 중 랜덤하게 골라서 실행
        now = int(time.time()) # now에 현재 시간 넣기

    print(score) # 게임이 끝난 후 score 출력
