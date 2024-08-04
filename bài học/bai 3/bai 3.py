# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 400, 600
# FPS = 60
# GRAVITY = 0.1
# FLAP_STRENGTH = -10
# PIPE_GAP = 150
# PIPE_FREQUENCY = 1500  # milliseconds

# # Colors
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # Load images
# bird_image = pygame.Surface((30, 30))
# bird_image.fill(BLUE)

# pipe_image = pygame.Surface((70, HEIGHT))
# pipe_image.fill(GREEN)

# # Create the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Flappy Bird Clone")

# class Bird:
#     def __init__(self):
#         self.x = 50
#         self.y = HEIGHT // 2
#         self.velocity = 0

#     def flap(self):
#         self.velocity = FLAP_STRENGTH

#     def update(self):
#         self.velocity += GRAVITY
#         self.y += self.velocity

#     def draw(self):
#         screen.blit(bird_image, (self.x, self.y))

# class Pipe:
#     def __init__(self):
#         self.x = WIDTH
#         self.height = random.randint(100, 400)
#         self.passed = False

#     def update(self):
#         self.x -= 3

#     def draw(self):
#         screen.blit(pipe_image, (self.x, self.height - HEIGHT))
#         screen.blit(pipe_image, (self.x, self.height + PIPE_GAP))

# def main():
#     clock = pygame.time.Clock()
#     bird = Bird()
#     pipes = []
#     score = 0

#     pygame.time.set_timer(pygame.USEREVENT, PIPE_FREQUENCY)

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     bird.flap()
#             if event.type == pygame.USEREVENT:
#                 pipes.append(Pipe())

#         bird.update()

#         # Update pipes
#         for pipe in list(pipes):
#             pipe.update()
#             if pipe.x < -70:
#                 pipes.remove(pipe)
#                 score += 1  # Increment score when pipe is passed

#         # Collision detection
#         for pipe in pipes:
#             if (bird.x + 30 > pipe.x and bird.x < pipe.x + 70):
#                 if (bird.y < pipe.height or bird.y + 30 > pipe.height + PIPE_GAP):
#                     running = False  # End game on collision

#         # Draw everything
#         screen.fill(WHITE)
#         bird.draw()
#         for pipe in pipes:
#             pipe.draw()

#         # Display score
#         font = pygame.font.SysFont(None, 36)
#         text = font.render(f'Score: {score}', True, (0, 0, 0))
#         screen.blit(text, (10, 10))

#         pygame.display.flip()
#         clock.tick(FPS)

#     pygame.quit()

# if __name__ == "__main__":
#     main()









# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 400, 600
# FPS = 70
# GRAVITY = 0.6
# FLAP_STRENGTH = -9
# PIPE_GAP = 150
# PIPE_FREQUENCY = 1500  # milliseconds

# # Colors
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# # Load images
# bird_image = pygame.image.load('bài học/bai 3/bird.png')  # Load your bird image
# bird_image = pygame.transform.scale(bird_image, (50, 50))  # Resize if necessary

# pipe_image = pygame.image.load('bài học/bai 3/pipe.png')  # Load your pipe image
# pipe_image = pygame.transform.scale(pipe_image, (70, HEIGHT))  # Resize if necessary

# # Load sounds
# # flap_sound = pygame.mixer.Sound('flap.wav')  # Load flap sound
# # game_over_sound = pygame.mixer.Sound('game_over.wav')  # Load game over sound

# # Create the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Flappy Bird Clone")

# class Bird:
#     def __init__(self):
#         self.x = 50
#         self.y = HEIGHT // 2
#         self.velocity = 0
#         self.width = 50  # Width of the bird
#         self.height = 50  # Height of the bird

#     def flap(self):
#         self.velocity = FLAP_STRENGTH

#     def update(self):
#         self.velocity += GRAVITY
#         self.y += self.velocity

#     def draw(self):
#         screen.blit(bird_image, (self.x, self.y))
        
#     def get_rect(self):
#         return pygame.Rect(self.x, self.y, self.width, self.height)

# class Pipe:
#     def __init__(self):
#         self.x = WIDTH
#         self.height = random.randint(100, 400)
#         self.passed = False

#     def update(self):
#         self.x -= 3

#     def draw(self):
#         screen.blit(pipe_image, (self.x, self.height - HEIGHT))
#         screen.blit(pipe_image, (self.x, self.height + PIPE_GAP))

#     def get_rects(self):
#         # Return the rectangle for the top and bottom pipes
#         top_rect = pygame.Rect(self.x, self.height - HEIGHT, self.width, HEIGHT)
#         bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, self.width, HEIGHT)
#         return top_rect, bottom_rect
    
# def main():
#     clock = pygame.time.Clock()
#     bird = Bird()
#     pipes = []
#     score = 0

#     pygame.time.set_timer(pygame.USEREVENT, PIPE_FREQUENCY)

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:  # Left mouse button
#                     bird.flap()
#             if event.type == pygame.USEREVENT:
#                 pipes.append(Pipe())

#         bird.update()

#         # Update pipes
#         for pipe in list(pipes):
#             pipe.update()
#             if pipe.x < -70:
#                 pipes.remove(pipe)
#                 score += 1  # Increment score when pipe is passed

#         # Collision detection
#         bird_rect = bird.get_rect()
#         for pipe in pipes:
#             top_rect, bottom_rect = pipe.get_rects()
#             if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
#                 running = False  # End game on collision


#         # Draw everything
#         screen.fill(WHITE)
#         bird.draw()
#         for pipe in pipes:
#             pipe.draw()

#         # Display score
#         font = pygame.font.SysFont(None, 36)
#         text = font.render(f'Score: {score}', True, (0, 0, 0))
#         screen.blit(text, (10, 10))

#         def main_menu():
#             while True:
#                   screen.fill((255, 255, 255))
#         font = pygame.font.Font(None, 36)
#         text = font.render("Press Enter to Start", True, (0, 0, 0))
#         screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
#         pygame.display.flip()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     game_loop()

# def game_loop():
#     clock = pygame.time.Clock()
#     bird = Bird()
#     pipes = []
#     score = 0
#     paused = False

#     pygame.time.set_timer(pygame.USEREVENT, 1500)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     bird.flap()
#             if event.type == pygame.USEREVENT:
#                 pipes.append(Pipe())

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_p:  # Press 'P' to pause
#                     paused = not paused

#         if not paused:
#             bird.update()
#             for pipe in list(pipes):
#                 pipe.update()
#                 if pipe.x < -70:
#                     pipes.remove(pipe)
#                     score += 1

#         # Draw everything
#         screen.fill((255, 255, 255))
#         bird.draw()
#         for pipe in pipes:
#             pipe.draw()

#         if paused:
#             font = pygame.font.Font(None, 36)
#             text = font.render("Paused - Press P to Resume", True, (0, 0, 0))
#             screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

#         pygame.display.flip()
#         clock.tick(FPS)

#     pygame.quit()

# if __name__ == "__main__":
#     main() 

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 70
GRAVITY = 0.6
FLAP_STRENGTH = -9
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds

# Colors
WHITE = (255, 255, 255)

# Load images
bird_image = pygame.image.load('bài học/bai 3/bird.png')  # Load your bird image
bird_image = pygame.transform.scale(bird_image, (50, 50))  # Resize if necessary

pipe_image = pygame.image.load('bài học/bai 3/pipe.png')  # Load your pipe image
pipe_image = pygame.transform.scale(pipe_image, (70, HEIGHT))  # Resize if necessary

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.width = 50  # Width of the bird
        self.height = 50  # Height of the bird

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, 400)
        self.width = 70  # Width of the pipe

    def update(self):
        self.x -= 3

    def draw(self):
        screen.blit(pipe_image, (self.x, self.height - HEIGHT))
        screen.blit(pipe_image, (self.x, self.height + PIPE_GAP))

    def get_rects(self):
        # Return the rectangle for the top and bottom pipes
        top_rect = pygame.Rect(self.x, self.height - HEIGHT, self.width, HEIGHT)
        bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, self.width, HEIGHT)
        return top_rect, bottom_rect

def main_menu():
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Press Enter to Start", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()

def game_loop():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = []
    score = 0
    paused = False

    pygame.time.set_timer(pygame.USEREVENT, PIPE_FREQUENCY)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bird.flap()
            if event.type == pygame.USEREVENT:
                pipes.append(Pipe())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Press 'P' to pause
                    paused = not paused

        if not paused:
            bird.update()
            for pipe in list(pipes):
                pipe.update()
                if pipe.x < -70:
                    pipes.remove(pipe)
                    score += 1

            # Collision detection
            bird_rect = bird.get_rect()
            for pipe in pipes:
                top_rect, bottom_rect = pipe.get_rects()
                if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                     # Display "The End" message
                    font = pygame.font.Font(None, 74)
                    text = font.render("Game over", True, (255, 0, 0))
                    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    
                    screen.fill(WHITE)  # Clear the screen
                    bird.draw()  # Draw the bird
                    for pipe in pipes:
                        pipe.draw()  # Draw the pipes
                    screen.blit(text, text_rect)  # Draw the "The End" message
                    pygame.display.flip()  # Update the display
                    
                    pygame.time.delay(2000)  # Wait for 2 seconds
                    return  # End game on collision

        # Draw everything
        screen.fill(WHITE)
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        if paused:
            font = pygame.font.Font(None, 36)
            text = font.render("Paused - Press P to Resume", True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

        # Display score
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main_menu()



# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 400, 600
# FPS = 60

# # Load images
# bird_image = pygame.image.load('bird.png')  # Load your bird image
# bird_image = pygame.transform.scale(bird_image, (30, 30))  # Resize if necessary

# pipe_image = pygame.image.load('pipe.png')  # Load your pipe image
# pipe_image = pygame.transform.scale(pipe_image, (70, HEIGHT))  # Resize if necessary

# # Load sounds
# # flap_sound = pygame.mixer.Sound('flap.wav')  # Load flap sound
# # game_over_sound = pygame.mixer.Sound('game_over.wav')  # Load game over sound

# # Create the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Game with Sound and Images")

# class Bird:
#     def __init__(self):
#         self.x = 50
#         self.y = HEIGHT // 2
#         self.velocity = 0

#     def flap(self):
#         self.velocity = -10  # Flap strength
#         flap_sound.play()  # Play flap sound

#     def update(self):
#         self.velocity += 0.5  # Gravity
#         self.y += self.velocity

#     def draw(self):
#         screen.blit(bird_image, (self.x, self.y))

# class Pipe:
#     def __init__(self):
#         self.x = WIDTH
#         self.height = random.randint(100, 400)  # Random height
#         self.passed = False

#     def update(self):
#         self.x -= 3  # Move pipe left

#     def draw(self):
#         screen.blit(pipe_image, (self.x, self.height - HEIGHT))  # Draw top pipe
#         screen.blit(pipe_image, (self.x, self.height + 150))  # Draw bottom pipe

# def main():
#     clock = pygame.time.Clock()
#     bird = Bird()
#     pipes = []
#     score = 0

#     pygame.time.set_timer(pygame.USEREVENT, 1500)  # Add pipes every 1.5 seconds

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:  # Left mouse button
#                     bird.flap()
#             if event.type == pygame.USEREVENT:
#                 pipes.append(Pipe())  # Add new pipe

#         bird.update()

#         # Update pipes
#         for pipe in list(pipes):
#             pipe.update()
#             if pipe.x < -70:
#                 pipes.remove(pipe)
#                 score += 1  # Increment score when pipe is passed

#         # Draw everything
#         screen.fill((255, 255, 255))  # Clear the screen with white
#         bird.draw()
#         for pipe in pipes:
#             pipe.draw()

#         pygame.display.flip()  # Update the display
#         clock.tick(FPS)  # Control the frame rate

#     pygame.quit()

# if __name__ == "__main__":
#     main()





