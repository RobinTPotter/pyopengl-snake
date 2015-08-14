#!/usr/bin/python
from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from time import time
from math import sin, cos, pi, floor, ceil, sqrt
import random
from Models import lists, MakeLists, colours, lumin_no_black
import array, struct
import pickle

import sys, traceback

print(lumin_no_black)

from CheapModel import Model

X=46.0

name = b'testing'



class Joystick:
    
    up,down,left,right,fire="","","","",""
    keys={}

    def __init__(self,up="q",down="a",left="o",right="p",fire="m"):
        self.up=up
        self.down=down
        self.left=left
        self.right=right
        self.fire=fire
        print (("hello",self.right))
        
    def isUp(self):
        if self.up in self.keys: return self.keys[self.up]
        else: return False
         
    def isDown(self):
        if self.down in self.keys: return self.keys[self.down]
        else: return False
         
    def isLeft(self):
        if self.left in self.keys: return self.keys[self.left]
        else: return False
         
    def isRight(self):
        if self.right in self.keys: return self.keys[self.right]
        else: return False
         
    def isFire(self):
        if self.fire in self.keys:
            return self.keys[self.fire]
            
        else: return False         
         
    def keydownevent(self,c,x,y):
        if type(c) is int: kk=str(c)
        else: kk=c.decode('ascii').lower()
        
        self.keys[kk]=True
        #glutPostRedisplay()
        
    def keyupevent(self,c,x,y):
    
        if type(c) is int: kk=str(c)
        else: kk=c.decode('ascii').lower()
        if kk in self.keys: self.keys[kk]=False
        #glutPostRedisplay()

         
 
 
 
class BarrierGrowth:    

    def __init__(self,barrierset,x=5,y=5,t=50,dx=1,dy=0,len=10,speed=10):
    
        self.barrierset=barrierset
        self.seed=[x,y]
        self.dir=[dx,dy]
        self.len=len
        self.timestart=t
        self.speedmod=speed
        self.timeup=len*speed+t
        self.currentlen=0
        
    def go(self,nowtime,food,set_food_none_callback):
        
        if nowtime % self.speedmod==0:
        
            br=[self.seed[0]+self.dir[0]*self.currentlen,self.seed[1]+self.dir[1]*self.currentlen]
            if br==food: set_food_none_callback()
            self.barrierset.append(br)
            self.currentlen+=1
            
        if nowtime>self.timeup: return False
        
        return True
            
        
   
 
 
 
class Testing:

    SIZE=[50,50]
    #SNAKE=[[25,25],[25,24],[25,23],[25,22],[25,21]]
    SNAKE=[[25,25],[25,25],[25,25],[25,25],[25,25]]
    DIR=[0,1]
    TIME=0
    
    WIDTH=640
    HEIGHT=480
    
    FOOD=None
    POINTS=0
    Eaten=False
    
    GROWTH_FREQUENCY=20    
    
    cxx,cyy,czz=SIZE[0]/2,SIZE[1]/2,40
    fxx,fyy,fzz=SIZE[0]/2,SIZE[1]/2,0
    fox,foy,foz=0,1,0
    
    
    COUNT_DOWN=0
    
    rcxx,rcyy,rczz=SIZE[0]/2,SIZE[1]/2,40
    rfxx,rfyy,rfzz=SIZE[0]/2,SIZE[1]/2,0
    rox,roy,roz=0,1,0
    
    ctx,cty,ctz=SIZE[0]/2,SIZE[1]/2,60
    ftx,fty,ftz=SIZE[0]/2,SIZE[1]/2,0
    
    LEVEL=[]
    
    lock=False
    lastFrameTime=0
    topFPS=0
    
    States=["GAMEOVER","PLAY"]
    state=0
    
    joystick=Joystick(up="101",down="103",left="100",right="102",fire=" ")
    
    snake_cam=0
    snake_cam_max=300
    snake_cam_min=100    
    snake_cam_warn=100
    OK_press=0
    
    barriergrowers=[]
    
    message_timer=0
    
    def start(self,yes=None):
    
    
        if yes==None: self.LEVEL=[]
    
        '''
        for xx in range(-1,self.SIZE[0]+2):
            self.LEVEL.append([xx,-1])
            self.LEVEL.append([xx,self.SIZE[1]+1])
            
            
        for yy in range(-1,self.SIZE[1]+2):
            self.LEVEL.append([-1,yy])
            self.LEVEL.append([self.SIZE[0]+1,yy])
        '''

    
        if yes==None:
            self.COUNT_DOWN=5
            self.message("ready!!")
            
        self.barriergrowers.append(BarrierGrowth(self.LEVEL,x=-1,y=self.SIZE[1],t=0,dx=0,dy=-1,len=self.SIZE[1]+1,speed=1))
        self.barriergrowers.append(BarrierGrowth(self.LEVEL,x=self.SIZE[0]+1,y=0,t=10,dx=0,dy=1,len=self.SIZE[1]+1,speed=1))
        
        self.barriergrowers.append(BarrierGrowth(self.LEVEL,y=-1,x=self.SIZE[0],t=0,dx=-1,dy=0,len=self.SIZE[0]+1,speed=1))
        self.barriergrowers.append(BarrierGrowth(self.LEVEL,y=self.SIZE[1]+1,x=0,t=10,dx=1,dy=0,len=self.SIZE[0]+1,speed=1))
    
            
            
        self.barriergrowers.append(BarrierGrowth(self.LEVEL,x=self.SIZE[0]-5,y=self.SIZE[1]-5,t=80,dx=-1,dy=0,len=20,speed=10))
        self.barriergrowers.append(BarrierGrowth(self.LEVEL,x=5,y=5,t=80,dx=1,dy=0,len=20,speed=10))
            
        self.barriergrowers.append(BarrierGrowth(self.LEVEL,x=self.SIZE[0]-15,y=self.SIZE[1]-15,t=180,dx=-1,dy=0,len=30,speed=5))
        self.barriergrowers.append(BarrierGrowth(self.LEVEL,x=15,y=15,t=180,dx=1,dy=0,len=30,speed=5))
    
        self.ctz=abs(self.ctz)
        self.FOOD=None
        self.POINTS=0
        self.SIZE=[50,50]
        self.SNAKE=[]
        for sss in range(0,5):
            self.SNAKE.append(self.shct([25,25-sss],[0,1]))
        
        print((self.SNAKE))
        self.DIR=[0,1]
        self.TIME=1
        if yes==None: self.state=1
            
        self.snake_cam=0
        self.reset_cam()
        
        self.OK_press=0
        
        global X
        X=0

    def shct(self,xy,dir):
        return {"Location":xy,"Direction":dir}

    def reset_cam(self):
        self.ctx,self.cty,self.ctz=self.rcxx,self.rcyy,self.rczz
        self.ftx,self.fty,self.ftz=self.rfxx,self.rfyy,self.rfzz
        self.fox,self.foy,self.foz=self.rox,self.roy,self.roz

    def animate(self,FPS=20):
    
        if self.lock==True: return
    
        currentTime=time()
                
        
        self.TIME+=1
        
        
        
        if self.state==1:
        
             
            
            if self.COUNT_DOWN==0:
                
                            
                if self.TIME % self.GROWTH_FREQUENCY != 0 or self.Eaten==False: self.SNAKE.pop() #gets rid of last blob (if required)
                
                
            
                self.SNAKE.insert(0,{"Location":[self.SNAKE[0]["Location"][0]+self.DIR[0],self.SNAKE[0]["Location"][1]+self.DIR[1]],"Direction":self.DIR})
                
                if self.Eaten==True: self.Eaten=False
                
                xxxx=len(self.SNAKE)-1        
                
                    
                if self.FOOD==None:
                
                    testing=False            
                    fx,fy=0,0
                    
                    while testing==False:   

                        testing=True
                    
                        fx=int(random.random()*self.SIZE[0])
                        fy=int(random.random()*self.SIZE[1])
                                            
                                    
                        for s in self.SNAKE:
                            if s==[fx,fy]:
                                testing=False
                                
                        for b in self.LEVEL:
                            if b==[fx,fy]:
                                testing=False
                                    
                        
                        
                    self.FOOD=[fx,fy]
                    
                
                if self.FOOD[0]==self.SNAKE[0]["Location"][0] and self.FOOD[1]==self.SNAKE[0]["Location"][1]:
                    self.POINTS+=1
                    if self.snake_cam>0: self.POINTS+=1
                    self.message("nom!... nom...!!")
                    self.FOOD=None
                
                if self.OK_press==0:
                    
                    if self.snake_cam==0:
                        if self.joystick.isUp() and not self.DIR==[0,-1]:
                            self.DIR=[0,1]
                        elif self.joystick.isDown() and not self.DIR==[0,1]:
                            self.DIR=[0,-1]
                        elif self.joystick.isLeft() and not self.DIR==[1,0]:
                            self.DIR=[-1,0]
                        elif self.joystick.isRight() and not self.DIR==[-1,0]:
                            self.DIR=[1,0]
                            
                    else:
                        if self.joystick.isLeft():
                            tmp=[-self.DIR[1],self.DIR[0]]
                            self.DIR=tmp
                            self.OK_press=2
                        elif self.joystick.isRight():
                            tmp=[self.DIR[1],-self.DIR[0]]
                            self.DIR=tmp
                            self.OK_press=2
                        
                else:
                    self.OK_press-=1
                        
                        
                self.ftx=self.SNAKE[0]["Location"][0]
                self.fty=self.SNAKE[0]["Location"][1]
                self.ftz=self.ftz
                
                
                
                test=0
                for s0 in self.SNAKE[1:]:
                    s=s0["Location"]
                    if s==self.SNAKE[0]["Location"]:
                        self.Dead()
                        
                for b in self.LEVEL:
                    if b==self.SNAKE[0]["Location"]:
                        self.Dead()
                            
            else:                
                if self.TIME % 7 ==0: self.COUNT_DOWN-=1
                        
                        
                        
            for bg in self.barriergrowers:
                if bg.timestart<self.TIME:
                    res=bg.go(self.TIME,self.FOOD,self.set_food_none_callback)
                    if res==False:
                        self.barriergrowers.remove(bg)
                        
                        
        else:
        
            if self.joystick.isFire() and self.state==0:
                self.start()

            #print(self.TIME)
                
            if self.TIME % 50==0:
                print("tick")
                self.ctx=cos(self.TIME/10)*10
                self.cty=sin(self.TIME/10)*10
                self.ctz=cos(self.TIME/10)*2+1
                print((self.ctx,self.cty,self.ctz))
                
                #self.ctx=random.random()*(2+self.SIZE[0])-1
                #self.cty=random.random()*(2+self.SIZE[1])-1
                #self.ctz=random.random()*6+1
                               
            
                
                
        if self.TIME % 300==0 and (self.TIME>1000 or self.state==0) and self.snake_cam==0:
            self.ctz*=-1
            self.message("Reversed")
            
            
        change_factor=3.0
        
        self.fxx=self.fxx+(self.ftx-self.fxx)/change_factor
        self.fyy=self.fyy+(self.fty-self.fyy)/change_factor
        self.fzz=self.fzz+(self.ftz-self.fzz)/change_factor
            
        self.cxx=self.cxx+(self.ctx-self.cxx)/change_factor
        self.cyy=self.cyy+(self.cty-self.cyy)/change_factor
        self.czz=self.czz+(self.ctz-self.czz)/change_factor
        
        if (self.TIME % 200 < self.snake_cam_max and self.snake_cam==0 and self.TIME>self.snake_cam_max) and self.state==1:
            self.snake_cam=self.snake_cam_max
            self.message("Snake Cam!!")
            
        if self.snake_cam>0:
            self.snake_cam-=1
            
            if self.snake_cam==0:
                self.reset_cam()
                self.message("Reset")
            
                self.snake_cam_max=self.TIME+200 
                
            else:
                self.ctx,self.cty,self.ctz=self.SNAKE[0]["Location"][0]-2*self.DIR[0],self.SNAKE[0]["Location"][1]-2*self.DIR[1],2
                self.ftx,self.fty,self.ftz=self.SNAKE[0]["Location"][0],self.SNAKE[0]["Location"][1],2
                self.fox,self.foy,self.foz=0,0,1
            
            
        

        
        #self.cxx=self.cxx+(self.SNAKE[0][0]-self.cxx)/30
        #self.cyy=self.cyy+(self.SNAKE[0][1]-self.cyy)/30                 
    
        glutPostRedisplay()
        
        glutTimerFunc(int(1000/FPS), self.animate, FPS)

        drawTime=currentTime-self.lastFrameTime
        if drawTime>0:
            self.topFPS=int(1000/(drawTime))
            if int(100*time())%100==0:
                print(("draw self.TIME "+str(drawTime)+" top FPS "+str(1000/drawTime)))
                #self.tcxx,self.tcyy,self.tczz=random.randint(5,14),random.randint(5,14),random.randint(5,14)
        else:
            drawTime=1
            

        self.lastFrameTime=time()


    def message(self,str):
        self.message_timer=30
        self.message_text=str
    


    def set_food_none_callback(self):
        self.FOOD=None

    def Dead(self):
        self.state=0

    def reshape(self,width,height):
        print("hello reshape "+str((width,height)))
        self.HEIGHT=float(height)
        self.WIDTH=float(width)
        glViewport(0,0,int(self.WIDTH),int(self.HEIGHT)        )
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0,self.WIDTH/self.HEIGHT,1.,50.)
        glMatrixMode(GL_MODELVIEW)
        #glPushMatrix()
        glLoadIdentity()



    def draw(self):
        
        self.lock=True
        global X
        
        try:
        
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(60.0,self.WIDTH/self.HEIGHT,0.001,100.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
                      
            glRotate(X/1000,0,0,1)
            glEnable(GL_DEPTH_TEST)  

            glEnable(GL_LIGHTING)
            
            gluLookAt(self.cxx,self.cyy,self.czz,
                      self.fxx,self.fyy,self.fzz,
                      self.fox,self.foy,self.foz)
                
                
            # // track material ambient and diffuse from surface color, call it before glEnable(GL_COLOR_MATERIAL)
            glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
            glEnable(GL_COLOR_MATERIAL)
            #glColor(1,1,1,1)
            
            glMaterialfv(GL_FRONT,GL_AMBIENT_AND_DIFFUSE,colours["red"])
            
            glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,colours["cyan"])
    
            for b in self.LEVEL:
                #print (b)
                glPushMatrix()
                glTranslate(b[0],b[1],0)
                glutSolidCube(0.9)
                glPopMatrix()

      
            glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,colours["yellow"])
              
            if self.FOOD!=None:
                glPushMatrix()
                glTranslate(self.FOOD[0],self.FOOD[1],0)
                #glutSolidSphere(0.5,8,8)
                glScale(0.4,0.4,0.4)
                glRotate(X,0,0,1)
                glTranslate(0,0,5)
                self.chap.drawMe(actually=False)
                glPopMatrix()
                self.Eaten=True
        
        
            num=0
            snoffset=0
            
            for s0 in self.SNAKE:
                #print((s0))
                
                s=s0["Location"]
                d=s0["Direction"]
            
                glPushMatrix()
                glTranslate(s[0],s[1],0)
                if num==0:
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["red"])
                else:
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["green"])
                
                #glutSolidCube(0.9)
                
                #print(("num",num))
                middle=int(len(self.SNAKE)/2)

                a=0
                if d==[0,1]: a=90
                if d==[0,-1]: a=-90
                if d==[-1,0]: a=180
                
                if num==0:
                    glPushMatrix()
                    glRotate(a,0,0,1)
                    glScale(0.5,0.5,0.5)
                    glTranslate(-4,0,0)
                    self.cheapModel[0].drawMe(actually=False)         
                    glPopMatrix()
                elif num<middle:
                    glPushMatrix()
                    glRotate(a,0,0,1)
                    glScale(0.5,0.5,0.5)
                    glTranslate(-2,0,0)
                    self.cheapModel[1].drawMe(actually=False)         
                    glPopMatrix()    
                elif num==middle:
                    glPushMatrix()
                    glRotate(a,0,0,1)
                    glScale(0.5,0.5,0.5)
                    glTranslate(0,0,0)
                    self.cheapModel[2].drawMe(actually=False)         
                    glPopMatrix()   
                elif num==len(self.SNAKE)-1:
                    glPushMatrix()
                    glRotate(a,0,0,1)
                    glScale(0.5,0.5,0.5)
                    glTranslate(4,0,0)
                    self.cheapModel[4].drawMe(actually=False)         
                    glPopMatrix()   
                elif num>middle:
                    glPushMatrix()
                    glRotate(a,0,0,1)
                    glScale(0.5,0.5,0.5)
                    glTranslate(2,0,0)
                    self.cheapModel[3].drawMe(actually=False)         
                    glPopMatrix()   
                    

                
                
                
                glPopMatrix()
                num+=1
            
            
                
                
            cc=glGetFloatv(GL_CURRENT_COLOR)
                
                
            X+=3
            
            



            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluOrtho2D(0,self.WIDTH,0,self.HEIGHT)
            glMatrixMode(GL_MODELVIEW)            
            glLoadIdentity()
            
            glDisable(GL_DEPTH_TEST)  
                        
            textOn=True
            #if self.X %2 == 0: textOn=False
            

            #disable lights for the text etc
            glDisable(GL_LIGHTING)

            glTranslate(2,2,0)
            self.drawString("SCORE: "+str(self.POINTS)) ##+" sanke cam: "+str(self.snake_cam)+" TIME: "+str(self.TIME))
            
            if self.message_timer>0:
                self.message_timer-=1
                glPushMatrix()                    
                glTranslate(random.random()*3,18+random.random()*3,0)
                d="white"
                if self.TIME % 4<2: d="red"                    
                self.drawString(self.message_text,col=d)
                glPopMatrix()
            
            
            if self.COUNT_DOWN>0:
                d="yellow"
                if self.TIME % 2<1: d="red"
                glPushMatrix()
                glTranslate(self.WIDTH/2-25,self.HEIGHT/2-25,0)
                glScale(5,5,0)
                self.drawString(str(self.COUNT_DOWN),col=d)
                glPopMatrix()
            
            if self.state==0:   

                if self.TIME % 300>150:
                 
                    glPushMatrix()
                    
                    glTranslate(0,18,0)
                    d="white"
                    if self.TIME % 10<5: d="red"
                    self.drawString("game over - space to start.",col=d)
                    
                    #d="green"
                    #if self.TIME % 10<5:
                    #    #d="yellow"
                    d=lumin_no_black[self.TIME%len(lumin_no_black)]
                    glPushMatrix()
                    glTranslate(self.WIDTH/2-150,self.HEIGHT/2+50,0)
                    glScale(6,4,0)
                    self.drawString("GAME",col=d)
                    glTranslate(13,-15,0)
                    self.drawString("OF",col=d)
                    glTranslate(-27,-15,0)
                    self.drawString("SNAKES",col=d)
                    glPopMatrix()

                    glPopMatrix()

            

                else:
                 
                    glPushMatrix()
                    
                    d="green"
                    if self.TIME % 10<5: d="yellow"
                    
                    
                    
                    glPushMatrix()                    
                    
                    glTranslate(self.WIDTH/2,self.HEIGHT/2,0)

                    glScale(3,2,0)
                    glTranslate(-135,10*(float(len(self.teams))+4)/2,0)
                    
                    
                    self.drawString("~~~GAME OF SNAKES~~~",col=d)
                    #glTranslate(-10,-20,0)
                    glTranslate(0,-14,0)
                    glTranslate(0,-14,0)
                    glTranslate(0,-14,0)
                    
                    if self.teams!=None:
                        for t in self.teams.keys():
                            #print(("team:",t))
                            glTranslate(0,-14,0)
                            self.drawString(   t.ljust(8)                                                    ,col=d)
                    
                    glPopMatrix()
                    
                    
                    
                    
                    
                    
                    glPushMatrix()                    
                    
                    glTranslate(self.WIDTH/2,self.HEIGHT/2,0)

                    glScale(1,2,0)
                    glTranslate(-135,10*(float(len(self.teams))+4)/2,0)
                    
                    
                    #glTranslate(-10,-20,0)
                    glTranslate(0,-14,0)
                    glTranslate(0,-14,0)
                    self.drawString(   " ".ljust(8)   +   str("Gms").rjust(5)      +   str("Tot").rjust(5)      +   str("Avg").rjust(5)     +   str("Tm.").rjust(5)        +   str("Bl.").rjust(5)        +   str("Bl.").rjust(5)        ,col=d)
                    
                    glTranslate(0,-14,0)
                    
                    
                    if self.teams!=None:
                        for t in self.teams.keys():
                            #print(("team:",t))
                            glTranslate(0,-14,0)
                            self.drawString(   " ".ljust(8)   +   str(len(self.teams[t]["games"])).rjust(5)      +   str(2).rjust(5)      +   str(3).rjust(5)     +   str(4).rjust(5)       +   str(4).rjust(5)       +   str(4).rjust(5)        ,col=d)
                    
                    glPopMatrix()
                    
                    
                    
                    
                    
                    

                    glPopMatrix()

            
            
            
            glColor(cc)



        except Exception as a:
            print (str(traceback.print_exc(file=sys.stdout)))
            print (("blah",a))
            
        finally:                
            self.lock=False


    def initkey(self,cl):   
    
        for c in cl:
            self.joystick.keydownevent(c,0,0)        
            self.joystick.keyupevent(c,0,0)

    def display(self):

        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #glClearDepth(1.0)
        #glEnable(GL_DEPTH_TEST)
        #glDepthFunc(GL_LEQUAL)

        #glLoadIdentity()
        
        
        self.draw()
        
        glutSwapBuffers()
        #glFinish()


    def drawString(self,string,col="yellow"):
        glPushMatrix()


        for l in range(0,len(string)):
            
            if string[l].upper()=="#":
                if len(string[l:])>2:
                    if string[l:l+3]=="###": break
            
            
            glPushMatrix()
            glTranslate(0,0,0.5)
            glColor(colours["black"])
            glLineWidth(3.0)
            if string[l].upper() in lists: glCallList(lists[string[l].upper()])
            else:  glCallList(lists[" "])
            glPopMatrix()
            
            
            glPushMatrix()
            glTranslate(0,0,0)
            glColor(colours[col])
            glLineWidth(0.5)
            if string[l].upper() in lists: glCallList(lists[string[l].upper()])
            else:  glCallList(lists[" "])
            glPopMatrix()
            glTranslate(14,0,0)



        glPopMatrix()


    def __init__(self,teamFile):

        print(teamFile)
        self.teams={}
    
        if teamFile!=None:
            
            try:
            
                line=0
                for t in open(teamFile,"rb").read().split("\n"):
                    line+=1
                    if line==1 and t!="TEAMNAMES":
                        raise Exception("bah not a list")
                    else:
                        if len(t)>0 and line>1:
                            print(t)
                            self.teams[t]={"games":[]}
                        
           
            except Exception as e:
                print("dor?")
                print (e)
                self.teams=pickle.loads(open(teamFile,"rb").read())
                
            print(self.teams)
            
        else:
            self.teams["robin"]={"games":[]}
            self.teams["chris"]={"games":[]}
            self.teams["lisa"]={"games":[]}
            self.teams["burtosa"]={"games":[]}
            self.teams["sam"]={"games":[]}
            self.teams["alex"]={"games":[]}
            
            
            
            
        if teamFile!=None: open(teamFile,"wb").write(pickle.dumps(self.teams))
            
        


        print((bool(glutInit)))
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(self.WIDTH,self.HEIGHT)
        glutCreateWindow(name)
        
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    
        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK) 
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        
        
        
        
        glEnable(GL_LIGHTING)
        lightZeroPosition = [0,0,5]
        lightZeroColor = [1.0,1.0,1.0,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.02)
        glEnable(GL_LIGHT0)
        
        
        
        MakeLists()
        
        self.cheapModel=[]
        
        self.cheapModel.append(Model("models/piece1.dat"))
        self.cheapModel.append(Model("models/piece2.dat"))
        self.cheapModel.append(Model("models/piece3.dat"))
        self.cheapModel.append(Model("models/piece4.dat"))
        self.cheapModel.append(Model("models/piece5.dat"))
        self.chap=Model("models/chap.dat")
        
        
        
        
        
        glutIgnoreKeyRepeat(1)

        glutReshapeFunc(self.reshape)
        
        glutSpecialFunc(self.joystick.keydownevent)
        glutSpecialUpFunc(self.joystick.keyupevent)

        glutKeyboardFunc(self.joystick.keydownevent)
        glutKeyboardUpFunc(self.joystick.keyupevent)
        glutDisplayFunc(self.display)
        #glutIdleFunc(self.display)
        
        glMatrixMode(GL_PROJECTION)
        gluPerspective(60.0,640.0/480.,0.001,100.0)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        
        
        ##self.initkey("zxdcfvqaopm")
        
        self.animate()
        self.start(yes="No")
        
        glutMainLoop()

        return


        
if __name__ == '__main__': 

    teamFile=None

    if len(sys.argv)==2: 
        teamFile=sys.argv[1]
        print(teamFile)

    else:
        print("no teams")
            
    Testing(teamFile)
