import pygame
pygame.init()
display=pygame.display.set_mode((800,500))
pygame.display.set_caption("Get Ready To Thrive")

time_delay=pygame.time.Clock()

background=pygame.image.load("background.png")
initial_image=pygame.image.load("STANDING.jpg")

score=0
#making bg:
#making hero:
#making hero to move:
#making hero to jump:
#making enemy:
#making hero shoot bullets
#making health bar
#creating health and marking score
#printing score in top left corner

class hero(object):
    #images r/l
    walkLeft=[pygame.image.load("L1.jpg"),pygame.image.load("L2.jpg"),pygame.image.load("L3.jpg"),pygame.image.load("L4.jpg"),pygame.image.load("L5.jpg"),pygame.image.load("L6.jpg")]
    walkRight=[pygame.image.load("R1.jpg"),pygame.image.load("R2.jpg"),pygame.image.load("R3.jpg"),pygame.image.load("R4.jpg"),pygame.image.load("R5.jpg"),pygame.image.load("R6.jpg")]
    
    def __init__(self,x,y,width,height):#position and dimension of the hero image
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=8#vel of hero
        self.left=False
        self.right=False#assuring hero will be standing at first
        self.standing=True
        self.walkCount=0
        self.jumpCount=10
        self.willjump=False#at initial hero wont jump
        self.hitbox=(self.x,self.y,50,67)#dimensions of bullet hitting rect
        
        
    
    def draw(self,display):
        if self.walkCount+1>=24:#6 images, each 4 times
            self.walkCount=0
        if not(self.standing):
            if self.right:
                display.blit(self.walkRight[self.walkCount//4],(self.x,self.y))#run images,position same as char
                self.walkCount+=1
            elif self.left:#can also use else
                display.blit(self.walkLeft[self.walkCount//4],(self.x,self.y))
                self.walkCount+=1
        else:#when standing still,but facing right or left
            if self.right:
                display.blit(self.walkRight[0],(self.x,self.y))
            else:
                display.blit(self.walkRight[0],(self.x,self.y))
        self.hitbox=(self.x,self.y,50,67)
        pygame.draw.rect(display,(255,0,0),self.hitbox,2)#if we dont write 2 then whole img of hero gets colored red
       
        

class enemy(object):
    #images r/l
    walkRight=[pygame.image.load('walk1.png'),pygame.image.load('walk2.png'),pygame.image.load('walk3.png'),pygame.image.load('walk4.png'),pygame.image.load('walk5.png'),pygame.image.load('walk6.png'),pygame.image.load('walk7.png'),pygame.image.load('walk8.png'),pygame.image.load('walk9.png'),pygame.image.load('walk10.png')]
    walkLeft=[pygame.image.load('walkL1.png'),pygame.image.load('walkL2.png'),pygame.image.load('walkL3.png'),pygame.image.load('walkL4.png'),pygame.image.load('walkL5.png'),pygame.image.load('walkL6.png'),pygame.image.load('walkL7.png'),pygame.image.load('walkL8.png'),pygame.image.load('walkL9.png'),pygame.image.load('walkL10.png')]


    def __init__(self,x,y,width,height,end):#position,dimension and region in which enemy moves
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.walkCount=0
        self.vel=10#velocity of enemy
        self.region=[self.x,self.end]#enemy moves in this region
        self.hitbox=(self.x,self.y,57,77)#this region will decide that bullet will hit or not
        self.health_bar=(self.hitbox[0],self.hitbox[1]-10,60,5)#dimensions of heath bar
        self.visible=True
        self.health=115

        
    def move(self):#movements of enemy
        if self.vel>0:#moving right
            if self.x + self.vel< self.region[1]:#dont exceed given region
                self.x+=self.vel
            else:
                self.vel=self.vel*(-1)#turn direction of enemy
                self.walkCount=0
        else:
            if self.x + self.vel > self.region[0]:
                self.x+=self.vel
            else:
                self.vel=self.vel*(-1)#turn direction of enemy
                self.walkCount=0
            
    def draw(self,display):#draw the enemy
        self.move()
        if self.visible:

            if self.walkCount +1>=40:
                self.walkCount=0
            if self.vel>0:
                display.blit(self.walkRight[self.walkCount//4],(self.x,self.y))#()has position of the image
                self.walkCount+=1
            else:
                display.blit(self.walkLeft[self.walkCount//4],(self.x,self.y))
                self.walkCount+=1
            self.hitbox=(self.x,self.y,57,77)
            pygame.draw.rect(display,(0,0,0),self.hitbox,2)
            
            self.health_bar=(self.hitbox[0],self.hitbox[1]-10,60,5)
            pygame.draw.rect(display,(255,0,0),self.health_bar,2)#red#color,coordinates
            
            pygame.draw.rect(display,(255,255,255),(self.hitbox[0],self.hitbox[1]-10,60- 0.5*(115 - self.health),5))#white

        
    def hit(self):#enemy is hit by bullet
        if self.health>0:
            print('I am hit, Pardon!')
            self.health-=1
        else:
            self.visible=False


class shoot(object):
    def __init__(self,x,y,radius,color,direction):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=facing*12#velocity of the bullet

    def draw(self,display):
        pygame.draw.circle(display,self.color,(self.x,self.y),self.radius)#dimensions of circle#i think order matters
        

def updatescreen():
    display.blit(background,(0,0))
    nobita.draw(display)
    thor.draw(display)
    for bullet in bullets:
        bullet.draw(display)#we have to use for loop over here as bz we have defined dimensions of bullet not bullets

    counter=font.render("Your Score " + str(score),1,(0,0,0))#render prints the text on screen
    display.blit(counter,(550,10))#position of counter
    pygame.display.update()
   
    
#set bg, score,health bar, bullets and all other stuff
#main loop
run=True
#getting font
#print(pygame.font.get_fonts())
font=pygame.font.SysFont('calibri',30,True)#name,size,bold,italic
bullets=[]
#name of hero
nobita=hero(400,367,60,75)
thor=enemy(0,358,60,75,800)
#shots=shoot(round(nobita.x + nobita.width//2),round(nobita.y + nobita.height//2),(0,0,0),5,facing)
while run:
    time_delay.tick(24)#there will be time gap of 0.024 sec
    updatescreen()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run==False#i have not worked much on this till now


    for bullet in bullets:
        if bullet.x + bullet.radius > thor.hitbox[0] and bullet.x - bullet.radius < thor.hitbox[0]+ thor.hitbox[2]:#assuring bullet is inside region via x coord
            if bullet.y - bullet.radius < thor.hitbox[1] + thor.hitbox[3] and bullet.y + bullet.radius > thor.hitbox[1]:#assuring bullet is inside region via y coord
                thor.hit()
                bullets.pop(bullets.index(bullet))
                score+=1#we count score once we remove bullet that is once bulelt hits enemy
        if bullet.x<800 and bullet.x>0:
            bullet.x+=bullet.vel
        else:#we remove bullet as if we keep it, then it will be seen at corners of the screen
            bullets.pop(bullets.index(bullet))


                
    pressed=pygame.key.get_pressed()
    ##here we used if,elif,else as at one time either of left or right is possible not both simultanueously
    if pressed[pygame.K_LEFT] and nobita.x > nobita.vel:#assuring hero dont go out of screen from left
        nobita.x-=nobita.vel
        nobita.left=True
        nobita.right=False
        nobita.standing=False
    elif pressed[pygame.K_RIGHT] and nobita.x<800 - nobita.width - nobita.vel:#assuring hero dont go out of screen from right
        nobita.x+=nobita.vel
        nobita.right=True
        nobita.left=False
        nobita.standing=False
    else:
        #if we dont use this else then nobita will continue walking once started
        nobita.standing=True
        nobita.walkCount=0#resetting walkCount so as to move again

    if not (nobita.willjump):
        if pressed[pygame.K_UP]:
               nobita.willjump=True#it makes not jump to jump and sends again back to loop and then else statement runs
               nobita.right=False
               nobita.left=False
               nobita.standing=False#####
               
    else:#to make jump we have to use quadratic concept
        if nobita.jumpCount>=-10:#since if jump count is -10 means will stop going more up
            neg=1#move up from 10 to 0
            if nobita.jumpCount<0:#when jc is blw 10 and 0 the hero will move up and if we dont use this condition then hero will take pause and will agian move up till -10 and wont come down.
                neg=-1#move down from 0 to -10
            nobita.y-=(nobita.jumpCount**2)*0.5*neg
            nobita.jumpCount-=1
        else:
            nobita.willjump=False
            nobita.jumpCount=10


    if pressed[pygame.K_SPACE]:
        if nobita.left:#hero looking left
            facing=-1
        else:
            facing=1
        if len(bullets)<7:#this is moximum number of bullets that can be available on screen
            bullets.append(shoot(round(nobita.x + nobita.width//2),round(nobita.y + nobita.height//2),5,(0,0,0),facing))#we cant define it earlier as we dont had facing defined earlier
           

#shots=shoot(round(nobita.x + nobita.width//2),round(nobita.y + nobita.height//2),(0,0,0),5,facing)

pygame.quit()
