import pygame
import matplotlib.pyplot as plt
import numpy as np
import time

# Pygame Initialization
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Heap Sort Visualization with Bar Heights")

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


# Matplotlib plot before sorting
def plot_initial_array(arr):
    plt.figure()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title("Initial Array")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

import time

comparison_count = 0
swap_count = 0

def heapify(arr, n, i):
    global comparison_count, swap_count
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # If left child exists and is greater than root
    comparison_count += 1
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    comparison_count += 1
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        swap_count += 1
        draw_array(arr, color_position=[i, largest])  # Visualize the swap
        time.sleep(0.1)

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort_visualized(arr):
    global comparison_count, swap_count
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swap_count += 1
        draw_array(arr, color_position=[i, 0])
        time.sleep(0.1)

        # Call heapify on the reduced heap
        heapify(arr, i, 0)

    # Print statistics
    print(f"Total comparisons: {comparison_count}")
    print(f"Total swaps: {swap_count}")

# Main function
def main():
    global comparison_count, swap_count
    running = True
    clock = pygame.time.Clock()

    # Generate a random array
    arr = np.random.randint(1, 100, 50)

    # Plot initial array using Matplotlib
    plot_initial_array(arr)

    # Measure execution time
    start_time = time.time()

    # Start the Heap Sort visualization
    heap_sort_visualized(arr)

    end_time = time.time()

    # Calculate and print the execution time
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time:.4f} seconds")

    # Pygame event loop to keep the window open after sorting
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
