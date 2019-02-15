from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x1<x0:
        x0,x1=x1,x0
        y0,y1=y1,y0
    if y1==y0:
        if y1<y0:
            yinc=-1
            octant=7
        else:
            yinc=1
            octant=1
    elif x1<x0: #pointing downwards
        yinc=-1
        if (y1-y0)/(x1-x0) > -1:
            #octant 7
            octant=7
        else:
            octant=8
    else:
        yinc=1
        if (y1-y0)/(x1-x0) < 1:
            #octant 1
            octant=1
        else:
            octant=2
    print(octant)
    x=x0
    y=y0
    a=y1-y0
    b=-1*(x1-x0)
    if octant == 1 or octant == 8:
        d=2*a*yinc+b
        while x<x1:
            plot(screen,color,x,y)
            if d>0:
                y+=yinc
                d+=2*b
            x+=1
            d+=2*a*yinc
    else:
        d=2*b+a*yinc
        while y<=y1:
            plot(screen,color,x,y)
            if d<0:
                x+=1
                d+=2*a
            y+=yinc
            d+=2*b
