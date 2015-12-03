


from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


colours={}

colours["gold"]=[1.0,0.9,0.0,1.0]
colours["red"]=[1.0,0.0,0.0,1.0]
colours["green"]=[0.0,1.0,0.0,1.0]
colours["blue"]=[0.0,0.0,1.0,1.0]
colours["yellow"]=[1.0,1.0,0.0,1.0]
colours["cyan"]=[0.0,1.0,1.0,1.0]
colours["pink"]=[1.0,0.0,1.0,1.0]
colours["white"]=[1.0,1.0,1.0,1.0]    
colours["gold"]=[1.0,0.9,0.0,1.0]
colours["hat"]=[0.105,0.097,0.207,1.0]
colours["body"]=[0.093,0.02,0.0006071,1.0]
colours["arm"]=[0.24,0.007,0.0,1.0]
colours["shoe"]=[0.096,0.3,1.0]
colours["wand"]=[0,0,0,1.0]
colours["wandtip"]=[1,1,1,1.0]
colours["black"]=[0,0,0,1.0]

for rr in range(0,5):
    for gg in range(0,5):
        for bb in range(0,5):
            colours[str(rr)+"_"+str(gg)+"_"+str(bb)]=[float(rr)/5,float(gg)/5,float(bb)/5]

lumin=[]

z=zip(colours.keys(),colours.values())

lum0=[(zz[1][0]*256)**2+(zz[1][1]*256)**2+(zz[1][2]*256)**2 for zz in z]

lumin=zip(colours.keys(),colours.values(),lum0)

lumin0=sorted(lumin,key=lambda a: a[2])
lumin=[c[0] for c in sorted(lumin0,key=lambda a: a[2])]
lumin_no_black=[c[0] for c in sorted(lumin0,key=lambda a: a[2]) if c[2]>100]


del(lum0)
del(lumin0)



lists={}

def MakeLists():

    #global lists
    lists["broken brick"] = glGenLists(1)
    print("about to compile list"+str(lists["broken brick"]))
    glNewList(lists["broken brick"],GL_COMPILE)

    glPushMatrix()
    glTranslate(0.25,0.25,0.25)
    glScale(0.4,0.44,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.25,0.25,0.25)
    glScale(0.44,0.44,0.34)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.25,-0.25,0.25)
    glScale(0.44,0.44,0.34)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.25,-0.25,0.25)
    glScale(0.44,0.44,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.25,0.25,-0.25)
    glScale(0.34,0.34,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.25,0.25,-0.25)
    glScale(0.44,0.34,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.25,-0.25,-0.25)
    glScale(0.24,0.44,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.25,-0.25,-0.25)
    glScale(0.24,0.5,0.44)
    glutSolidCube(1)
    glPopMatrix()
    
    glEndList()


    lists[" "] = glGenLists(1) 
    glNewList(lists[" "],GL_COMPILE) 
    glEndList()

    lists["."] = glGenLists(1) 
    glNewList(lists["."],GL_COMPILE)
    glBegin(GL_LINE_STRIP)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.5, 0.0) 
    glEnd()
    glEndList()
    
    
    lists["!"] = glGenLists(1) 
    glNewList(lists["!"],GL_COMPILE)
    glBegin(GL_LINES)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.5, 0.0) 
    glVertex2f(5.0, 2)
    glVertex2f(6, 10.0) 
    glEnd()
    glEndList()

    

    lists["-"] = glGenLists(1) 
    glNewList(lists["-"],GL_COMPILE)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.5, 5.0)
    glVertex2f(9.5, 5.0) 
    glEnd()
    glEndList()

    lists["*"] = glGenLists(1) 
    glNewList(lists["*"],GL_COMPILE)
    glBegin(GL_LINES)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.0, 10.0) 
    
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0) 
    
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 0.0) 
    
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0) 
    
    
    
    glEnd()
    glEndList()

    lists["A"] = glGenLists(1) 
    glNewList(lists["A"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()


    lists["B"] = glGenLists(1) 
    glNewList(lists["B"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["C"] = glGenLists(1) 
    glNewList(lists["C"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()


    lists["D"] = glGenLists(1) 
    glNewList(lists["D"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(10.0, 8.0)
    glVertex2f(10.0, 2.0)
    glVertex2f(8.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["E"] = glGenLists(1) 
    glNewList(lists["E"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()


    lists["F"] = glGenLists(1) 
    glNewList(lists["F"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()


    lists["G"] = glGenLists(1) 
    glNewList(lists["G"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(8.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(8.0, 10.0) 
    glEnd()
    glEndList()


    lists["H"] = glGenLists(1) 
    glNewList(lists["H"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()


    lists["I"] = glGenLists(1) 
    glNewList(lists["I"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()


    lists["J"] = glGenLists(1) 
    glNewList(lists["J"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 2.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(3.0, 0.0)
    glVertex2f(5.0, 2.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()


    lists["K"] = glGenLists(1) 
    glNewList(lists["K"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["L"] = glGenLists(1) 
    glNewList(lists["L"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["M"] = glGenLists(1) 
    glNewList(lists["M"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["N"] = glGenLists(1) 
    glNewList(lists["N"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["O"] = glGenLists(1) 
    glNewList(lists["O"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["P"] = glGenLists(1) 
    glNewList(lists["P"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["Q"] = glGenLists(1) 
    glNewList(lists["Q"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["R"] = glGenLists(1) 
    glNewList(lists["R"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["S"] = glGenLists(1) 
    glNewList(lists["S"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["T"] = glGenLists(1) 
    glNewList(lists["T"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(5.0, 0.0) 
    glEnd()
    glEndList()



    lists["U"] = glGenLists(1) 
    glNewList(lists["U"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()



    lists["V"] = glGenLists(1) 
    glNewList(lists["V"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()



    lists["W"] = glGenLists(1) 
    glNewList(lists["W"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["X"] = glGenLists(1) 
    glNewList(lists["X"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()



    lists["Y"] = glGenLists(1) 
    glNewList(lists["Y"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(5.0, 0.0) 
    glEnd()
    glEndList()



    lists["Z"] = glGenLists(1) 
    glNewList(lists["Z"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["0"] = glGenLists(1) 
    glNewList(lists["0"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["1"] = glGenLists(1) 
    glNewList(lists["1"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["2"] = glGenLists(1) 
    glNewList(lists["2"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(7.0, 5.0)
    glVertex2f(10.0, 8.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(2.0, 10.0)
    glVertex2f(0.0, 8.0) 
    glEnd()
    glEndList()



    lists["3"] = glGenLists(1) 
    glNewList(lists["3"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(3.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(10.0, 3.0)
    glVertex2f(10.0, 2.0)
    glVertex2f(8.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0) 
    glEnd()
    glEndList()



    lists["4"] = glGenLists(1) 
    glNewList(lists["4"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(8.0, 0.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(10.0, 2.0) 
    glEnd()
    glEndList()



    lists["5"] = glGenLists(1) 
    glNewList(lists["5"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(10.0, 2.0)
    glVertex2f(8.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0) 
    glEnd()
    glEndList()



    lists["6"] = glGenLists(1) 
    glNewList(lists["6"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["7"] = glGenLists(1) 
    glNewList(lists["7"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(2.0, 0.0) 
    glEnd()
    glEndList()



    lists["8"] = glGenLists(1) 
    glNewList(lists["8"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["9"] = glGenLists(1) 
    glNewList(lists["9"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0) 
    glEnd()
    glEndList()
  
  
  
    lists["blue_key"] = glGenLists(1) 
    glNewList(lists["blue_key"],GL_COMPILE) 
  
      
    q=gluNewQuadric()

    glPushMatrix()


    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["blue"])


    #blue edge 1
    glPushMatrix()
    glScale(0.25,0.25,0.01)
    glTranslate(0.7,-0.75,7.5)
    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,1,1,1,10,1)  
    glTranslate(0,0,1)  
    gluDisk(q, 0.0, 1, 10, 1);     
    #glTranslate(0,0,-1)  
    #glRotate(180,1,0,0)
    #gluDisk(q, 0.0,1, 10, 1);  
    glPopMatrix()




    #blue edge 2
    glPushMatrix()
    glScale(0.25,0.25,0.01)
    glTranslate(0.7,-0.75,-9.5)
    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,1,1,1,10,1)  
    glTranslate(0,0,1)  
    #gluDisk(q, 0.0, 1, 10, 1);     
    glTranslate(0,0,-1)  
    glRotate(180,1,0,0)
    gluDisk(q, 0.0,1, 10, 1);     
    glPopMatrix()





    glPushMatrix()
    glTranslate(0.17,-0.17,-0.013)
    glRotate(45,1,0,0)
    glRotate(45,0,1,0)
    glutSolidCube(0.2)
    glPopMatrix()



    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["gold"])

    glPushMatrix()


    glScale(0.35,0.35,0.15)
    glTranslate(0.5,-0.55,-0.5)

    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,1,1,1,10,1)  

    glTranslate(0,0,1)  
    gluDisk(q, 0.0, 1, 10, 1);     

    glTranslate(0,0,-1)  
    glRotate(180,1,0,0)
    gluDisk(q, 0.0,1, 10, 1);     

    glPopMatrix()






    glPushMatrix()
    glRotatef(90,-1,0,0) 
    glRotatef(-45,0,1,0) 

    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,0.15,0.15,0.5,10,1)  

    glTranslate(0,0,0.5)  
    gluDisk(q, 0.0, 0.15, 10, 1);     

    glTranslate(0,0,-0.5)  
    glRotate(180,1,0,0)
    gluDisk(q, 0.0, 0.15, 10, 1);     
            
    glPushMatrix()
    glTranslate(-0.20,0,0)
    glTranslate(0,0,-0.4)
    glutSolidCube(0.1)
    glPopMatrix()
        
    glPushMatrix()
    glTranslate(-0.20,0,0)
    glTranslate(0,0,-0.2)
    glutSolidCube(0.1)
    glPopMatrix()

        
    glPopMatrix()


    glPopMatrix()
  
    glEndList()
  
  
  
  
  
      
      
    lists["green_key"] = glGenLists(1)
    glNewList(lists["green_key"],GL_COMPILE)    
      
    glPushMatrix()
    

    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["green"])



    glPushMatrix()
    glScale(.45,.45,0.01)
    glTranslate(0.5,-0.5,5.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glScale(.45,.45,0.01)
    glTranslate(0.5,-0.5,-5.5)
    glutSolidCube(1)
    glPopMatrix()




    glPushMatrix()
    glTranslate(0.25,-0.25,-0.0)
    glRotate(45,1,0,0)
    glRotate(45,0,1,0)
    glutSolidCube(0.15)
    glPopMatrix()




    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["gold"])

    glPushMatrix()
    glScale(.55,.55,0.1)
    glTranslate(0.4,-0.4,0)
    glutSolidCube(1)
    glPopMatrix()

    q=gluNewQuadric()
    glPushMatrix()
    glRotatef(90,-1,0,0) 
    glRotatef(-45,0,1,0) 

    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,0.15,0.15,0.5,10,1)  

    glTranslate(0,0,0.5)  
    gluDisk(q, 0.0, 0.15, 10, 1);     

    glTranslate(0,0,-0.5)  
    glRotate(180,1,0,0)
    gluDisk(q, 0.0, 0.15, 10, 1);     
            
    glPushMatrix()
    glTranslate(-0.20,0,0)
    glTranslate(0,0,-0.4)
    glutSolidCube(0.1)
    glPopMatrix()
        
    glPushMatrix()
    glTranslate(-0.20,0,0)
    glTranslate(0,0,-0.2)
    glutSolidCube(0.1)
    glPopMatrix()

        
    glPopMatrix()


    glPopMatrix()

  
  
    glEndList()
