def ehrenfest(number_of_balls, initial_state):

    import numpy as np
    import pygame

    win_high = 500
    win_len = 500
    window = pygame.display.set_mode((win_len, win_high))
    pygame.display.set_caption("Ehrenfest chain Simulator")
    pygame.draw.polygon(window, (255, 0, 0), ((10, 5), (10, 495), (200, 495), (200, 5)), 5)
    pygame.draw.polygon(window, (0, 255, 0), ((300, 5), (300, 495), (495, 495), (495, 5)), 5)
    pygame.display.update()

    class Box:
        def __init__(self, n_box):
            self.balls = 0
            self.n_box = n_box

        def addball(self):
            if self.n_box == 1:
                pygame.draw.circle(window, (255, 0, 0), [30 + (30 * (self.balls % 6)), 470 - (int(self.balls/6) * 30)], 10)
                self.balls += 1
            else:
                pygame.draw.circle(window, (0, 255, 0), [320 + (30 * (self.balls % 6)), 470 - (int(self.balls/6) * 30)], 10)
                self.balls += 1

        def deleteBall(self):
            if self.n_box == 1:
                self.balls -= 1
                pygame.draw.circle(window, (0, 0, 0), [30 + (30 * (self.balls % 6)), 470 - (int(self.balls/6)) * 30], 10)
            else:
                self.balls -= 1
                pygame.draw.circle(window, (0, 0, 0), [320 + (30 * (self.balls % 6)), 470 - (int(self.balls/6)) * 30], 10)

    chain = [initial_state]
    index = 1
    run = True

    # Drawing the initial state
    box_1 = Box(1)
    for j in range(initial_state):
        Box.addball(box_1)
        pygame.time.delay(100)
        pygame.display.update()

    box_2 = Box(2)
    for j in range(initial_state, number_of_balls):
        Box.addball(box_2)
        pygame.time.delay(100)
        pygame.display.update()

    # Obtaining the chain
    while run:
        choose_a_ball = np.random.randint(1, number_of_balls + 1)

        if choose_a_ball <= chain[index - 1]:
            state_index = chain[index - 1] - 1

        else:
            state_index = chain[index - 1] + 1

        chain = chain + [state_index]
        print(chain)

        # Drawing the updates
        if state_index < chain[index - 1]:
            Box.deleteBall(box_1)
            Box.addball(box_2)
        else:
            Box.addball(box_1)
            Box.deleteBall(box_2)
        pygame.time.delay(500)
        pygame.display.update()

        index += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


ehrenfest(10, 4)
