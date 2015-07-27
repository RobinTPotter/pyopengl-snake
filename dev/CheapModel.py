import array, struct
from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from time import time
from math import sin, cos, pi, floor, ceil, sqrt
import random


class Model:

    




    def __init__(self,file=None):
    
        self.coordinates=[]
        self.normals=[]
        self.colours=[]
        
        if file!=None:
            self.loader(file)
            
        self.list=None
        
    def loader(self,filename):    
    
        fp=open(filename,"rb")
        fp.seek(0,2)
        flength=int(fp.tell()/48) #length in triangles 48=2 lots of coords for vertices and colours  *3 for how many components for coord  *8 and for nunber of bytes to store a double
        print (("file",flength))        

        z=array.array("d")
        fp.seek(0)
        print(("flength",flength))
        z.fromfile(fp,flength*3)
        self.coordinates=z.tolist()
        print(("coordinates",len(self.coordinates)))

        cc=array.array("d")
        #fp.seek(0)
        cc.fromfile(fp,flength*3)
        self.colours=cc.tolist()
        print(("colours",len(self.colours)))
        
        self.makenormals()
        



    def norm(self,u0,v0):            
        
        mu=sqrt(u0[0]**2 + u0[1]**2 + u0[2]**2)    
        if mu==0: mu=1        
        u=[x/mu for x in u0]    
        mv=sqrt(v0[0]**2 + v0[1]**2 + v0[2]**2)    
        if mv==0: mv=1        
        v=[x/mv for x in v0]       
        
        n= [
            u[1]*v[2]-u[2]*v[1],
            u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0]
        ]
        
        mn=sqrt(n[0]**2 + n[1]**2 + n[2]**2)    
        if mn==0: mn=1  
          
        return [x/mn for x in n]   
        


    def makenormals(self):   
                   
        self.normals=[]
        tt=0 
        
        try:
                    
            for nn in range(0,len(self.coordinates),9):
                
                ax,ay,az,bx,by,bz,cx,cy,cz=self.coordinates[nn:nn+9]
                tt+=1
                a=[bx-ax,by-ay,bz-az]
                b=[cx-ax,cy-ay,cz-az] 
                nh=self.norm(a,b)
                ##each vertex has a normal we are spanning 3 above to get those that make a triange
                ##we are giving the same normal to each vertex in the triangle
                self.normals+=nh
                self.normals+=nh
                self.normals+=nh
            
            print(("normals",len(self.normals)))
        except:
            print(("bugger",tt,nn))



    def drawMe(self,actually=True):

        #print((1))
        initializing=False

        if (actually==False and self.list==None):

            print((2))
            self.list = glGenLists(1) 
            initializing=True
            print(("list",self.list))
            glNewList(self.list,GL_COMPILE) 
            print((3))


        if actually==True or (actually==False and initializing==True):
            
            print((4))
            #print(("got to draw"))
            glEnableClientState(GL_NORMAL_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)
            glEnableClientState(GL_VERTEX_ARRAY) 
            glNormalPointer(GL_FLOAT, 0, self.normals)    
            glColorPointer(3, GL_FLOAT, 0, self.colours)   
            glVertexPointer(3, GL_FLOAT, 0, self.coordinates)   
            glPushMatrix()    
            glDrawArrays(GL_TRIANGLES,0,int(len(self.coordinates)/3))
            glPopMatrix()
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)
            glDisableClientState(GL_NORMAL_ARRAY)
            print((5))

            if (actually==False and initializing==True):
                print((6))
                glEndList()
                print((7))
            
        elif (actually==False and not self.list==None):
            #print((8))
            glCallList(self.list)
            


    