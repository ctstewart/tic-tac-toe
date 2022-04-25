import sys, pygame
pygame.init()


def main():
    game = Game()
    game.loop()


class Game:
    def __init__(self, width=640, height=480) -> None:
        self.run = True
        self.size = self.width, self.height = width, height
        self.black = 0, 0, 0
        self.white = 255, 255, 255
        self.screen = pygame.display.set_mode(self.size)
        self.board_size = 320, 240
        self.board = Board(
            (self.width // 2 - self.board_size[0], self.height // 2 - self.board_size[1] + 10),
            self.board_size[0],
            self.board_size[1])

    def loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    sys.exit()

            self.screen.fill(self.black)
            self.board.draw(self.screen)
            # screen.blit(ball, ballrect)
            pygame.display.flip()


class Board:
    def __init__(self, offset: tuple, width=320, height=240) -> None:
        self.white = 255, 255, 255
        self.offset = offset
        self.size = self.width, self.height = width, height
        self.vert_line = width // 3, width // 3 * 2
        self.horz_line = height // 3, height // 3 * 2

    def draw(self, screen):
        for i in range(2):
            pygame.draw.line(screen, self.white, (self.vert_line[i], self.offset[0]), (self.vert_line[i], self.height))
            pygame.draw.line(screen, self.white, (self.offset[1], self.horz_line[i]), (self.width, self.horz_line[i]))


if __name__ == "__main__":
    main()