# Game where the objective is to click a blue square as many times possible in a 60 second time period without clicking
# anything else

import pygame
import random

# Screen info
width = 1200
height = 900
fps = 60

# Initialize pyGame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))

# Color definitions
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
teal = (0, 100, 255)
undefinedColor = black

# Render instructions for buttons, menu and game-play
renderInstruction = 0
renderStart = 0
stopRenderMenu = 0
renderScoreScreen = 0
unrenderSprite = 0
renderSpriteHider = 0
renderSeizure = 0
renderCountdownWarning = 0

# Clock and timer
clock = pygame.time.Clock()
startClockSet = 0
startClockSet1 = 0
start_ticks = pygame.time.get_ticks()
countdown = 0

# In game values
score = 0
generateSequence = 0
initialBlockCoordinate = 0
scoreRemove = 0
stopWarning = 0

# Random coordinate generator
if initialBlockCoordinate == 0:  # Initial block spawn area is the middle
    widthPixel = width / 2
    heightPixel = height / 2
    initialBlockCoordinate = 1
else:
    widthPixel = random.randint(50, 1150)
    heightPixel = random.randint(125, 850)

# Storing previous coordinates
previousWidthPixel = widthPixel
previousHeightPixel = heightPixel

previousWidthPixel2 = widthPixel + 50
previousHeightPixel2 = heightPixel + 50

# Sprites
all_sprites = pygame.sprite.Group()


# Blue square that gives points when clicked
class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))  # what sprite looks like
        self.image.fill(blue)  # rectangle that encloses sprite
        self.rect = self.image.get_rect()
        self.rect.center = (widthPixel, heightPixel)


# Black square that hides blue square after it is clicked
class BlockHider(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))  # what sprite looks like
        self.image.fill(undefinedColor)  # rectangle that encloses sprite
        self.rect = self.image.get_rect()
        self.rect.center = (previousWidthPixel, previousHeightPixel)


# Teal square that serves as a distraction
class BlockDistract(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))  # what sprite looks like
        self.image.fill(teal)  # rectangle that encloses sprite
        self.rect = self.image.get_rect()
        self.rect.center = (widthPixel + 50, heightPixel + 50)


# Game loop
running = True
while running:
    # Runs the loop at this speed / Refresh rate
    clock.tick(fps)

    # Process events
    for event in pygame.event.get():

        # Check for closing window
        if event.type == pygame.QUIT:
            running = False

        # Detecting mouse clicks
        if event.type == pygame.MOUSEBUTTONUP:

            # Mouse x,y coordinates
            mouse = pygame.mouse.get_pos()  # Returns the mouse position

            # Instruction button
            if mouse[0] > 250 and mouse[0] < 950 and mouse[1] > 500 and mouse[1] < 590 and renderStart == 0:
                stopRenderMenu = 1
                renderInstruction = 1

            # Return button
            if mouse[0] > 20 and mouse[0] < 350 and mouse[1] > 790 and mouse[1] < 880 and renderInstruction == 1 and renderStart == 0:
                renderInstruction = 0
                stopRenderMenu = 0

            # Start button
            if mouse[0] > 350 and mouse[0] < 850 and mouse[1] > 400 and mouse[1] < 490 and renderInstruction == 0:
                stopRenderMenu = 1
                renderStart = 1

            # Menu button
            if mouse[0] > 20 and mouse[0] < 350 and mouse[1] > 790 and mouse[1] < 880 and renderScoreScreen == 1:
                renderScoreScreen = 0
                renderStart = 0
                stopRenderMenu = 0
                seconds = 0
                startClockSet = 0
                countdown = 0
                startClockSet1 = 0
                score = 0
                initialBlockCoordinate = 0
                renderSeizure = 0

            # Quit button
            if mouse[0] > 847 and mouse[0] < 1180 and mouse[1] > 790 and mouse[1] < 880 and renderScoreScreen == 1:
                running = False
            if renderStart == 1:
                if block.rect.collidepoint(mouse):
                    unrenderSprite = 1
                    previousHeightPixel = heightPixel
                    previousWidthPixel = widthPixel
                    previousHeightPixel2 = heightPixel + 50
                    previousWidthPixel2 = widthPixel + 50
                    widthPixel = random.randint(50, 1150)
                    heightPixel = random.randint(125, 850)
                else:
                    if score != 0:
                        score = score - 1

    # Updating sprites
    all_sprites.update()

    block = Block()
    all_sprites.add(block)

    blockDistract = BlockDistract()
    all_sprites.add(blockDistract)

    blockHider = BlockHider()

    if renderSpriteHider == 1:
        all_sprites.add(blockHider)

    # Draw/render everything
    # Background color before color inverting
    if renderSeizure == 0 or renderScoreScreen == 1:
        screen.fill(black)

    # Inverts background at 30 seconds in every second
    else:
        if ((round((60 + secondsPassed1) - seconds)) % 2) == 0:
            screen.fill(white)
            undefinedColor = white
        else:
            screen.fill(black)
            undefinedColor = black

    # Rendering menu buttons and title
    if stopRenderMenu == 0:
        # Start button box
        pygame.draw.rect(screen, teal, pygame.Rect(350, 400, 500, 90))

        # Instructions button box
        pygame.draw.rect(screen, teal, pygame.Rect(250, 500, 700, 90))

        # Title text
        fontInfo100 = pygame.font.Font('freesansbold.ttf', 100)
        titleText = fontInfo100.render("AIM IMPROVER", True, white)
        screen.blit(titleText, (222.5, 250))

        # Start button text
        fontInfo75 = pygame.font.Font('freesansbold.ttf', 75)
        startButtonText = fontInfo75.render("START", True, white)
        screen.blit(startButtonText, (480, 415))

        # Instructions button text
        instructionsButtonText = fontInfo75.render("INSTRUCTIONS", True, white)
        screen.blit(instructionsButtonText, (307.5, 515))

        # Game edition text
        fontInfo25 = pygame.font.Font('freesansbold.ttf', 25)
        seizureSmallText = fontInfo25.render("SEIZURE EDITION", True, white)
        screen.blit(seizureSmallText, (485, 350))

    # Rendering instructions text
    if renderInstruction == 1:
        # Return button box
        pygame.draw.rect(screen, teal, pygame.Rect(20, 790, 333, 90))

        # Instructions header
        fontInfo80 = pygame.font.Font('freesansbold.ttf', 80)
        instructionsHeaderText = fontInfo80.render("INSTRUCTIONS", True, white)
        screen.blit(instructionsHeaderText, (20, 20))

        # Return button text
        fontInfo75 = pygame.font.Font('freesansbold.ttf', 75)
        returnButtonText = fontInfo75.render("RETURN", True, white)
        screen.blit(returnButtonText, (30, 805))

        # Actual instructions for the game
        fontInfo50 = pygame.font.Font('freesansbold.ttf', 50)
        fontInfo20 = pygame.font.Font('freesansbold.ttf', 20)
        instructionsText = fontInfo50.render("Click on the blue square to get a higher score.", True, white)
        screen.blit(instructionsText, (20, 125))

        instructionsText2 = fontInfo50.render("Clicking anywhere will cost you a point.", True, white)
        screen.blit(instructionsText2, (20, 200))

        instructionsText3 = fontInfo50.render("Beware of the teal distraction squares and the", True, white)
        screen.blit(instructionsText3, (20, 275))

        instructionsText4 = fontInfo50.render("black and white ones which appear at 30", True, white)
        screen.blit(instructionsText4, (20, 350))

        instructionsText5 = fontInfo50.render("seconds in where colors invert rapidly (seizure).", True, white)
        screen.blit(instructionsText5, (20, 425))

        # Credit
        creditsText = fontInfo20.render("Game coded, designed and conceptualized by Gordon Ng.", True, white)
        screen.blit(creditsText, (600, 850))

    # Render game when start button is clicked
    if renderStart == 1 and renderScoreScreen == 0:
        # Setting the length of seconds based off of ticks
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        # Amount of time that has passed since the start button was clicked
        if startClockSet == 0:
            secondsPassed = seconds
            startClockSet = 1

        # 3, 2, 1 countdown after start is clicked
        if countdown == 0:
            fontInfo300 = pygame.font.Font('freesansbold.ttf', 300)
            # (3 + amount of time since the start button was pressed) - amount of time since the launch of the game
            textBoxBigCountdown = fontInfo300.render(str(round((3 + secondsPassed) - seconds)), True, white)
            screen.blit(textBoxBigCountdown, (500, 300))
            if round((3 + secondsPassed) - seconds) == 0:
                countdown = 1

        # Amount of time that has passed after the end of the 3, 2, 1 countdown
        if startClockSet1 == 0 and countdown == 1:
            secondsPassed1 = seconds
            startClockSet1 = 1

        # Variable detecting end of 3, 2, 1 countdown
        if countdown == 1:
            # Subtracting 1 from overall score when click is registered on somewhere that is not the blue block
            if scoreRemove == 1 and score != 0:
                score = score - 1
                scoreRemove = 0

            # Rendering the sprite group
            if unrenderSprite == 0:
                all_sprites.draw(screen)
            else:
                # Adding 1 to overall score
                score = score + 1
                unrenderSprite = 0
                renderSpriteHider = 1  # Allowing a rendering of a black box to cover previous location of the blue box

            # Detecting when time is up in game and allowing score screen to render
            if (round((60 + secondsPassed1) - seconds)) == 0:
                renderScoreScreen = 1

            # Detecting when 30 seconds has passed in game and allowing color inverting to happen
            if (round((60 + secondsPassed1) - seconds)) == 30:
                renderSeizure = 1

            # Detecting when there is 3 seconds left from color inverting and giving player a warning 3 seconds before
            if (round((60 + secondsPassed1) - seconds)) == 33 and stopWarning == 0:
                renderCountdownWarning = 1

            # Rendering of a countdown warning for color inverting
            if renderCountdownWarning == 1:
                fontInfo50 = pygame.font.Font('freesansbold.ttf', 50)
                countdownWarningText = fontInfo50.render(str(round((30 + secondsPassed1) - seconds)), True, white)
                screen.blit(countdownWarningText, (575, 175))
                countdownText = fontInfo50.render("SEIZURE IN:", True, white)
                screen.blit(countdownText, (465, 100))
                if round((30 + secondsPassed1) - seconds) == 0:
                    stopWarning = 1
                    renderCountdownWarning = 0

            # Inverting color of game information so they remain visible
            if renderSeizure == 0 or renderScoreScreen == 1:
                # When background is black and color invert is not activated
                fontInfoSize50 = pygame.font.Font('freesansbold.ttf', 50)

                # Score info
                scorePresenter = fontInfoSize50.render("SCORE:", True, white)
                screen.blit(scorePresenter, (25, 25))

                scoreValue = fontInfoSize50.render(str(score), True, white)
                screen.blit(scoreValue, (240, 25))

                # Time left info
                timePresenter = fontInfoSize50.render("TIME LEFT:", True, white)
                screen.blit(timePresenter, (800, 25))

                timeLeftValue = fontInfoSize50.render(str(round((60 + secondsPassed1) - seconds)), True, white)
                screen.blit(timeLeftValue, (1100, 25))
            else:
                # Detecting if the seconds divided by 2 returns a remainder to switch text color every 1 second
                if ((round((60 + secondsPassed1) - seconds)) % 2) == 0:
                    # When background is white
                    # Score info
                    scorePresenter = fontInfoSize50.render("SCORE:", True, black)
                    screen.blit(scorePresenter, (25, 25))

                    scoreValue = fontInfoSize50.render(str(score), True, black)
                    screen.blit(scoreValue, (240, 25))

                    # Time info
                    timePresenter = fontInfoSize50.render("TIME LEFT:", True, black)
                    screen.blit(timePresenter, (800, 25))

                    timeLeftValue = fontInfoSize50.render(str(round((60 + secondsPassed1) - seconds)), True, black)
                    screen.blit(timeLeftValue, (1100, 25))
                else:
                    # When background is black
                    # Score info
                    scorePresenter = fontInfoSize50.render("SCORE:", True, white)
                    screen.blit(scorePresenter, (25, 25))

                    scoreValue = fontInfoSize50.render(str(score), True, white)
                    screen.blit(scoreValue, (240, 25))

                    # Time info
                    timePresenter = fontInfoSize50.render("TIME LEFT:", True, white)
                    screen.blit(timePresenter, (800, 25))

                    timeLeftValue = fontInfoSize50.render(str(round((60 + secondsPassed1) - seconds)), True, white)
                    screen.blit(timeLeftValue, (1100, 25))

    # Rendering the score screen
    if renderScoreScreen == 1:
        # Menu button box
        pygame.draw.rect(screen, teal, pygame.Rect(20, 790, 333, 90))

        # Quit button box
        pygame.draw.rect(screen, teal, pygame.Rect(847, 790, 333, 90))

        fontInfoSize100 = pygame.font.Font('freesansbold.ttf', 100)

        # Score info
        scoreHeaderText = fontInfoSize100.render("SCORE", True, white)
        screen.blit(scoreHeaderText, (440, 300))

        scoreValue = fontInfoSize100.render(str(score), True, white)
        screen.blit(scoreValue, (560, 425))

        # Menu button text
        fontInfo75 = pygame.font.Font('freesansbold.ttf', 75)
        returnButtonText = fontInfo75.render("MENU", True, white)
        screen.blit(returnButtonText, (75, 805))

        # Return button text
        returnButtonText = fontInfo75.render("QUIT", True, white)
        screen.blit(returnButtonText, (910, 805))

    pygame.display.flip()

pygame.quit()
