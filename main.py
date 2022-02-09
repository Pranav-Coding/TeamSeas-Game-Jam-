import pygame,sys,random,time

pygame.init()
WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Floating Trash Can")
clock = pygame.time.Clock()
font = pygame.font.Font('./fonts/Roboto-Light.ttf', 40)
print("Space to move")

def showlives():
    live = font.render(f"Lives:- {str(lives)}" , True, BLACK)
    screen.blit(live, (0, 435))
    pass
def showmoney():
    curr = font.render(f"$:- {str(money)} " , True, BLACK)
    screen.blit(curr, (220, 435))
    pass
def STARTSCREEN():
    start = font.render(f"Floating Tash Can!" , True, WHITE)
    screen.blit(start, (140, 200))
    pass
def cts():
    cta = font.render(f"Click to start" , True, WHITE)
    screen.blit(cta, (185, 250))
    pass
background = pygame.image.load("./images/background.png")
# upgrade_button_surface = pygame.Surface((50,50))
upgrade_button_surface = pygame.image.load("./images/lives.png").convert_alpha()
# upgrade_button_surface.fill(WHITE)
upgrade_button_rect = upgrade_button_surface.get_rect(center = (500,465))
# upgrade_button_surface2 = pygame.Surface((50,50))
upgrade_button_surface2 = pygame.image.load("./images/clear.png").convert_alpha()
# upgrade_button_surface2.fill(WHITE)
upgrade_button_rect2 = upgrade_button_surface.get_rect(center = (400,465))

WHITE = (255,255,255)
BLACK = (0,0,0)
Background = (38,70,83)
Foreground = (42, 157, 143)						 
# player_surface = pygame.Surface((40,60))
# player_surface.fill(WHITE)
player_surface = pygame.image.load("./images/player.png").convert_alpha()
player_rect = player_surface.get_rect(center = (50,50))
camera = [0,0]


times = pygame.USEREVENT
timer = 2500
pygame.time.set_timer(times, timer)

num_of_enemy = 8
enemy_img = []
enemy_x_change = []
enemy_y_change = []
height = [-10,-40,-70,-80,-90,-100 ]
trash = ["./images/can.png","./images/bag.png"]
for i in range(num_of_enemy):
	# x = pygame.Surface((30,30))
	# x.fill(WIDTH)
	rand_img = random.choice(trash)
	x = pygame.image.load(rand_img).convert_alpha()
	enemy_img.append(x)
	enemy_x_change.append(random.randint(0, 470))
	enemy_y_change.append(random.uniform(-1000, -10))
money = 0
def is_over(rect, pos):
	return True if rect.collidepoint(pos[0], pos[1]) else False
def collide(obj1,obj2):
	return True if obj1.colliderect(obj2) else False
def reset():
	enemy_y_change[i] = random.uniform(-1000, -10)
	enemy_x_change[i] = random.randint(0, 470)
def enemy(x,y,i):
	global money
	x_rect = enemy_img[i].get_rect(center = (x,y))
	if collide(x_rect, player_rect):
		money += 1
		reset()
	screen.blit(enemy_img[i], x_rect)


ui_bar = pygame.Surface((600,100))
ui_bar.fill((WHITE))




gravity = 0.1
side = 5
player_movement = 0
player_side_movement = 0
lives = 10
gameon = False
def rotate_bird(surface):
	new_bird = pygame.transform.rotozoom(surface, -player_movement * -16, 1)
	return new_bird


while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == times:
			pass
		if event.type == pygame.MOUSEBUTTONUP:
			mouse_pos = pygame.mouse.get_pos()
			if is_over(upgrade_button_rect, mouse_pos):
				if money >= 10:
					money -= 10
					lives += 1
				else:
					pass
			if is_over(upgrade_button_rect2, mouse_pos):
				if money >= 30:
					money -= 30
					for i in range(num_of_enemy):
						reset()
				else:
					pass

			if gameon == False:
				gameon = True
				lives = 10
				for i in range(num_of_enemy):
					reset()
				player_rect.centerx = 50
				player_rect.centery = 50
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player_movement = 0
				player_movement = -4

	# screen.fill(BLACK)
	screen.blit(background,(0,0))
	timer -= 1
	if gameon:
		player_movement += gravity
		player_rect.centery += player_movement
		if player_rect.centerx >= WIDTH:
			player_rect.centerx = WIDTH
			side = -6
		if player_rect.centerx <= 0:
			player_rect.centerx = 0
			side = 6
		player_rect.centerx += side
		for i in range(num_of_enemy):
			enemy(enemy_x_change[i], enemy_y_change[i], i)
			enemy_y_change[i] += 2
			if enemy_y_change[i] >= 700:
				lives -= 1
				if lives == 0:
					gameon = False
					money = 0
				reset()
		x = rotate_bird(player_surface)
		screen.blit(x,player_rect)
		screen.blit(ui_bar, (0,430))
		showlives()
		showmoney()
		screen.blit(upgrade_button_surface, upgrade_button_rect)
		screen.blit(upgrade_button_surface2, upgrade_button_rect2)
		if player_rect.centery >= HEIGHT + 10:
			gameon = False
	else:
		STARTSCREEN()
		cts()
	

	clock.tick(60)
	pygame.display.flip()