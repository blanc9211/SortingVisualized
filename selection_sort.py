import pygame
import matplotlib.pyplot as plt
import numpy as np
import time

# Pygame Initialization
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Selection Sort Visualization")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Function to draw the array as vertical bars
def draw_array(arr, color_position=None, swap_position=None):
    screen.fill(BLACK)
    bar_width = width // len(arr)
    max_height = max(arr)
    
    for i, val in enumerate(arr):
        x = i * bar_width
        y = height - (val / max_height) * (height - 20)
        if color_position and i in color_position:
            color = RED
        elif swap_position and i in swap_position:
            color = BLUE
        else:
            color = GREEN
        pygame.draw.rect(screen, color, (x, y, bar_width, height))
    
    pygame.display.flip()

# Selection Sort with Visualization
def selection_sort_visualized(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_array(arr, color_position=[min_idx, j])
            time.sleep(0.05)
            
            if arr[j] < arr[min_idx]:
                min_idx = j
            draw_array(arr, color_position=[min_idx, j])
            time.sleep(0.05)
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_array(arr, swap_position=[i, min_idx])
        time.sleep(0.1)
    
    draw_array(arr)  # Final sorted array

# Matplotlib plot before sorting
def plot_initial_array(arr):
    plt.figure()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title("Initial Array")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

# Main function
def main():
    running = True
    clock = pygame.time.Clock()
    
    # Generate a random array
    arr = np.random.randint(1, 100, 20)
    
    # Plot initial array using Matplotlib
    plot_initial_array(arr)
    
    # Start the Selection Sort visualization
    selection_sort_visualized(arr)
    
    # Pygame event loop to keep the window open after sorting
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
