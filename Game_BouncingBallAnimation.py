import sys, pygame                                                  # import the package with all available Pygame modules
pygame.init()														# initialize each of those modules

size = width, height = 900, 700
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)								# create a graphical window

ball = pygame.image.load("C:\\Users\\SherryLee1990\\Desktop\\ball.png")                         # load ball.png image
ballrect = ball.get_rect()											# rect object represents a rectangular area

while True:															# infinite loop
	for event in pygame.event.get():								
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)									# move the ball
	if ballrect.left < 0 or ballrect.right > width:					
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]										# if ball moves outside of screen, reverse the speed in that direction

	screen.fill(black)												# erase the screen by filling it with a black RGB color
	screen.blit(ball, ballrect)										# draw the ball image onto the screen
	pygame.display.flip()                                           # update visible display -- call flip method after we finish 
																	# drawing, which will make everything we have drawn on the 
																	# screen become visible