from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    a=y1-y0
    b=-1*(x1-x0)
    octant=0
    d2=2*a+b
    while x<x1:
        plot(screen,color,x,y)
        if d>0:
            y+=1
            d+=2*b
        x+=1
        d+=2*a
    #check which octant
    if a < 0: #pointing downwards
        if (y1-y0)/(x1-x0) > 1:
            #octant 7
            octant=7
        else:
            octant=8
    else:
         if (y1-y0)/(x1-x0) > 1:
             #octant 7
             octant=1
         else:
             octant=2


    pass
