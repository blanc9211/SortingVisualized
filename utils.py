import pygame
import matplotlib.pyplot as plt

# Pygame Initialization
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
def setup_display(width, height, caption):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

# Function to draw the array as vertical bars
def draw_array(screen, arr, width, height, color_position=None, swap_position=None, show_values=False):
    screen.fill(BLACK)
    bar_width = width // len(arr)
    max_height = max(arr)
    
    for i, val in enumerate(arr):
        x = i * bar_width
        bar_height = (val / max_height) * (height - 50)
        y = height - bar_height
        
        if color_position and i in color_position:
            color = RED
        elif swap_position and i in swap_position:
            color = BLUE
        else:
            color = GREEN
        
        pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))
        
        if show_values:
            font = pygame.font.SysFont('Arial', 12)
            label = font.render(str(val), True, WHITE)
            label_x = x + (bar_width // 2 - label.get_width() // 2)
            label_y = y - label.get_height() - 5
            screen.blit(label, (label_x, label_y))
    
    pygame.display.flip()

# Matplotlib plot before sorting
def plot_initial_array(arr):
    plt.figure()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title("Initial Array")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()
