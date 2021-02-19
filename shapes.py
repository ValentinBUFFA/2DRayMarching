import math
import pygame
import numpy as np

w_dim = (1000,800)
pygame.init()
pygame.key.set_repeat(5)
screen = pygame.display.set_mode(w_dim)
background = pygame.Surface(w_dim)
background.fill((38, 70, 83))

def length(ipos, fpos=(0,0)):
    return int(math.sqrt(pow(ipos[0]-fpos[0],2) + pow(ipos[1]-fpos[1],2)))

class Circle:
    def __init__(self, pos, radius):
        self.pos = pos
        self.r = radius
        pygame.draw.circle(background, (42, 157, 143), pos, radius + 1)
    
    def dst(self, ipos):
        dst = abs(length(ipos, self.pos)-self.r)
        return dst

class Rectangle:
    def __init__(self, pos, size):
        self.pos = np.add(pos,np.true_divide(size,2))
        self.size = size
        pygame.draw.rect(background, (42, 157, 143),pygame.Rect(pos,size))
    
    def dst(self, ipos):
        offset = np.subtract(ipos, self.pos)
        outside = np.maximum(np.subtract(np.absolute(offset), np.true_divide(self.size,2)), (0,0))

        return length(outside)

class Line:
    def __init__(self,pos1,pos2):
        self.A = pos1
        self.B = pos2
        self.length = length(pos1,pos2)
        pygame.draw.line(background, (42, 157, 143), pos1, pos2)
    
    def dst(self,ipos):
        if np.dot(np.subtract(self.B,self.A),np.subtract(ipos,self.A))<0:
            return length(ipos, self.A)
        if np.dot(np.subtract(self.A,self.B),np.subtract(ipos,self.B))<0:
            return(length(ipos,self.B))
        return abs((self.A[0]-self.B[0])*(self.B[1]-ipos[1])-(self.B[0]-ipos[0])*(self.A[1]-self.B[1]))/length(self.B,self.A)