""" 
This file is meant to be used to test various parts of the final game in static, mostly blank world.
The world is created using Tiled and pyTMX.

Features to test here include initial player movement, player attacking, enemy AI movement, and enemy attacking.
"""
import sys
import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

# start main
def main():
    #initial position for player
    playerXpos = 320 
    playerYpos = 500
    dXpos = 0
    dYpos = 0
    # Game loop
    running = True
    while running:
        screen.fill((255,255,255)) # Screen starts white before doing anything else
        #event loop -- looks for events like key presses or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            #handle movement -- consider making own function
            if event.type == pygame.KEYDOWN: #key pressed
                if event.key == pygame.K_a:
                    dXpos = -1 #move player left
                if event.key == pygame.K_d:
                    dXpos = 1 #move player right
                if event.key == pygame.K_w:
                    dYpos = -1 #move player up
                if event.key == pygame.K_s:
                    dYpos = 1 #move player down
            if event.type == pygame.KEYUP: #key released
                if event.key == pygame.K_a:
                    print("stop left")
                    dXpos = 0
                if event.key == pygame.K_d:
                    print("stop right")
                    dXpos = 0
                if event.key == pygame.K_w:
                    print("stop up")
                    dYpos = 0
                if event.key == pygame.K_s:
                    print("stop down")
                    dYpos = 0
        playerXpos += dXpos
        playerYpos += dYpos
        
        draw_map()
        
        player((playerXpos, playerYpos)) #draw player and update postion
        pygame.display.update() # Makes sure the screen is always being updated
# end main 

# start player()
# loads player into bottom middle of the world
# NOTE player sprite is pretty small, maybe try and scale it up
def player(position):
    playerImg = pygame.image.load("tile PNGs\\blueWizard.png") # Load player sprite
    #print(position)
    screen.blit(playerImg, position) # draws player to screen
# end player()

# start draw_map
def draw_map():
    tmxdata = load_pygame("rooms\\basic_room.tmx") # Load map from tmx file
    for layer in tmxdata:
        for tiles in layer.tiles():
            xPixelPos = tiles[0] * 16 #+ world_offset
            yPixelPos = tiles[1] * 16 #+ world_offset
            mapImg = tiles[2] #get img to draw from tmxdata
            screen.blit(mapImg, (xPixelPos, yPixelPos)) #draw map to screen
# end draw_map

# Initialize and run game
if __name__ == "__main__":
    width, height = 640, 640
    #init pygame
    pygame.init()
    #create screen (width, height)
    screenSize = (width, height)
    screen = pygame.display.set_mode(screenSize)
    # Window title
    pygame.display.set_caption("Untitled Rogue-Like game")
    # To set window icon: 
    # icon = pygame.image.load("image.png")
    # pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    main()  
    pygame.quit()