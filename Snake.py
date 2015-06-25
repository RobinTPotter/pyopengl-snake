#!/bin/python
from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from time import time
from math import sin, cos, pi, floor, ceil, sqrt
import random
from Models import lists, MakeLists, colours
import array, struct

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

         
 
 
 
class Testing:

    SIZE=[50,50]
    SNAKE=[[5,5],[5,4],[5,3],[5,2]]
    DIR=[1,0]
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
    
    
    rcxx,rcyy,rczz=SIZE[0]/2,SIZE[1]/2,40
    rfxx,rfyy,rfzz=SIZE[0]/2,SIZE[1]/2,0
    rox,roy,roz=0,1,0
    
    ctx,cty,ctz=SIZE[0]/2,SIZE[1]/2,50
    ftx,fty,ftz=SIZE[0]/2,SIZE[1]/2,0
    
    
    
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
    
    
    def start(self):
    
        self.ctz=abs(self.ctz)
        self.FOOD=None
        self.POINTS=0
        self.SIZE=[50,50]
        self.SNAKE=[[5,5],[5,4],[5,3],[5,2]]
        self.DIR=[1,0]
        self.TIME=1
        self.state=1
            
        self.snake_cam=0
        self.reset_cam()
        
        global X
        X=0

    def reset_cam(self):
        self.ctx,self.cty,self.ctz=self.rcxx,self.rcyy,self.rczz
        self.ftx,self.fty,self.ftz=self.rfxx,self.rfyy,self.rfzz
        self.fox,self.foy,self.foz=self.rox,self.roy,self.roz

    def animate(self,FPS=20):
    
        if self.lock==True: return
    
        currentTime=time()
                
        
        self.TIME+=1
        
        if self.state==1:
        
            
            test=0
            for s in self.SNAKE[1:]:
                if s==self.SNAKE[0]:
                    self.Dead()
                        
            if self.TIME % self.GROWTH_FREQUENCY != 0 or self.Eaten==False: self.SNAKE.pop() #gets rid of last blob (if required)
            
            
        
            self.SNAKE.insert(0,[self.SNAKE[0][0]+self.DIR[0],self.SNAKE[0][1]+self.DIR[1]])
            
            if self.Eaten==True: self.Eaten=False
            
            xxxx=len(self.SNAKE)-1        
            
            if self.SNAKE[0][0]>self.SIZE[0] or self.SNAKE[0][0]<0 or self.SNAKE[0][1]>self.SIZE[1] or self.SNAKE[0][1]<0:
                self.Dead()
                
            if self.FOOD==None:
                self.FOOD=[int(random.random()*self.SIZE[0]),int(random.random()*self.SIZE[1])]
            
            
            if self.FOOD[0]==self.SNAKE[0][0] and self.FOOD[1]==self.SNAKE[0][1]:
                self.POINTS+=1
                self.FOOD=None
            
            
            if self.joystick.isUp():
                self.DIR=[0,1]
            elif self.joystick.isDown():
                self.DIR=[0,-1]
            elif self.joystick.isLeft():
                self.DIR=[-1,0]
            elif self.joystick.isRight():
                self.DIR=[1,0]
                          
                
            self.ftx=self.SNAKE[0][0]
            self.fty=self.SNAKE[0][1]
            self.ftz=self.ftz
            
            
        else:
        
            if self.joystick.isFire() and self.state==0:
                self.start()
                
            if self.TIME % 100==0:
                self.ftx=random.random()*self.SIZE[0]
                self.fty=random.random()*self.SIZE[1]
                               
                
                
                
        if self.TIME % 300==0 and (self.TIME>1000 or self.state==0) and self.snake_cam==0:
            self.ctz*=-1
            
        self.fxx=self.fxx+(self.ftx-self.fxx)/10.0
        self.fyy=self.fyy+(self.fty-self.fyy)/10.0
        self.fzz=self.fzz+(self.ftz-self.fzz)/10.0
            
        self.cxx=self.cxx+(self.ctx-self.cxx)/10.0
        self.cyy=self.cyy+(self.cty-self.cyy)/10.0
        self.czz=self.czz+(self.ctz-self.czz)/10.0
        
        if self.TIME % 200 < self.snake_cam_max and self.snake_cam==0 and self.TIME>self.snake_cam_max:
            self.snake_cam=self.snake_cam_max
            
        if self.snake_cam>0:
            self.snake_cam-=1
            
            if self.snake_cam==0:
                self.reset_cam()
                
            else:
                self.ctx,self.cty,self.ctz=self.SNAKE[0][0]-2*self.DIR[0],self.SNAKE[0][1]-2*self.DIR[1],2
                self.ftx,self.fty,self.ftz=self.SNAKE[0][0],self.SNAKE[0][1],2
                self.fox,self.foy,self.foz=0,0,1
            
            
        

        
        #self.cxx=self.cxx+(self.SNAKE[0][0]-self.cxx)/50
        #self.cyy=self.cyy+(self.SNAKE[0][1]-self.cyy)/50                 
    
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

    def Dead(self):
        self.state=0

    def __init__(self):

        
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
        
        # // track material ambient and diffuse from surface color, call it before glEnable(GL_COLOR_MATERIAL)
        #glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        #glEnable(GL_COLOR_MATERIAL)
            
        glEnable(GL_LIGHTING)
        lightZeroPosition = [0,0,5]
        lightZeroColor = [0.9,1.0,0.9,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.2)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)
        
        MakeLists()
        
        glutIgnoreKeyRepeat(1)
        
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
        
        glutMainLoop()

        return




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
                
            #glTranslate(-25,-25,-35)
            
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
            
            #glBegin(GL_POINTS)
            for x in range(-1,self.SIZE[0]+2):
                for y in range(-1,self.SIZE[1]+2):
                    if x==-1 or y==-1 or x==self.SIZE[0]+1 or y==self.SIZE[1]+1:
                        #glVertex3f(x,y,0)
                        glPushMatrix()
                        glTranslate(x,y,0)
                        #print (x,y)
                        glutSolidCube(0.9)
                        glPopMatrix()
                    
              
            #glEnd()
            #glPopMatrix()
            
            if self.FOOD!=None:
                glPushMatrix()
                glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["yellow"])
                glTranslate(self.FOOD[0],self.FOOD[1],0)
                glutSolidSphere(0.5,8,8)
                glPopMatrix()
                self.Eaten=True
        
    
        
            num=0
            for s in self.SNAKE:
                #print (s))
            
                glPushMatrix()
                glTranslate(s[0],s[1],0)
                if num==0:
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["red"])
                else:
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["green"])
                glutSolidCube(0.9)
                glPopMatrix()
                num+=1
            
            X+=3



            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluOrtho2D(0,self.WIDTH,0,self.HEIGHT)
            glMatrixMode(GL_MODELVIEW)            
            glLoadIdentity()
            
            glDisable(GL_DEPTH_TEST)  
            
            #glScale(self.WIDTH/640.0,self.WIDTH/640.0,1)
            
            textOn=True
            #if self.X %2 == 0: textOn=False
            

            #disable lights for the text etc
            glDisable(GL_LIGHTING)

            glTranslate(2,2,0)
            self.drawString("SCORE: "+str(self.POINTS)) ##+" sanke cam: "+str(self.snake_cam)+" TIME: "+str(self.TIME))
            
            if self.state==0:                
                glTranslate(0,18,0)
                d="white"
                if self.TIME % 10<5: d="red"
                self.drawString("game over  space to start",col=d)





        except Exception as a:
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


        
if __name__ == '__main__': Testing()
