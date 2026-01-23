import pygame
import numpy as np

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (40, 40, 40)

# ----------------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

# Create grid
grid = np.zeros((ROWS, COLS))


# Draw grid cells
def draw_grid():
    screen.fill(BLACK)

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (col * CELL_SIZE,
                     row * CELL_SIZE,
                     CELL_SIZE,
                     CELL_SIZE)
                )

    # Draw grid lines
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))


# Count neighbors
def count_neighbors(r, c):
    total = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            nr = r + i
            nc = c + j

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                total += grid[nr][nc]

    return total


# Update logic
def update_grid():
    global grid
    new_grid = grid.copy()

    for row in range(ROWS):
        for col in range(COLS):
            neighbors = count_neighbors(row, col)

            if grid[row][col] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[row][col] = 0
            else:
                if neighbors == 3:
                    new_grid[row][col] = 1

    grid = new_grid


# Main loop
running = True
paused = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Toggle pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

            if event.key == pygame.K_c:
                grid = np.zeros((ROWS, COLS))

        # Mouse click to add cells
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            grid[row][col] = 1

    if not paused:
        update_grid()

    draw_grid()
    pygame.display.update()

pygame.quit()














































































