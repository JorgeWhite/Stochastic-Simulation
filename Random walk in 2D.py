
def rdmwalk(lenght_of_steps):

    import numpy as np
    import pygame as py

    win_high = 500
    win_lenght = 500

    window = py.display.set_mode((win_high, win_lenght))
    py.display.set_caption("Random walk in 2D")

    initial_state = [round(win_high/2), round(win_lenght/2)]
    chain = [initial_state]
    index = 1
    state_index = initial_state
    run = True

    while run:
        direction = np.random.randint(1, 5)
        if direction == 1: # UP
            state_index = [chain[index - 1][0], chain[index - 1][1] + lenght_of_steps]

        if direction == 2: # Right
            state_index = [chain[index - 1][0] + lenght_of_steps, chain[index - 1][1]]

        if direction == 3: # Down
            state_index = [chain[index - 1][0], chain[index - 1][1] - lenght_of_steps]

        if direction == 4: # Left
            state_index = [chain[index - 1][0] - lenght_of_steps, chain[index - 1][1]]

        chain = chain + [state_index]

        py.time.delay(1)
        py.draw.line(window, (255, 0, 0), (chain[index - 1][0], chain[index - 1][1]), (chain[index][0], chain[index][1]))
        py.display.update()

        index += 1

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

rdmwalk(1)