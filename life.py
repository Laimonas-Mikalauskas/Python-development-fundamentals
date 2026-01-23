import pygame
import random


class Config:
    WIDTH = 800
    HEIGHT = 600
    CELL_SIZE = 10
    FPS = 10

    ROWS = HEIGHT // CELL_SIZE
    COLS = WIDTH // CELL_SIZE

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRID_COLOR = (40, 40, 40)


class Grid:
    def __init__(self):
        self.rows = Config.ROWS
        self.cols = Config.COLS
        self.grid = self.create_grid()

    def create_grid(self):
        return [[random.choice([0, 1]) for _ in range(self.cols)]
                for _ in range(self.rows)]

    def draw(self, surface):
        surface.fill(Config.BLACK)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col]:
                    pygame.draw.rect(
                        surface,
                        Config.WHITE,
                        (col * Config.CELL_SIZE,
                         row * Config.CELL_SIZE,
                         Config.CELL_SIZE,
                         Config.CELL_SIZE)
                    )

        # Draw grid lines (optional)
        for x in range(0, Config.WIDTH, Config.CELL_SIZE):
            pygame.draw.line(surface, Config.GRID_COLOR, (x, 0), (x, Config.HEIGHT))

        for y in range(0, Config.HEIGHT, Config.CELL_SIZE):
            pygame.draw.line(surface, Config.GRID_COLOR, (0, y), (Config.WIDTH, y))

    def count_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        count = 0

        for dr, dc in directions:
            r = row + dr
            c = col + dc

            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]

        return count

    def update(self):
        new_grid = [[0 for _ in range(self.cols)]
                    for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.count_neighbors(row, col)

                # Conway Rules
                if self.grid[row][col] == 1:
                    if neighbors == 2 or neighbors == 3:
                        new_grid[row][col] = 1
                else:
                    if neighbors == 3:
                        new_grid[row][col] = 1

        self.grid = new_grid

    def toggle_cell(self, x, y):
        col = x // Config.CELL_SIZE
        row = y // Config.CELL_SIZE

        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = 1

    def clear(self):
        self.grid = [[0 for _ in range(self.cols)]
                     for _ in range(self.rows)]


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Conway's Game of Life (OOP)")
        self.clock = pygame.time.Clock()

        self.grid = Grid()
        self.running = True
        self.paused = False

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused

                if event.key == pygame.K_c:
                    self.grid.clear()

        # Mouse drawing
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            self.grid.toggle_cell(x, y)

    def update(self):
        if not self.paused:
            self.grid.update()

    def render(self):
        self.grid.draw(self.screen)
        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(Config.FPS)
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()










































































