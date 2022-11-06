import argparse
import pygame

from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.height = cell_size * life.rows
        self.width = cell_size * life.cols
        self.cell_height = life.rows
        self.cell_width = life.cols
        self.screen_size = cell_size * life.cols, cell_size*life.rows
        self.screen = pygame.display.set_mode(self.screen_size)
        self.game = life

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color(
                "black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color(
                "black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.game.curr_generation[i][j]:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("green"),
                        (j * self.cell_size, i * self.cell_size,
                         self.cell_size, self.cell_size),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("white"),
                        (j * self.cell_size, i * self.cell_size,
                         self.cell_size, self.cell_size),
                    )
        self.draw_lines()

    def render(self) -> None:
        clock = pygame.time.Clock()
        self.draw_grid()
        pygame.display.flip()
        clock.tick(10)

    def run(self) -> None:
        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # self.grid: Grid = self.create_grid(randomize=True)

        running = True
        paused = False
        while running:
            if not paused:
                self.game.curr_generation = self.game.get_next_generation()
                self.render()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = pos[0] // self.cell_size
                    y = pos[1] // self.cell_size
                    self.game.prev_generation = []  # to prevent bugs where curr_gen == prev_gen
                    self.game.curr_generation[y][x] = 1
                    self.render()
        pygame.quit()


parser = argparse.ArgumentParser()
parser.add_argument("--width", dest="width", type=int,
                    default=320, help="Field width")
parser.add_argument("--height", dest="height", type=int,
                    default=240, help="Field height")
parser.add_argument(
    "--cell-size", dest="cell_size", type=int, default=10, help="Cell size"
)
args = parser.parse_args()
if __name__ == "__main__":
    game = GameOfLife((args.height//args.cell_size,
                      args.width//args.cell_size))
    ui = GUI(game, cell_size=args.cell_size)
    ui.run()
