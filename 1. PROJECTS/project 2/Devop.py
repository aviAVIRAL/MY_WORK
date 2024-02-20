# project 

import random
import time

def introduction():
    print("You are a brave knight on a quest to defeat the fearsome dragon.")
    print("You have a sword and a shield, but the dragon is powerful.")
    print("Your choices will determine your fate. Let's begin!\n")

def get_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please select from:", ", ".join(options))

def battle():
    dragon_health = 100
    player_health = 100

    while dragon_health > 0 and player_health > 0:
        print("\nDragon Health:", dragon_health)
        print("Your Health:", player_health)
        print("\nWhat will you do?")
        choice = get_input("1. Attack\n2. Defend\n3. Run\nYour choice: ", ["1", "2", "3"])

        if choice == "1":
            player_damage = random.randint(10, 20)
            dragon_damage = random.randint(5, 15)
            print(f"You strike the dragon for {player_damage} damage.")
            print(f"The dragon retaliates with a fiery breath for {dragon_damage} damage.")
            player_health -= dragon_damage
            dragon_health -= player_damage
        elif choice == "2":
            dragon_damage = random.randint(5, 15)
            print("You raise your shield to defend.")
            print(f"The dragon's attack deals only {dragon_damage // 2} damage.")
            player_health -= dragon_damage // 2
        else:
            print("You attempt to run away...")
            escape_chance = random.random()
            if escape_chance > 0.5:
                print("You managed to escape from the dragon!")
                return True
            else:
                print("You failed to escape. The battle continues.")
                dragon_damage = random.randint(10, 20)
                print(f"The dragon attacks you for {dragon_damage} damage.")
                player_health -= dragon_damage

    if player_health <= 0:
        print("You have been defeated by the dragon. Game Over.")
    else:
        print("You have defeated the dragon! Congratulations!")

def main():
    introduction()
    while True:
        play_again = get_input("Do you want to play again? (yes/no): ", ["yes", "no"])
        if play_again == "no":
            print("Thanks for playing! Goodbye.")
            break
        elif play_again == "yes":
            battle()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
import random

# List of words to choose from
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to initialize the game
def initialize_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    return word, guessed_letters, attempts

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main game loop
def hangman():
    print("Welcome to Hangman!")
    word, guessed_letters, attempts = initialize_game()

    while attempts > 0:
        print("\nWord: " + display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")
        else:
            print("Good guess!")

        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("\nYou ran out of attempts. The word was:", word)

# Start the game
hangman()
import random
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Function to generate a random list of numbers
def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to print the sorted list and measure time
def sort_and_measure_time(sorting_function, arr):
    start_time = time.time()
    sorted_arr = sorting_function(arr.copy())
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Sorted list: {sorted_arr}")
    print
print()