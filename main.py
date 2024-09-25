from analyze import *
from record import *
from functions import *
import sys
import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 450, 800

harmonics = {'E': [82.41, 164.82, 247.23, 329.64, 412.05], 
             'A': [110, 220, 330, 440, 550], 
             'D': [146.83, 293.66, 440.49, 587.32, 734.15], 
             'G': [196, 392, 588, 784, 980], 
             'B': [246.94, 493.88, 740.82, 987.76, 1234.7], 
             'H': [329.63, 659.26, 988.89, 1318.52, 1648.15]}

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load('Guitar_Picture.png')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale if needed
    

    clock = pygame.time.Clock() 
    dt = 0
    score = 0

    #Setup Font
    font_size = 36
    font = pygame.font.Font(None, font_size)  # Use default font
    text_color = (255,255,255)  # White color

    while True:
        sys.stdout.flush()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Record Audio
        record_wav(2, 'output.wav')
        #Determine frequency and string played
        freq, string = find_frequency_and_string('output.wav')



        score_text = f"Score: {score}"
        

        #Black out screen
        screen.blit(background_image, (0,0))
        
        

        # Render the score text
        # score_text = f"Score: {score}"
        # hiscore_text = f"Hiscore: {hiscore}"
        # text_surface = font.render(score_text, True, text_color)
        # hiscore_text_surface = font.render(hiscore_text, True, text_color)
        # score_text_rect = text_surface.get_rect(topleft=(10, 10))
        # hiscore_text_rect = hiscore_text_surface.get_rect(topleft=(SCREEN_WIDTH-200, 10))
        string_picked = ""
        if string is not None:
            string_picked = f"Tuning {string} to {harmonics[string[0]][0]}"
        else:
            string_picked = "Listening for guitar!"
        current_frequency = f"Current Frequency: {round(freq,2)}"

        text_surface = font.render(string_picked, True, text_color)
        current_text_surface = font.render(current_frequency, True, text_color)

        text_rect = text_surface.get_rect(topleft=(SCREEN_WIDTH/2-150, SCREEN_HEIGHT-100))
        current_text_rect = current_text_surface.get_rect(topleft=(SCREEN_WIDTH/2-150, SCREEN_HEIGHT-50))


        #Draws score text
        screen.blit(text_surface, text_rect)
        screen.blit(current_text_surface,  current_text_rect)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
