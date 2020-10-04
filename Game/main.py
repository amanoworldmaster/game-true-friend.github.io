#Importing pygame
import pygame
import pyttsx3
import random
import time
pygame.init()
f=pyttsx3.init()

#Window setting
screen_size=[350,600]
screen=pygame.display.set_mode(screen_size)

#title page
pygame.display.set_caption("True Friend")
pygame.display.update()

#Variable decleration
fps=30
start=False
user_x=100
score=0
level=0
background=pygame.image.load('background3.png')
background_image=pygame.image.load('user1.png')
user=pygame.transform.scale(background_image,(110,110))
user_image=pygame.image.load('chicken4.png')
chicken=pygame.transform.scale(user_image,(110,110))
chicken_y=[-1*random.randint(100,1500),-1*random.randint(100,1500),-1*random.randint(150,1500)]
clock=pygame.time.Clock()

#chicken moving and sound and negative scoreing
def move(i):
  global score
  chicken_y[i]=chicken_y[i]+5
  if chicken_y[i]>600:
      pygame.mixer.music.load("drop.mp3")
      pygame.mixer.music.set_volume(1)
      pygame.mixer.music.play()
      score=score-20
      score_fn(score,level)
      chicken_y[i]=-1*random.randint(100,1500)

#score add by 5 and play music function
def score_sound(n):
    global score
    pygame.mixer.music.load("catch.mp3")
    pygame.mixer.music.play()
    chicken_y[n]=-1*random.randint(100,1500)
    score+=5

#Score Update function
def score_fn(score,level):
    font=pygame.font.SysFont('Conic Sans MS',30)
    score_text="Score : "+str(score)
    level_text="Level : "+str(level)
    text_image=font.render(score_text,True,(51,102,255))
    level_image=font.render(level_text,True,(51,102,255))
    screen.blit(text_image,[20,10])
    screen.blit(level_image,[250,10])
f.say("This game TRUE FRIEND developed by Aman Singh, Using python ,Lets Play")
f.runAndWait()
f.stop()


#Game loop
while not start:
    pygame.event.get()
    keys=pygame.key.get_pressed()
    if keys[pygame.QUIT]:
        start = True
    if keys[pygame.K_RIGHT] and user_x<=265:
        user_x=user_x+5
    elif keys[pygame.K_LEFT] and user_x>-20:
        user_x=user_x-5
    move(0)
    move(1)
    move(2)
    screen.blit(background,[0,0])
    screen.blit(user,[user_x,520])
    screen.blit(chicken,[-10,chicken_y[0]])
    screen.blit(chicken,[140,chicken_y[1]])
    screen.blit(chicken,[267,chicken_y[2]])
    if chicken_y[0]>470 and user_x<80:
        score_sound(0)
    if chicken_y[1]>470 and (user_x<200 and user_x>86):
        score_sound(1)
    if chicken_y[2]>470 and user_x>200:
        score_sound(2)

#Score and level fps
    if score<300:
        fps=30
        leve=0
    elif score>=300 and score<700:
        fps=35
        level=1
    elif score>=700 and score<1700:
        fps=45
        level=2
    elif score>=1700 and score<4000:
        fps=50
        level=3
    elif score>=4000 and score<5000:
        fps=60
        level=4
    elif score>=5000 and score<6000 :
        fps=55
        level=5
    elif score>=6000 and score<7000:
        fps=70
        level=6
    elif score>=7000 and score<10000:
        fps=80
        level=7
    elif score>=10000:
        fps=90
        level=8
    elif score<=-500:
        font=pygame.font.SysFont('Conic Sans MS',80)
        lose_text="You Lose"
        lose_image=font.render(lose_text,True,(225,50,0))
        screen.blit(lose_image,[50,300])
        pygame.display.update()
        time.sleep(15)
        pygame.quit()
        quit()
    score_fn(score,level)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
