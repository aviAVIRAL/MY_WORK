import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 600
ARRAY_SIZE = 100
ARRAY_HEIGHT_FACTOR = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

# Generate an array of random heights
array = [random.randint(1, ARRAY_HEIGHT_FACTOR * HEIGHT // ARRAY_SIZE) for _ in range(ARRAY_SIZE)]

# Function to draw the array
def draw_array():
    for i, height in enumerate(array):
        pygame.draw.rect(screen, WHITE, (i * WIDTH // ARRAY_SIZE, HEIGHT - height, WIDTH // ARRAY_SIZE, height))

# Sorting algorithms
def bubble_sort():
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_array()
                pygame.display.update()
                pygame.time.delay(10)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def update_display():
    screen.fill(BLACK)
    draw_array()
    pygame.display.update()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                array = [random.randint(1, ARRAY_HEIGHT_FACTOR * HEIGHT // ARRAY_SIZE) for _ in range(ARRAY_SIZE)]
                update_display()
            if event.key == pygame.K_b:
                bubble_sort()
                update_display()
            if event.key == pygame.K_q:
                array = quick_sort(array)
                update_display()

pygame.quit()
sys.exit()
