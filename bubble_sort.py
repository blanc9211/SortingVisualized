import pygame
import numpy as np
import time
from utils import setup_display, draw_array, plot_initial_array

def bubble_sort_visualized(screen, arr, width, height):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_array(screen, arr, width, height, color_position=[j, j+1])
            time.sleep(0.05)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_array(screen, arr, width, height, color_position=[j, j+1])
                time.sleep(0.05)
    draw_array(screen, arr, width, height)

def main():
    width, height = 800, 600
    screen = setup_display(width, height, "Bubble Sort Visualization")
    
    arr = np.random.randint(1, 100, 50)
    plot_initial_array(arr)
    
    bubble_sort_visualized(screen, arr, width, height)
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
