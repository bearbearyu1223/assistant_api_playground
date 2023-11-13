import pygame

def play_mp3(path):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load(path)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for the music to play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


file_path = 'speech.mp3'
play_mp3(file_path)