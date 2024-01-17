import pygame

f = open("data/Day18-2015_Input")

def print_light_grid(light_grid):
    for row in light_grid:
        for light in row:
            print(light["current_state"], end=" ")
        print()


def turn_on_corners(light_grid):
    last_row = len(light_grid)-1
    last_column = len(light_grid[0])-1

    light_grid[0][0]["current_state"] = "#"
    light_grid[last_row][0]["current_state"] = "#"
    light_grid[0][last_column]["current_state"] = "#"
    light_grid[last_row][last_column]["current_state"] = "#"

    light_grid[0][0]["next_state"] = "#"
    light_grid[last_row][0]["next_state"] = "#"
    light_grid[0][last_column]["next_state"] = "#"
    light_grid[last_row][last_column]["next_state"] = "#"


def get_next_state(row, col, light_grid):
    neighbors = get_neighbors(row, col, light_grid)
    count_on = 0
    for n in neighbors:
        if light_grid[n[0]][n[1]]["current_state"] == "#":
            count_on += 1


    # if light is on, stay on if 2 or 3 neighbors are on
    if light_grid[row][col]["current_state"] == "#":
        if count_on != 2 and count_on != 3:
            light_grid[row][col]["next_state"] = "."

    # if light is off, turn on if 3 neighbors are on
    if light_grid[row][col]["current_state"] == ".":
        if count_on == 3:
            light_grid[row][col]["next_state"] = "#"



def check_valid_point(row, col, light_grid):
    if row < 0 or col < 0:
        return False
    if row >= len(light_grid) or col >= len(light_grid[0]):
        return False
    return True


def update_state(light_grid):
    for row in light_grid:
        for light in row:
            light["current_state"] = light["next_state"]


def get_neighbors(row, col, light_grid):
    all_neighbors = []

    all_neighbors.append((row - 1, col))
    all_neighbors.append((row + 1, col))
    all_neighbors.append((row, col - 1))
    all_neighbors.append((row, col + 1))

    all_neighbors.append((row - 1, col - 1))
    all_neighbors.append((row + 1, col + 1))

    all_neighbors.append((row + 1, col - 1))
    all_neighbors.append((row - 1, col + 1))

    filtered_neighbors = []

    for neighbor in all_neighbors:
        if check_valid_point(neighbor[0], neighbor[1], light_grid):
            filtered_neighbors.append(neighbor)

    return filtered_neighbors


light_grid = []

for w in f:
    line = w.rstrip()
    row = []
    for char in line:
        light = {}
        light["current_state"] = char
        light["next_state"] = char
        light["x"] = -1
        light["y"] = -1
        row.append(light)
    light_grid.append(row)

turn_on_corners(light_grid)
rows = len(light_grid)
columns = len(light_grid[0])

# print("Original layout:")
# print_light_grid(light_grid)
# print()
steps = 10
for step in range(steps):
    for r in range(rows):
        for c in range(columns):
            get_next_state(r, c, light_grid)

    update_state(light_grid)
    turn_on_corners(light_grid)

    # print("After step", step+1)
    # print_light_grid(light_grid)
    # print()

how_many_on = 0

for row in light_grid:
    for light in row:
        if light["current_state"] == "#":
            how_many_on += 1

print("Lights on:", how_many_on)

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Courier New', 12)
pygame.display.set_caption("AP CSP Pygame!")

# set up variables for the display
size = (1400, 750)
screen = pygame.display.set_mode(size)

name = "Mr. Das"

# render the text for later
light_grid_row_one = ""
light_grid_row_two = ""
for row in light_grid[0]:
    light_grid_row_one += row["current_state"] + " "
    row["y"] = 0

for row in light_grid[1]:
    light_grid_row_two += row["current_state"] + " "
    row["y"] = 12

row_one = my_font.render(light_grid_row_one, True, (0, 0, 0))
row_two = my_font.render(light_grid_row_two, True, (0, 0, 0))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((255, 255, 255))
    screen.blit(row_one, (0, light_grid[0][0]["y"]))
    screen.blit(row_two, (0, light_grid[1][0]["y"]))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


