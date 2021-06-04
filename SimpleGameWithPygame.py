import pygame
from Gun_for_player import call_test
class Stage:

    def __init__(self):
        self.S = Stage

        self.screen_x = 1000
        self.screen_y = 600
        self.window = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.surface = pygame.Surface((self.screen_x, self.screen_y))

        self.running = True
        self.Force = None
        self.Left = None
        self.Right = None
        self.MouseDown = None
        self.Picked_Up = None
        self.stop_enemy = False
        self.Up = None
        self.Down = None

        self.Player_X = 250
        self.Player_Y = 250
        self.Player_Size = 50

        self.Enemy_X = 500
        self.Enemy_Y = 500
        self.Enemy_Size = 50
        self.Enemy_Color = (255, 0, 0)

        self.clock = pygame.time.Clock()
        self.F = .5 * (5 ** 2)
        self.enemy_speed = 180
        self.enemy_box = [self.Enemy_X, self.Enemy_Y, self.Enemy_X + self.Enemy_Size, self.Enemy_Y + self.Enemy_Size]

        self.pos = pygame.mouse.get_pos()
        self.mouse_x = 0
        self.mouse_y = 0

        self.move_x = None
        self.move_y = None
        self.dx = None
        self.dy = None
        self.Overlap_Forgiveness = self.Player_Size - 5  # <-- the lower this number the more forgiving, if its equal to self.Player_Size then you can't die

        self.bk = pygame.image.load("Game_Bullet.png").convert_alpha()
        pygame.mouse.set_visible(False)

    def Kill(self):
        if self.dx < self.Overlap_Forgiveness and self.dx > -self.Overlap_Forgiveness:
            if self.dy < self.Overlap_Forgiveness and self.dy > -self.Overlap_Forgiveness:
                self.running = False
                print("YOU DIED")

    def Enemy_Movement(self):
        pass
        self.dx, self.dy = (self.Enemy_X - self.Player_X, self.Enemy_Y - self.Player_Y)
        print(self.dx, self.dy)
        stepx, stepy = (self.dx / self.enemy_speed, self.dy / self.enemy_speed)
        self.Enemy_X -= stepx
        self.Enemy_Y -= stepy


    def Player_Movement(self):
        if self.Left:
            self.Player_X += self.F
        if self.Right:
            self.Player_X -= self.F
        if self.Up:
            self.Player_Y -= self.F
        if self.Down:
            self.Player_Y += self.F

    def Mouse_Down(self):
        self.mouse_x, self.mouse_y = self.pos
        if self.MouseDown:
            self.mouse_x, self.mouse_y = self.pos
            if self.mouse_x >= self.enemy_box[0] and self.mouse_y >= self.enemy_box[1] and self.pos <= (self.enemy_box[2], self.enemy_box[1]) and self.mouse_y <= self.enemy_box[3]:
                self.Picked_Up = True
                self.Enemy_Color = (255, 155, 0)
            if self.Picked_Up:
                self.Enemy_X, self.Enemy_Y = self.mouse_x - (self.Enemy_Size / 2), self.mouse_y - (self.Enemy_Size / 2)

    def mainloop_func(self):
        # Regulates the Frames Per Second of the Main Loop
        self.clock.tick(60)
        self.pos = pygame.mouse.get_pos()

        call_test(self.surface, self.Player_X, self.Player_Y)

        S.Player_Movement()
        self.window.blit(self.bk, (self.mouse_x - 6, self.mouse_y - 6))

        # Create a enemy
        S.Enemy_Movement()
        pygame.draw.rect(self.surface, self.Enemy_Color, (self.Enemy_X, self.Enemy_Y, self.Enemy_Size, self.Enemy_Size))


        if not self.Picked_Up:
            self.Enemy_Color = (255, 0, 0)
        if self.mouse_x >= self.enemy_box[0] and self.mouse_y >= self.enemy_box[1] and self.pos <= (self.enemy_box[2], self.enemy_box[1]) and self.mouse_y <= self.enemy_box[3]:
            self.Enemy_Color = (255, 155, 0)

        self.enemy_box = [self.Enemy_X, self.Enemy_Y, self.Enemy_X + self.Enemy_Size, self.Enemy_Y + self.Enemy_Size]

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.MouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.MouseDown = False
                self.Picked_Up = False
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.Left = True
                if event.key == pygame.K_a:
                    self.Right = True
                if event.key == pygame.K_w:
                    self.Up = True
                if event.key == pygame.K_s:
                    self.Down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.Left = False
                if event.key == pygame.K_a:
                    self.Right = False
                if event.key == pygame.K_w:
                    self.Up = False
                if event.key == pygame.K_s:
                    self.Down = False

        S.Mouse_Down()
        S.Kill()

    def Mainloop(self):
        while self.running:

            S.mainloop_func()

            # Updates the screen, make this the last line
            pygame.display.update()
S = Stage()
S.Mainloop()
