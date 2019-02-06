from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(200,200,100,10,screen,color)
display(screen)
save_extension(screen, 'img.png')
