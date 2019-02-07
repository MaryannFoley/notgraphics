from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(200,10,300,40,screen,color)
draw_line(300,100,200,40,screen,color)
display(screen)
save_extension(screen, 'img.png')
