import pygame
import matplotlib.pyplot as plt
import numpy as np
import time

# Pygame Initialization
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quick Sort Visualization with Bar Heights")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up font for displaying bar heights (smaller font size)
pygame.font.init()
font = pygame.font.SysFont('Arial', 12)  # Reduced font size

# Function to draw the array as vertical bars with heights
def draw_array(arr, color_position=None):
    screen.fill(BLACK)
    bar_width = width // len(arr)
    max_height = max(arr)
    
    for i, val in enumerate(arr):
        x = i * bar_width
        bar_height = (val / max_height) * (height - 50)  # Adjust for height
        y = height - bar_height

        # Set color based on the position
        color = GREEN if color_position is None or i not in color_position else RED

        # Draw the bar
        pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))
        
        # Draw the bar height as text
        label = font.render(str(val), True, WHITE)
        label_x = x + (bar_width // 2 - label.get_width() // 2)  # Center text
        label_y = y - label.get_height() - 5  # Position text slightly above the bar
        screen.blit(label, (label_x, label_y))

    pygame.display.flip()

# Quick Sort with Visualization
def quick_sort_visualized(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort the elements before and after partition
        quick_sort_visualized(arr, low, pi - 1)
        quick_sort_visualized(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pivot element
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            draw_array(arr, color_position=[i, j])  # Visualize the swapping
            time.sleep(0.05)

    # Swap the pivot element with the element at i+1 position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_array(arr, color_position=[i + 1, high])  # Visualize the final pivot swap
    time.sleep(0.05)

    return i + 1

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
    arr = np.random.randint(1, 100, 50)
    
    # Plot initial array using Matplotlib
    plot_initial_array(arr)
    
    # Start the Quick Sort visualization
    quick_sort_visualized(arr, 0, len(arr) - 1)
    
    # Pygame event loop to keep the window open after sorting
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
