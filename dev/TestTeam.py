#!/usr/bin/python
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
import pickle

import sys, traceback








class Testing:
    def __init__(self,teamFile):
    
        print(teamFile)
    
        if teamFile!=None:
            self.teams={}
            
            try:
            
                line=0
                for t in open(teamFile,"rb").read().split("\n"):
                    line+=1
                    if line==1 and t!="TEAMNAMES":
                        raise Exception("bah not a list")
                    else:
                        if len(t)>0 and line>1:
                            print(t)
                            self.teams[t]={}
                        
           
            except Exception as e:
                print("dor?")
                print (e)
                self.teams=pickle.loads(open(teamFile,"rb").read())
                
            print(self.teams)
            
            open(teamFile,"wb").write(pickle.dumps(self.teams))
            

        
if __name__ == '__main__': 

    teamFile=None

    if len(sys.argv)==2: 
            teamFile=sys.argv[1]
            
    print(teamFile)
    Testing(teamFile)
