from tkinter import Tk
import pygame
import sys
from button import Button  # Assuming you have a Button class implemented in button.py

win = Tk()
win.attributes("-topmost", 1)
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")

# Clock for controlling frame rate
CLOCK = pygame.time.Clock()

import os

# Change the current working directory
new_directory = r'C:\Users\User\Downloads\CSP1123_Group-04\pomodoro'
os.chdir(new_directory)

# Load images
BACKDROP = pygame.image.load(r"backflower.jpg")
# Resize the background image to match screen dimensions
BACKDROP = pygame.transform.scale(BACKDROP, (WIDTH, HEIGHT))

WHITE_BUTTON = pygame.image.load(r"button.png")

# Load font
FONT = pygame.font.Font(r"ArialRoundedMTBold.ttf", 120)

# Load music
pygame.mixer.music.load("bgm.mp3.mp3")  

# Initial timer settings
POMODORO_LENGTH = 25 * 60  # 25 minutes in seconds
SHORT_BREAK_LENGTH = 5 * 60  # 5 minutes in seconds
LONG_BREAK_LENGTH = 15 * 60  # 15 minutes in seconds

# Create buttons
START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
                    pygame.font.Font(r"ArialRoundedMTBold.ttf", 20), 
                    "#c97676", "#9ab034")
POMODORO_BUTTON = Button(None, (WIDTH/2-150, HEIGHT/2-140), 120, 30, "Pomodoro", 
                pygame.font.Font(r"ArialRoundedMTBold.ttf", 20), 
                "#FFFFFF", "#9ab034")
SHORT_BREAK_BUTTON = Button(None, (WIDTH/2, HEIGHT/2-140), 120, 30, "Short Break", 
                            pygame.font.Font(r"ArialRoundedMTBold.ttf", 20), 
                            "#FFFFFF", "#9ab034")
LONG_BREAK_BUTTON = Button(None, (WIDTH/2+150, HEIGHT/2-140), 120, 30, "Long Break", 
                    pygame.font.Font(r"ArialRoundedMTBold.ttf", 20), 
                        "#FFFFFF", "#9ab034")

# Initial timer state
current_seconds = POMODORO_LENGTH
started = False

# Main loop
while True:
   dt = CLOCK.tick(60)  # dt is the time since the last frame in milliseconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                started = not started  # Toggle the timer state
            elif POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = POMODORO_LENGTH
                started = False
            elif SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = SHORT_BREAK_LENGTH
                started = False
            elif LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = LONG_BREAK_LENGTH
                started = False

    # Update timer if started
    if started and current_seconds > 0:
        current_seconds -= dt / 1000 
      
     # If the timer reaches 0, stop the timer
        if current_seconds <= 0:
            current_seconds = 0
            started = False
            pygame.mixer.music.stop()  # Stop background music

    # Clear the screen
    SCREEN.fill("#ba4949")

    # Draw the backdrop
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))

    # Update and draw buttons
    START_STOP_BUTTON.update(SCREEN)
    POMODORO_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.update(SCREEN)

    # Render timer text
    display_minutes = int(current_seconds // 60)
    display_seconds = int(current_seconds % 60)
    timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
    timer_text_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2-25))
    SCREEN.blit(timer_text, timer_text_rect)

    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos()) 
    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    CLOCK.tick(60)
