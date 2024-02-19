import turtle
import time
import random
import playsound
import pygame

pygame.mixer.init()  # pygame ses başlat
# arkaplandaki müziği başlatıyor
pygame.mixer.music.load("game.mp3")
pygame.mixer.music.play(-1)  #tekrar 

Liste = [] #yılanın kuyruğu
skor = 0
maxSkor = 0

# Çerçeve Ayarları
w = turtle.Screen()
w.title("Yılan Oyunu")
w.setup(600, 600)
w.bgcolor("purple")
w.tracer(0) #güncelleme hızı,hiç gecikme olmadan günceller

#yılan nesne
yilan = turtle.Turtle()
yilan.speed(0)
yilan.shape("circle")
yilan.color("black")
yilan.penup()
yilan.goto(0, 0)
yilan.yon = "dur"


def hareket():
    if yilan.yon == "ust":
        y = yilan.ycor()  # y ekseninde git
        yilan.sety(y + 20)

    if yilan.yon == "asagi":
        y = yilan.ycor()
        yilan.sety(y - 20)

    if yilan.yon == "sag":
        x = yilan.xcor()  # x ekseninde git
        yilan.setx(x + 20)

    if yilan.yon == "sol":
        x = yilan.xcor()
        yilan.setx(x - 20)


def yukariGit():
    if yilan.yon != "asagi":
        yilan.yon = "ust"


def asagiGit():
    if yilan.yon != "ust":
        yilan.yon = "asagi"


def sagaGit():
    if yilan.yon != "sol":
        yilan.yon = "sag"


def solaGit():
    if yilan.yon != "sag":
        yilan.yon = "sol"


w.listen()
w.onkeypress(yukariGit, "Up")
w.onkeypress(asagiGit, "Down")
w.onkeypress(sagaGit, "Right")
w.onkeypress(solaGit, "Left")


#yem nesne
yem = turtle.Turtle()
yem.speed(0)
yem.shape("square")
yem.color("red")
yem.penup()
yem.goto(0, 100)


#yemi yedikten sonra
def yemiYe():
    
    if yilan.distance(yem) < 20:  # distance = 2 nesne arasındaki mesafeyi ölçer
        pygame.mixer.Sound("eat.mp3").play()
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)

        kuyruk = turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("white")
        kuyruk.penup()
        Liste.append(kuyruk)
        global skor,maxSkor

        skor += 5
        if skor > maxSkor:
            maxSkor = skor
            w.title("Skor: {} En yüksek skor: {}".format(skor, maxSkor))

    uzunluk = len(Liste)
    for i in range(uzunluk - 1, 0, -1):
        x = Liste[i - 1].xcor()
        y = Liste[i - 1].ycor()
        Liste[i].goto(x, y)

    if len(Liste) > 0:
        x = yilan.xcor()
        y = yilan.ycor()
        Liste[0].goto(x, y)


def baslangic():
    time.sleep(2.3)
    yilan.goto(0, 0)
    yilan.yonu = "dur"
    global skor
    for eklem in Liste:  #kuyruk sayısı kadar dönecek
        eklem.goto(1000, 1000)
    Liste.clear()
    skor = 0
    w.title("Skor:{} En yüksek skor: {}".format(skor, maxSkor))


w.listen() 
while True:
    w.update()
    yemiYe()
    hareket()
    if yilan.xcor() > 290 or yilan.xcor() < -290 or yilan.ycor() > 290 or yilan.ycor() < -290:  #çerçeveye çarptığında sıfırla
        pygame.mixer.Sound("dead.mp3").play()
        baslangic()

    for eklem in Liste:
        if eklem.distance(yilan) < 20: #kendine çarptığında sıfırla
            pygame.mixer.Sound("dead.mp3").play()
            baslangic()
    time.sleep(0.1)
