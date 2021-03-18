import pygame


def write(text, x, y, color="Coral",):
    "Returns a surface with a text in the center of the screen, at y coord."
    # renders a font object with a text (this return a surface with a text)
    surface_text = font.render(text, 1, pygame.Color(color))
    # get the center of the text with get_rect (from surface)
    text_rect = surface_text.get_rect(center=(500 // 2, y))
    # show on the screen the surface with text at the text_rect corrdinates in the center
    screen.blit(surface_text, text_rect)
    return surface_text


def render_multiline(data):
        "converts the data with multiline string into a colored text, example: show_text"
        tc = []
        for line in data.split("\n"):

            if line != "":
                text, size, color = line.split(",")
                size = int(size)
                tc.append([text, size, color])
        # 2. Each list of the list above is send to write to render text
        for t, s, c in tc:
            for i in t.split("\n"):
                write(i, 200, s, color=c)
                s += 30
    
def show_text():
    "Text with position and color for each line to be rendered with render_multiline"
    screen.fill((0, 0, 0))
    text_container = """*** ARKAGAME ***, 30, gold
A Game by Giovanni Gatto, 80, red
pythonprogramming.altevista.org, 120, coral
Game vaguely inspired by classic games, 180, cyan
like breakout or Arkanoid, 200, cyan
CHOOSE YOUR GAME, 260, green
1 - Monochromatic, 290, coral
2 - Full color, 310, cyan
3 - Tiny breaks, 330, cyan
4 - Tiny version 2, 350, cyan
5 - Randomized Versions, 370, cyan
Use the mouse to move the bar, 450, cyan
************ August 2020 - Genuary 2021 *************, 480, gray"""
    render_multiline(text_container)

pygame.init()

font = pygame.font.SysFont("Arial", 24)
font2 = pygame.font.SysFont("Arial", 20)
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        clock.tick(30)
        show_text()
        pygame.display.update()
