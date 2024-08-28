import pygame
import numpy as np
import time
from utils import setup_display, draw_array, plot_initial_array

def insertion_sort_visualized(screen, arr, width, height):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            draw_array(screen, arr, width, height, color_position=[j, j+1])
            time.sleep(0.05)
            arr[j + 1] = arr[j]
            j -= 1
            draw_array(screen, arr, width, height, color_position=[j+1])
            time.sleep(0.05)
        arr[j + 1] = key
        draw_array(screen, arr, width, height, color_position=[j+1])
        time.sleep(0.05)
    draw_array(screen, arr, width, height)

def main():
    width, height = 800, 600
    screen = setup_display(width, height, "Insertion Sort Visualization")
    
    arr = np.random.randint(1, 100, 50)
    plot_initial_array(arr)
    
    insertion_sort_visualized(screen, arr, width, height)
    
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
