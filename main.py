import pygame
import math
import random

# Setup Display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("python Hangman Game")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 50)
MAIN_SCREEN_FONT = pygame.font.SysFont('comicsans', 60)

# Load Images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

#


# Game Variables
hangman_status = 0
words = ["LIGHT", "CHEESE", "TEST", "DEVELOPER", "PYTHON", "COMPUTER"]
wordChoice = random.choice(words)
guessedLetters = [""]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


# The function which updates the screen
def draw():
    win.fill(WHITE)

    # Renders the Title above the main area of the game.
    text = MAIN_SCREEN_FONT.render("Python Hangman v1", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Checks if a letter is valid and updates the display accordingly.
    display_word = ""
    for letterChoice in wordChoice:
        if letterChoice in guessedLetters:
            display_word += letterChoice + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw the buttons
    for letterPicked in letters:
        x, y, ltr, visible = letterPicked
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(2000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(4000)


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                distance = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                if distance < RADIUS:
                    letter[3] = False
                    guessedLetters.append(ltr)
                    if ltr not in wordChoice:
                        hangman_status += 1

    draw()

    won = True
    for letter in wordChoice:
        if letter not in guessedLetters:
            won = False
            break
    if won:
        display_message("You Won!")
        break

    if hangman_status == 6:
        display_message("You Lost")
        break

pygame.quit()
