
import pygame
import Board


class Game(object):
    def __init__(self, board):
        super(Game, self).__init__()
        self.board = board

    def display(self):
        pygame.init()
        size = width, height = 500, 300
        windowSize = (1024, 768)

        font = pygame.font.SysFont('comicsansms', 64)
        screen = pygame.display.set_mode(windowSize, 0, 32)
        pygame.display.set_caption('2048')

        text = font.render('0', True, (0, 128, 0))
        for i in range(5):
            step = int(((width/4) * i))
            pygame.draw.line(pygame.display.get_surface(),
                             pygame.Color('white'), (step, 0), (step, width))
            pygame.draw.line(pygame.display.get_surface(),
                             pygame.Color('white'), (0, step), (width, step))

        for i in range(len(self.board.getBoard()[0])):
            for j in range(len(self.board.getBoard()[0])):
                text = font.render(
                    str(self.board.getBoard()[i][j]), True, (255, 255, 255))
                screen.blit(text, (45 + j * 125, 45 + i * 125))

        pygame.display.update()
    
    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.display()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] == 1 or keys[pygame.K_s] == 1:
                self.board.move_right()
            if keys[pygame.K_UP] == 1 or keys[pygame.K_w] == 1:
                self.board.move_left()
            if keys[pygame.K_LEFT] == 1 or keys[pygame.K_a] == 1:
                self.board.move_up()
            if keys[pygame.K_RIGHT] == 1 or keys[pygame.K_d] == 1:
                self.board.move_down()
            if keys[pygame.K_RETURN] == 1:
                exit()
            clock.tick(60)
            pygame.time.wait(120)
            

game = Game(Board.Board())
game.run()
